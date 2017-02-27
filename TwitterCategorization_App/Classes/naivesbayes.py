#import nltk
import random
import re

path="/Users/tushar/Desktop/Py_Hackathon/data.txt"
data = []

with open(path) as f:
	for tweet in f:
		data.append({['tweet']:tweet,'[label]':'Personal'})


#size = int(len(data) * 0.9)

#train_data = data[:size]
#test_data = data[size:]

#train_set = [line.rstrip() for line in open(path)]

# pick a classifier
#classifier = nltk.NaiveBayesClassifier

# train classifier using training set
#classifier = nltk.NaiveBayesClassifier.train(train_set)

#classifier.show_most_informative_features(20)
print data