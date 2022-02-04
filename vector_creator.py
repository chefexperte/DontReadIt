import re
from os.path import exists

import statics
import tokenizer

"""
Attributes: 
    WORD_COUNT: Number of words
    DISTINCT_WORD_PERCENT: Percent of distinct words
    PUNCT: Punctuation at end of sentence
    COMMAS: Number of commas in a sentence
    NOUNS: Number of nouns (most common 1k)
    VERBS: Number of verbs (most common 1k)
    ADJECTIVES: Number of adjectives (most common 1k)
    TO_BE: Number of forms of "to be"
    WORDS_FROM_TITLE: Number of words appearing in the title
    = 9
    WORD_LIST: All words from sentence (that appear in the word list)
    -> + ALL WORDS
"""


class Punctuation:
    QUEST = -1
    UNK = 0
    FULLSTOP = 1
    EXCLAM = 2


def get_punct(last_token: str):
    if last_token == "!":
        return Punctuation.EXCLAM
    elif last_token == "?":
        return Punctuation.QUEST
    elif last_token == ".":
        return Punctuation.FULLSTOP
    else:
        return Punctuation.UNK


class VectorCreator:

    def __init__(self, sentence: str, title: str):
        self.WORD_LIST = []
        self.WORD_COUNT = 0
        self.DISTINCT_WORD_COUNT = 0
        self.PUNCT = Punctuation.UNK
        self.COMMAS = 0
        self.NOUNS = 0
        self.VERBS = 0
        self.ADJECTIVES = 0
        self.TO_BE = 0
        self.WORDS_FROM_TITLE = 0
        tokens = tokenizer.tokenizer(sentence)
        self.WORD_COUNT = len(tokens)
        self.PUNCT = get_punct(tokens[-1])
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
        title = title[0].lower() + title[1:]
        title = re.sub(r"[.!?,:;]", "", title)
        title_t = tokenizer.tokenizer(title)
        for t in title_t:
            if tokens.count(t) > 0:
                self.WORDS_FROM_TITLE += 1
        print("Processing: ", self.WORD_LIST)

    def create_sentence_vec(self):
        # 8 attributes, all words and NOT the bias
        vec_size = 8 + statics.TOTAL + 0
        vector = [self.WORD_COUNT/10, self.DISTINCT_WORD_COUNT / self.WORD_COUNT, self.PUNCT, self.COMMAS,
                  self.NOUNS / self.WORD_COUNT, self.VERBS / self.WORD_COUNT, self.ADJECTIVES / self.WORD_COUNT,
                  self.TO_BE, self.WORDS_FROM_TITLE]
        for i in range(8, vec_size):
            vector.append(self.WORD_LIST.count(statics.ALL_WORDS[i - 8]))
        # print_vector(vector)
        return vector


def load_weight_vec(file_name: str):
    vector = []
    if exists(file_name):
        for line in open(file_name, mode="r").readlines():
            line = line.replace("\n", "")
            vector.append(float(line))
        return vector


def create_empty_weight_vec():
    # 8 attributes, all words and the bias
    vec_size = 8 + statics.TOTAL + 1
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
    print("---")
    attributes = ["WORD_COUNT", "DISTINCT", "PUNCT", "COMMAS", "NOUNS", "VERBS", "ADJECTIVES", "TO_BE", "FROM_TITLE"]
    for i in range(9):
        print(attributes[i] + ": " + str(weight_list[i]))
    for i in range(9, len(weight_list) - 1):
        threshold = 0.15
        if abs(weight_list[i]) >= threshold:
            print(i, ": ", statics.ALL_WORDS[i - 9], ": ", weight_list[i])
    print("bias: " + str(weight_list[-1]))
