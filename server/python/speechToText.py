import sys
import speech_recognition as sr


def main():
    path, r = sys.argv[1], sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Lyrics: " + s)
    except Exception as e:
        print("Exception: " + str(e))
    sys.stdout.flush()


if __name__ == "main":
    main()
