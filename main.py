import os
from os.path import exists
from time import sleep
import get_article
import regression_calc
import tokenizer
import vector_creator
import statics
from training_window import TrainingWindow

word_resources = "word_resources/"

request_close = False


def request_close_callback():
    global request_close
    request_close = True


def load_word_resources():
    if not os.path.exists(word_resources):
        os.mkdir(word_resources)
    load_resource(statics.NOUNS, "nouns.txt")
    load_resource(statics.VERBS, "verbs.txt")
    load_resource(statics.ADJECTIVES, "adjectives.txt")
    load_resource(statics.TO_BE, "to_be.txt")
    load_resource(statics.EXTRAS, "extras.txt")
    statics.ALL_WORDS = statics.NOUNS + statics.VERBS + statics.ADJECTIVES + statics.TO_BE + statics.EXTRAS
    statics.TOTAL = len(statics.ALL_WORDS)


def load_resource(list_var, file_name: str):
    if exists(word_resources + file_name):
        for line in open(word_resources + file_name):
            word = line.replace("\n", "")
            if word[0] == "#":
                return
            word = word[0].lower() + word[1:]
            list_var.append(word)


class DontReadIt:
    # weights = vector_creator.create_empty_weight_vec()

    def __init__(self):
        pass


def on_finish(weight_list: list[float], title: str, success: bool):
    # vector_creator.print_vector(weight_list)
    vector_creator.print_vector_names(weight_list)

    with open("trained_weights", mode="w") as f:
        f.writelines([str(weight) + "\n" for weight in weight_list])

    if success:
        with open("eval_list", mode="a") as f:
            f.write(title.replace(" ", "-") + ".txt\n")

    print("---")
    first = "Nothing happened, also I like food."
    second = "The most important thing to remember is: important!"
    creator = vector_creator.VectorCreator(first, title)
    s_vec = creator.create_sentence_vec()
    print("useless:   " + str(regression_calc.sigmoid(s_vec, weight_list)))
    creator2 = vector_creator.VectorCreator(second, title)
    s_vec2 = creator2.create_sentence_vec()
    print("important: " + str(regression_calc.sigmoid(s_vec2, weight_list)))


if __name__ == "__main__":
    print("Loading word resources")
    load_word_resources()
    # url = "https://www.the-sun.com/entertainment/4535847/kanye-west-slams-kim-kardashian-kissing-pete-davidson-snl/"
    # print("Loading article")
    # title, text = get_article.get_article_from_url(url)
    # print("Loading sentences")
    # sentences = tokenizer.sentencenizer(text)
    # print("Loaded: \n", sentences, "\n", tokenizer.tokenizer_multi(sentences))
    # weights = vector_creator.create_empty_weight_vec()
    # print("Trying to load already trained weights")
    # loaded_weights = vector_creator.load_weight_vec("trained_weights")
    # if loaded_weights is not None:
    #     weights = loaded_weights
    # print("Init TrainingWindow")
    # window = TrainingWindow(weights, on_finish)
    # window.add_sentences(sentences, "This is a useful important sentence.")
    # window.show_window()
    article_list = os.listdir("articles/")
    done_list = []
    if not exists("eval_list"):
        open("eval_list", "w").write("")
    for line in open("eval_list", "r").readlines():
        done_list.append(line)
    article_list = [i for i in article_list if i not in done_list]
    for file in article_list:
        if request_close:
            break
        print("Loading article file " + file)
        title, text = get_article.get_article_local(file)
        print("Article title: " + title)
        # print("Article text: " + text)
        print("Making sentences...")
        sentences = tokenizer.sentencenizer(text)
        weights = vector_creator.create_empty_weight_vec()
        print("Trying to load trained weights")
        loaded_weights = vector_creator.load_weight_vec("trained_weights")
        if loaded_weights is not None:
            weights = loaded_weights
            print("Loaded trained weights")
        print("Opening window")
        window = TrainingWindow(weights, on_finish, request_close_callback)
        window.add_sentences(sentences, title)
        window.show_window()
        print("Finished article file " + file)
        sleep(2)
        del window
