import re


def tokenizer_multi(mult_sentences: list):
    # print(sentences)
    split = [re.findall(r"(?:\w'?)+|[.!?,;:()\[\]{}]", sentence, re.MULTILINE) for sentence in mult_sentences]
    return split


def tokenizer(single_sentence: str):
    split = re.findall(r"(?:\w'?)+|[.!?,;:()\[\]{}]", single_sentence, re.MULTILINE)
    return split


def sentencenizer(long_text):
    return re.findall(r"(.+[.!?])", long_text, re.MULTILINE)