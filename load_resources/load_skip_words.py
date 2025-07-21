from pathlib import Path


def load_skip_words():
    with open("./resources/ignore_words/IgnoreWords.txt") as iw:
        return iw.read().lower()

