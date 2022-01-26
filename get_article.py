import os
import re
import sys
from io import open
from os.path import exists

from newspaper import Article


def get_article_local(title: str):
    title = title.replace(" ", "") + ".txt"
    text = ""
    if not os.path.exists("articles/"):
        os.mkdir("articles/")
    if exists("articles/" + title):
        for line in open("articles/" + title).readlines():
            text += line
    return text


def get_article_from_url(url: str):
    art = Article(url, language="en")
    title = re.match(r"https://(?:.*/)*([^/]+)", url).group(1)
    print(title)
    title = title.replace(" ", "") + ".txt"
    text = ""
    if not os.path.exists("articles/"):
        os.mkdir("articles/")
    if not exists("articles/" + title):
        art.download()
        art.parse()
        text = art.text
        text = text.replace("\n\n", "\n")
        open("articles/" + title, mode="w").writelines(text)
    else:
        for line in open("articles/" + title).readlines():
            text += line
    text = text.replace("\n\n", "\n")
    return text


if __name__ == "__init__":
    print("Initializing article downloader")
    if len(sys.argv) == 2:
        print("saving article")
        get_article_from_url(sys.argv[1])
        print("finished")
    elif len(sys.argv) >= 2:
        print("saving articles")
        for article in sys.argv[1:]:
            get_article_from_url(article)
    else:
        print("wrong number of arguments")
