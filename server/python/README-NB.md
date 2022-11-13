# Breakdown
### This file implements the pretrianed (by us) naive bayes classifier. We are using a simple bag of words approach, due mostly to time constraints and inconsistencies in the lyric formatting.

# Description
### We used this data set to train Naive Bayes to classify lyrics based on their genre: https://www.kaggle.com/datasets/neisse/scrapped-lyrics-from-6-genres?select=artists-data.csv 

### For text preprocessing: # I used the tokenizer from the nltk, and at first I stripped the top k hits from the bag of words, as they are too common to provide any real information gain. I found k = 7 to perform the best, though the improvement is minimal. Then I decided to import a stopword dictionary and used that instead of the top k which worked better.
# Stripping punctuation also helped performance.
# Counting all words as their lower case further increases performance
# tried tokenizing sentences before tokenizing each word of those sentences and then combining words. This didn't help at first, but some batch processing on the sentences before tokenizing the words did improve performance.
# The majority of the batch processing was contraction expansion and accent removal. This helped to normalize text, though an MUCH more efficient, albiet less accurate contraction expansion library had to be used because pycontractions was just too slow.
# After the text was processed, we trained nieve bayes using bag of words. We split our dataset into 90/10 for training and test set respectivly. The accuracy on the test set was rather low (about 40%), however for some categories like rap we found much higher real world performance. Metal seemes to be a little harder to classify, though when the model gets it 'wrong' it tends to not be too wrong. We didn't see rap miscassified as folk, for example. 

# Libraries
### csv, nltk(tokenizing), math, pickle(to save our model), re(more tokenizing), unidecode (more tokenizing, removes accents), contractions(more tokenizing), string (gets list of punctuation to strip), collections counter (tf).

# Dependencies
### nltk premade lists (punkt, stopwords), Python 3.10, w1, w2, w3, w4 (files for the pretrained model)

# Building
### N/A, python is interpreted

# Running
### import classify_from_web from get_genre.py (this file) and call classify_from_web with a string containing lyrics
