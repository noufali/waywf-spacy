import csv
import spacy
from spacy.pipeline import Tagger
from collections import Counter
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
import json

tweets = []

objects = []
actions = []
personal = []
lems = []

# load spacy for english language
nlp = spacy.load('en')
tagger = nlp.create_pipe("tagger")

# open csv file and sort responses into list of tweets
with open('SXSW.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        tweets.append(row[0])
csvFile.close()

# remove uneeded rows
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

# re-organize list of tweets into flat list of words (remove punctuation and stopwords)
for tweet in tweets:
    doc = nlp(tweet)
    item = doc[0]
    #print("original:", tweet)
    #print(item.text, item.lemma_, item.pos_, item.tag_, item.dep_, item.shape_, item.is_alpha, item.is_stop)
    # if verbs
    if item.dep_ == "aux" or item.pos_ == "VERB":
        actions.append(tweet)
        #print("ACTION: ", tweet)
    # if nouns or pronouns or adjective
    if item.pos_ == "NOUN" and item.dep_ != "compound" and item.dep_ != "amod" or item.pos_ == "PROPN" and item.dep_ != "compound" and item.dep_ != "amod" or item.pos_ == "ADJ" and item.dep_ != "compound" and item.dep_ != "amod":
        objects.append(tweet)
        #print("OBJECT: ", tweet)
    # if compound or adjectival modifier or determiner or adverbial modifier
    if item.dep_ == "amod" or item.dep_ == "compound" or item.dep_ == "det" or item.pos_ == "ADP" or item.dep_ == "advmod":
        objects.append(tweet)
        #print("OBJECT: ", tweet)
    # if possession
    if item.lemma_ == "-PRON-":
        personal.append(tweet)
        #print("PERSONAL: ", tweet)
    #print("--")

for verb in actions:
    thing = nlp(verb)

    for token in thing:
        if token.pos_ == "VERB":
            lems.append(token.lemma_)

# for tweet in tweets:
#     analyze = nlp(tweet)
#     print("original:", tweet)
#     for token in analyze:
#         print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
#     print("--")

with open('data.txt', 'w') as f:
    for item in actions:
        f.write("%s\n" % item)
        
# print(actions)
# print("--")
# print(objects)
# print("--")
# print(personal)























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























# sentiment analysis
# for tweet in tweets:
#     blob = TextBlob(tweet)
#     score = blob.sentiment.polarity
#     subjectivity = blob.sentiment.polarity
#     if score > 0.0:
#         pos.append({'tweet': tweet, 'score': score, 'subjectivity': subjectivity})
#     if score < 0.0:
#         neg.append({'tweet': tweet, 'score': score, 'subjectivity': subjectivity})
#     if score == 0.0:
#         neutral.append({'tweet': tweet, 'score': score, 'subjectivity': subjectivity})

# with open('pos.json', 'w') as posfile:
#     json.dump(pos, posfile)

# with open('train.json', 'r') as fp:
#     cl = NaiveBayesClassifier(fp, format="json")
#
# for tweet in tweets:
#     what = cl.classify(tweet)
#     categories.append({'tweet': tweet, 'category': what})
#
# with open('categories.json', 'w') as file:
#     json.dump(categories, file)
