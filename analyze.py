import csv
import spacy
from spacy.pipeline import Tagger
from collections import Counter
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
import json

tweets = []
words = []
pos = []
neg = []
neutral = []
categories = []

objects = []
actions = []
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

# remove first rows
tweets.remove('Wired UGC WAYWF Responses | Tracker')
tweets.remove('Original Post')
tweets.remove('Work')

# re-organize list of tweets into flat list of words (remove punctuation and stopwords)
for tweet in tweets:
    doc = nlp(tweet)
    index = 0
    print("original:", tweet)

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

        if index == 0 and token.dep_ == "aux" or index == 0 and token.pos_ == "VERB":
            actions.append(tweet)
            #tweets.remove(tweet)
            print("ACTION: ", tweet)

        if index == 0 and token.pos_ == "NOUN" and token.dep_ != "compound" and token.dep_ != "amod" or index == 0 and token.pos_ == "PROPN" and token.dep_ != "compound" and token.dep_ != "amod":
            objects.append(tweet)
            print("OBJECT: ", tweet)

        if index == 0 and token.dep_ == "amod" or index == 0 and token.dep_ == "compound" or index == 0 and token.dep_ == "det":
            objects.append(tweet)
            print("OBJECT: ", tweet)
            #tweets.remove(tweet)
            #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
        # if token.is_stop != True and token.is_punct != True and token.text != '\n' and token.pos_ == "NOUN":
        index+=1
    print("--")

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

#print(tweets)
#print("--")
#print(objects)














# nouns = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]
# w = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.text != '\n']
# for word in w:
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
