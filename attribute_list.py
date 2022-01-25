import enum

"""

Satzlänge
Punktierung (!?.)
Kommas (,)
Anzahl Wortart (Nomen, Verbe, Adjektive)
Anzahl Formen von "sein" (ist, war, ...)

Spezifische Wörter

"""


class Punctuation(enum):
    UNK = -1
    EXCLAM = 0,
    QUEST = 1,
    FULLSTOP = 2


WORD_COUNT = 0
PUNCT = Punctuation.UNK
COMMAS = 0
NOUNS = 0
VERBS = 0
ADJECTIVES = 0

WORD_LIST = []
