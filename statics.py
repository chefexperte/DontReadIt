"""
resources used:
"news" articles from
    thesun.co.uk
word lists from
    wordexample.com
"""

VERSION_CODE = "0.0.1"

LEARNING_RATE = 0.05

NOUNS = []
VERBS = []
ADJECTIVES = []
TO_BE = []
EXTRAS = []


def ALL_WORDS():
    return NOUNS + VERBS + ADJECTIVES + TO_BE + EXTRAS


def TOTAL():
    return len(NOUNS) + len(VERBS) + len(ADJECTIVES) + len(TO_BE) + len(EXTRAS)
