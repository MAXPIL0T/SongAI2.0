import csv
import nltk
import math
import pickle
import re
import unidecode
import contractions
import string
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')


def get_label(labels):
    for label in labels:
        if 'Folk' == label:
            return 'Folk'
        elif 'Hip Hop' == label or 'Rap' == label:
            return 'Rap'
        elif 'K-Pop' in label:
            return 'K-Pop'
        elif 'Rock' in label:
            return 'Rock'
        elif 'Pop' == label:
            return 'Pop'
        elif 'Metal' in label:
            return 'Metal'
        elif 'Funk' == label:
            return 'Funk'
        elif 'R&B' == label:
            return 'R&B'
        elif 'Country' == label:
            return 'Country'
        elif 'Indie' in label:
            return 'Indie'
        elif 'Jazz' == label:
            return 'Jazz'
        return 'OOV'


def tokenize_doc_and_more(text):
    bow = Counter()
    punctuation_table = str.maketrans('', '', string.punctuation)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    # tokenize sentences, remove whitespace and set all words to lowercase
    sentences = [re.sub(' +', ' ', sent.lower()) for sent in sent_tokenize(text)]
    # expand contractions, remove punctuation and accents
    sentences = [unidecode.unidecode(contractions.fix(sent).translate(punctuation_table)) for sent in sentences]
    # clear up any newly created whitespace
    sentences = [re.sub(' +', ' ', sent.lower()) for sent in sentences]
    # tokenize words of each sentence
    words = [word_tokenize(word) for word in sentences]
    # flatten list of words, lemmatize them, and then filter stop words
    for word in [lemmatizer.lemmatize(w) for sent in words for w in sent]:
        if word not in stop_words:
            bow.update([word])
    return bow


class NaiveBayes:
    def __init__(self, train_data=None, test_data=None, tokenizer=None, rw1=None, rw2=None, rw3=None, rw4=None):
        # Vocabulary is a set that stores every word seen in the training data
        self.tokenizer = tokenizer
        if rw1 and rw2 and rw3 and rw4:
            with open(rw1, 'rb') as w1f:
                self.class_word_counts = pickle.load(w1f)
            with open(rw2, 'rb') as w2f:
                self.class_total_doc_counts = pickle.load(w2f)
            with open(rw3, 'rb') as w3f:
                self.class_total_word_counts = pickle.load(w3f)
            with open(rw4, 'rb') as w4f:
                self.vocab = pickle.load(w4f)

        else:
            self.vocab = set()
            self.train_fn = train_data
            self.test_fn = test_data
            self.class_total_doc_counts = {"Folk": 0.0,
                                           "Rap": 0.0,
                                           "Rock": 0.0,
                                           "Pop": 0.0,
                                           "Metal": 0.0,
                                           "Funk": 0.0,
                                           "R&B": 0.0,
                                           "Country": 0.0,
                                           "K-Pop": 0.0,
                                           "Indie": 0.0,
                                           "Jazz": 0.0
                                           }

            self.class_total_word_counts = {"Folk": 0.0,
                                            "Rap": 0.0,
                                            "Rock": 0.0,
                                            "Pop": 0.0,
                                            "Metal": 0.0,
                                            "Funk": 0.0,
                                            "R&B": 0.0,
                                            "Country": 0.0,
                                            "K-Pop": 0.0,
                                            "Indie": 0.0,
                                            "Jazz": 0.0
                                            }

            self.class_word_counts = {"Folk": Counter(),
                                      "Rap": Counter(),
                                      "Rock": Counter(),
                                      "Pop": Counter(),
                                      "Metal": Counter(),
                                      "Funk": Counter(),
                                      "R&B": Counter(),
                                      "Country": Counter(),
                                      "K-Pop": Counter(),
                                      "Indie": Counter(),
                                      "Jazz": Counter()
                                      }

    def train_model(self):
        with open(self.train_fn, encoding='utf-8') as csvfile:
            csvf = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvf:
                new_label = get_label(row[1:-1])
                if new_label == "OOV":
                    continue
                text = row[-1]
                self.tokenize_and_update_model(text, new_label)

    def update_model(self, bow, label):
        self.class_total_doc_counts[label] += 1
        for word, count in zip(bow.keys(), bow.values()):
            self.vocab.add(word)
            self.class_word_counts[label].update([word])
            self.class_total_word_counts[label] += count

    def tokenize_and_update_model(self, doc, label):
        self.update_model(self.tokenizer(doc), label)

    def p_word_given_label(self, word, label):
        return self.class_word_counts[label].get(word, 0) / self.class_total_word_counts[label]

    def p_word_given_label_and_alpha(self, word, label, alpha):
        return (self.class_word_counts[label].get(word, 0) + alpha) / \
               (self.class_total_word_counts[label] + alpha * len(self.vocab))

    def log_likelihood(self, bow, label, alpha):
        return sum(math.log(self.p_word_given_label_and_alpha(word, label, alpha)) for word in bow.keys())

    def log_prior(self, label):
        label_docs = self.class_total_doc_counts[label]
        total_docs = sum(self.class_total_doc_counts.values())
        return math.log(label_docs / total_docs)

    def likelihood_ratio(self, word, alpha):
        return self.p_word_given_label_and_alpha(word, 'pos', alpha) / \
               self.p_word_given_label_and_alpha(word, 'neg', alpha)

    def unnormalized_log_posterior(self, bow, label, alpha):
        return self.log_likelihood(bow, label, alpha) + self.log_prior(label)

    def classify(self, bow, alpha):
        labels = self.class_word_counts.keys()
        return sorted([(label, self.unnormalized_log_posterior(bow, label, alpha))
                       for label in labels], key=lambda x: -x[1])[0][0]

    def evaluate_classifier_accuracy(self, alpha):
        correct = 0
        total = 0
        with open(self.test_fn, encoding='utf-8') as csvfile:
            csvf = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvf:
                new_label = get_label(row[1:-1])
                if new_label == "OOV":
                    continue
                text = row[-1]
                bow = self.tokenizer(text)
                if self.classify(bow, alpha) == new_label:
                    correct += 1
                total += 1
        return 100 * correct / total


def train_model():
    nb = NaiveBayes(train_data='train_data.csv', test_data='test_data.csv', tokenizer=tokenize_doc_and_more)
    nb.train_model()
    w1 = nb.class_word_counts
    w2 = nb.class_total_doc_counts
    w3 = nb.class_total_word_counts
    w4 = nb.vocab

    with open('w1', 'wb') as w1_file:
        pickle.dump(w1, w1_file)
    with open('w2', 'wb') as w2_file:
        pickle.dump(w2, w2_file)
    with open('w3', 'wb') as w3_file:
        pickle.dump(w3, w3_file)
    with open('w4', 'wb') as w4_file:
        pickle.dump(w4, w4_file)
    print(nb.evaluate_classifier_accuracy(0.2))


def classify_from_web(text):
    nb = NaiveBayes(tokenizer=tokenize_doc_and_more, rw1='w1', rw2='w2', rw3='w3', rw4='w4')
    bow = nb.tokenizer(text)
    return nb.classify(bow, 0.2)
