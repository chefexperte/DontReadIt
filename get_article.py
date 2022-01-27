import os
import re
import sys
from io import open
from os.path import exists

from newspaper import Article


def get_article_local(file_name: str):
    """

    :param file_name: The name of the file the article is stored in
    :return: Returns the title and the text of the article
    """
    file_name = file_name.replace(" ", "") + ".txt"
    file_name = file_name.replace(".txt.txt", ".txt")
    title = None
    text = ""
    if not os.path.exists("articles/"):
        os.mkdir("articles/")
    if exists("articles/" + file_name):
        for line in open("articles/" + file_name).readlines():
            if title is None:
                title = line
            else:
                text += line
    else:
        print("Error opening file " + file_name)
    title = title.replace("\n", "")
    return title, text


def get_article_from_url(url: str):
    art = Article(url, language="en")
    file_name = re.match(r"https://(?:.*/)*([^/]+)", url).group(1)
    print(file_name)
    file_name = file_name.replace(" ", "") + ".txt"
    text = ""
    title = ""
    if not os.path.exists("articles/"):
        os.mkdir("articles/")
    if not exists("articles/" + file_name):
        art.download()
        art.parse()
        text = art.text
        title = art.title
        text = text.replace("\n\n", "\n")
        open("articles/" + file_name, mode="w").writelines(art.title + "\n" + text)
    else:
        for line in open("articles/" + file_name).readlines():
            if title == "":
                title = line
            else:
                text += line
    text = text.replace("\n\n", "\n")
    title = title.replace("\n", "")
    return title, text


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
