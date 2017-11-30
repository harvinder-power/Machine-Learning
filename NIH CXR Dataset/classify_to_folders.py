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


counts = np.zeros(len(labels))

labelList = [None]*len(labels)

for x in labels:
    for i in xrange(len(my_list)-1):
        for j in xrange(len(labels)):
            if my_list[i+1][1] == labels[j]:
                 counts[j]+=1
                 labelList[j].append(my_list[i+1][0])
            print counts

#Atelectasis	Cardiomegaly	Consolidation	Edema	Effusion	Emphysema	Fibrosis	Hernia	Infiltration	Mass	No Finding	Nodule	Pleural_Thickening	Pneumonia	Pneumothorax
