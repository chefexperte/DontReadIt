# DontReadIt
## What is this?
This project is a small ui program written for Gtk 3.0 in Python with PyGObject. 
It uses linear regression to calculate which sentences in a news article are important, and which are not. 
## Training?
For training I have used simple "news" articles from The Sun UK 
(which is a UK magazine that calls itself a newspaper, but it's more like reality tv).
### Attributes
To decide if a sentence is important or not, every attribute is calculated with the value and weight + bias. 

The things I consider for a sentence are: 
- The number of words the sentence has
- The percent of distinct words
- The punctuation at end of the sentence
- The number of commas in a sentence
- The count of the first 1k most common nouns, adjectives and verbs
- The count of forms of "to be"
- The number of words appearing in the sentence that are also in the title

## Results?
The results are mixed, sometimes it can be a little bit better than random sentence selection (in my opinion), but other times not. 
It is/was a small project for university, which I did take a little too far for the first semester. 

I don't think linear regression, so few measured attributes and so little could produce that much better results, so it's not disappointing. 
It should be pretty simple to extend the program to use either
- a more complex method of calculating the weights
- adding more attributes
- making downloading news articles more simple/automatic

# How to use the program
There are two ways how you can use this program. 
## Adding news articles
Run get_article.py followed by as many links to news articles as you please. 

I am using [Newspaper3k](https://github.com/codelucas/newspaper) by Lucas Ou-Yang to extract the text and title from the articles, so you don't need to do any of the work, just paste the links. 
## Training the thing and testing the results
Run main.py