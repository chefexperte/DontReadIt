import statics
import tokenizer

"""

Satzlänge
Punktierung (!?.)
Kommas (,)
Anzahl Wortart (Nomen, Verbe, Adjektive)
Anzahl Formen von "sein" (ist, war, ...)

Spezifische Wörter

"""


class Punctuation:
    QUEST = -1
    UNK = 0
    FULLSTOP = 1
    EXCLAM = 2


class VectorCreator:

    # WORD_LIST = []

    def __init__(self, sentence: str):
        self.WORD_LIST = []
        self.WORD_COUNT = 0
        self.DISTINCT_WORD_COUNT = 0
        self.PUNCT = Punctuation.UNK
        self.COMMAS = 0
        self.NOUNS = 0
        self.VERBS = 0
        self.ADJECTIVES = 0
        self.TO_BE = 0
        tokens = tokenizer.tokenizer(sentence)
        self.WORD_COUNT = len(tokens)
        self.PUNCT = self.get_punct(tokens[-1])
        for t in tokens:
            if statics.NOUNS.count(t) >= 1:
                self.NOUNS += 1
            if statics.VERBS.count(t) >= 1:
                self.VERBS += 1
            if statics.ADJECTIVES.count(t) >= 1:
                self.ADJECTIVES += 1
            if statics.TO_BE.count(t) >= 1:
                self.TO_BE += 1
            if self.WORD_LIST.count(t) == 0:
                self.WORD_LIST.append(t)
                self.DISTINCT_WORD_COUNT += 1
            if t == ",":
                self.COMMAS += 1
        print("Processing: ", self.WORD_LIST)

    def get_punct(self, last_token: str):
        if last_token == "!":
            return Punctuation.EXCLAM
        elif last_token == "?":
            return Punctuation.QUEST
        elif last_token == ".":
            return Punctuation.FULLSTOP
        else:
            return Punctuation.UNK

    """
    Attributes: 
        WORD_COUNT
        DISTINCT_WORD_COUNT
        PUNCT
        COMMAS
        NOUNS
        VERBS
        ADJECTIVES
        TO_BE
        = 8
        WORD_LIST
        -> + ALL WORDS
    """

    def create_sentence_vec(self):
        # 8 attributes, all words and NOT the bias
        vec_size = 8 + statics.TOTAL() + 0
        vector = []
        vector = [self.WORD_COUNT, self.DISTINCT_WORD_COUNT, self.PUNCT, self.COMMAS, self.NOUNS, self.VERBS,
                  self.ADJECTIVES, self.TO_BE]
        for i in range(8, vec_size):
            vector.append(self.WORD_LIST.count(statics.ALL_WORDS()[i - 8]))
        # print_vector(vector)
        return vector


def create_empty_weight_vec():
    # 8 attributes, all words and the bias
    vec_size = 8 + statics.TOTAL() + 1
    vector = []
    for i in range(vec_size):
        vector.append(0)
    return vector


def print_vector(weight_list: list[float]):
    print("Length: " + str(len(weight_list)))
    for i in range(len(weight_list)):
        if weight_list[i] != 0:
            print(i, ": ", weight_list[i])


def print_vector_names(weight_list: list[float]):
    print("Length: " + str(len(weight_list)))
    for i in range(8, len(weight_list)-1):
        if weight_list[i] != 0:
            print(i, ": ", statics.ALL_WORDS()[i - 8], ": ", weight_list[i])
    print("bias: " + str(weight_list[-1]))