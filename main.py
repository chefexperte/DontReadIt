import re

import get_article
from main_window import TrainingWindow
from statics import VERSION_CODE


class DontReadIt:
    text = ""

    def __init__(self):
        pass
        # self.text = str(input_text)

    def sentencenizer(self, text):
        return re.findall(r"(.+[.!?])", text, re.MULTILINE)

    def tokenizer(self, sentences):
        # print(sentences)
        split = [re.findall(r"(?:\w'?)+|[.!?,;:()\[\]{}]", sentence, re.MULTILINE) for sentence in sentences]
        return split


if __name__ == "__main__":
    sample_text = """
    This is a sample text.
    An important thing to consider is an example. 
    But besides that there is not much more to it. 
    But whatever, I like it the way it is. I don't know 
    how much we can do anymore but that's fine or whatever. 
    The amount of water on earth is a big amount. 
    More than 12 litres I think, but I am not sure.
    """
    url = "https://www.the-sun.com/entertainment/4535847/kanye-west-slams-kim-kardashian-kissing-pete-davidson-snl/"
    text = get_article.get_article(url)
    tldr = DontReadIt()
    sentences = tldr.sentencenizer(text)
    print("Init\n", sentences, "\n", tldr.tokenizer(sentences))
    window = TrainingWindow()
    window.add_sentences(sentences)
    window.show_window()
