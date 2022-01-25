import os
import re, sys
from os.path import exists
from io import open

from newspaper import Article


def get_article(url: str):
    art = Article(url, language="en")
    title = re.match(r"https://(?:.*/)*(.*)/", url).group(1)
    # print(title)
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


print("Initializing article downloader")
if len(sys.argv) == 2:
    print("saving article")
    get_article(sys.argv[1])
    print("finished")
else:
    print("wrong number of arguments")
