import csv
import spacy
from spacy.pipeline import Tagger
from collections import Counter
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
import json
import numpy as np
import matplotlib.pyplot as plt

tweets = []
objects = []
actions = []
personal = []
segmentation = []

lems = []
goals = []

### load spacy for english language
nlp = spacy.load('en')
tagger = nlp.create_pipe("tagger")

### open csv file and sort responses into list of tweets
with open('SXSW.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        tweets.append(row[0])
csvFile.close()

### remove uneeded rows
tweets.remove('Wired UGC WAYWF Responses | Tracker')
tweets.remove('Original Post')
tweets.remove('Work Row')
tweets.remove('Higher Purpose')
tweets.remove('Personal Aspirations/Goals')
tweets.remove('Family & Friends')
tweets.remove('Financial')
tweets.remove('Miscellaneous')
tweets.remove('Happiness Row')
tweets.remove('Travel Row')
#print(item.text, item.lemma_, item.pos_, item.tag_, item.dep_, item.shape_, item.is_alpha, item.is_stop)

for tweet in tweets:
    category = "NA"

    ### sentiment analysis
    blob = TextBlob(tweet)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.polarity

    ### action vs object
    doc = nlp(tweet)
    item = doc[0]

    # if auxiliary or verb
    if item.dep_ == "aux" or item.pos_ == "VERB":
        actions.append(tweet)
        category = "action"

    # if nouns or pronouns or adjective
    if item.pos_ == "NOUN" and item.dep_ != "compound" and item.dep_ != "amod" or item.pos_ == "PROPN" and item.dep_ != "compound" and item.dep_ != "amod" or item.pos_ == "ADJ" and item.dep_ != "compound" and item.dep_ != "amod":
        objects.append(tweet)
        category = "object"

    # if compound or adjectival modifier or determiner or adverbial modifier
    if item.dep_ == "amod" or item.dep_ == "compound" or item.dep_ == "det" or item.pos_ == "ADP" or item.dep_ == "advmod":
        objects.append(tweet)
        category = "object"

    # if possession
    if item.lemma_ == "-PRON-":
        personal.append(tweet)
        category = "personal"

    segmentation.append( {'tweet': tweet, 'sentiment': sentiment, 'subjectivity': subjectivity, 'category': category} )


with open('segmentation.json', 'w') as file:
    json.dump(segmentation, file)

for verb in actions:
    thing = nlp(verb)

    for token in thing:
        if token.pos_ == "VERB":
            lems.append(token.lemma_)

# Create data
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter Text')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# for tweet in tweets:
#     analyze = nlp(tweet)
#     print("original:", tweet)
#     for token in analyze:
#         print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
#     print("--")

# with open('goals.json', 'r') as fp:
#     cl = NaiveBayesClassifier(fp, format="json")
#
# for tweet in tweets:
#     what = cl.classify(tweet)
#     goals.append({'tweet': tweet, 'goal': what})
#
# with open('gl.json', 'w') as file:
#     json.dump(goals, file)
























# nouns = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]
# w = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.text != '\n']
# for word in w:
#     if token.is_stop != True and token.is_punct != True and token.text != '\n' and token.pos_ == "NOUN":
#     lowercase = word.lower()
#     words.append(lowercase)

# frequent words
# word_freq = Counter(words)
# common_words = word_freq.most_common(10)
#print(common_words)
