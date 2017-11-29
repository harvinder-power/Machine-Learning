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
    labels = list(reader)
print "Labels:", labels


for x in labels:
    i
count = 0
for x in labels:
    for i in xrange(len(my_list)-1):
        if my_list[i+1][1] == "Cardiomegaly":
             count+=1
             names.append(my_list[i+1][0])
        print count
print "Cardiomegaly images", names
