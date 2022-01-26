import os
from os.path import exists

import get_article
import regression_calc
import tokenizer
import vector_creator
import statics
from training_window import TrainingWindow


def load_word_resources():
    word_resources = "word_resources/"
    if not os.path.exists(word_resources):
        os.mkdir(word_resources)
    if exists(word_resources + "nouns.txt"):
        for line in open(word_resources + "nouns.txt"):
            statics.NOUNS.append(line.replace("\n", ""))
    if exists(word_resources + "verbs.txt"):
        for line in open(word_resources + "verbs.txt"):
            statics.VERBS.append(line.replace("\n", ""))
    if exists(word_resources + "adjectives.txt"):
        for line in open(word_resources + "adjectives.txt"):
            statics.ADJECTIVES.append(line.replace("\n", ""))
    if exists(word_resources + "to_be.txt"):
        for line in open(word_resources + "to_be.txt"):
            statics.TO_BE.append(line.replace("\n", ""))
    if exists(word_resources + "extras.txt"):
        for line in open(word_resources + "extras.txt"):
            statics.EXTRAS.append(line.replace("\n", ""))


class DontReadIt:
    # weights = vector_creator.create_empty_weight_vec()

    def __init__(self):
        pass


def on_finish(weight_list: list[float]):
    # vector_creator.print_vector(weight_list)
    vector_creator.print_vector_names(weight_list)
    print("---")
    first = "useless fish?"
    second = "important!"
    creator = vector_creator.VectorCreator(first)
    s_vec = creator.create_sentence_vec()
    print("useless:   " + str(regression_calc.sigmoid(s_vec, weight_list)))
    creator2 = vector_creator.VectorCreator(second)
    s_vec2 = creator2.create_sentence_vec()
    print("important: " + str(regression_calc.sigmoid(s_vec2, weight_list)))


if __name__ == "__main__":
    print("Loading word resources")
    load_word_resources()
    url = "https://www.the-sun.com/entertainment/4535847/kanye-west-slams-kim-kardashian-kissing-pete-davidson-snl/"
    print("Loading article")
    # text = get_article.get_article_from_url(url)
    text = get_article.get_article_local("sample_text")
    # tldr = DontReadIt()
    print("Loading sentences")
    sentences = tokenizer.sentencenizer(text)
    print("Loaded: \n", sentences, "\n", tokenizer.tokenizer_multi(sentences))
    weights = vector_creator.create_empty_weight_vec()
    print("Init TrainingWindow")
    window = TrainingWindow(weights, on_finish)
    window.add_sentences(sentences)
    window.show_window()
