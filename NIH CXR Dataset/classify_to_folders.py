import pandas as pd
import numpy as np
import os
import time
import csv


#Open classifications folder - and import data
with open('classifications.csv', 'rb') as f:
    reader = csv.reader(f)
    my_list = list(reader)

#Open determined_classifiers and add labels to a list called "labels"
with open('determined_classifiers.csv', 'rb') as f:
    reader = csv.reader(f)
    labels = list(reader)[0]
print "Labels:", labels

#initialises the counts list with zeros
counts = np.zeros(len(labels))

#creates a list within a list to allow for classifiers and their files respectively to be added
labelList = []
for i in xrange(len(labels)):
	labelList.append([])

#iterates over the samples to deteremine which files belongs to each classifier, then adds it to that list
for i in xrange(len(my_list)-1):
    for j in xrange(len(labels)):
        if my_list[i][1] == labels[j]:
             counts[j]+=1
             labelList[j].append(my_list[i+1][0])
    if my_list [i][1] not in labelList:
        print my_list[i+1][1]

print counts
print sum(counts)
