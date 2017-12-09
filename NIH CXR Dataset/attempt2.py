import pandas as pd
import numpy as np
import os
import time
import csv

#Open classifications folder - and import data
with open('classifications.csv', 'rb') as f:
    reader = csv.reader(f)
    my_list = list(reader)

#Gives the image file name (i.e. [x][y] - x gives row number, and y gives column number)
print my_list[1][1]

print 'Length of list', len(my_list)

classifiers = []
for i in xrange(len(my_list)-1):
    if (my_list[i][1].split('|')[0] in classifiers):
         pass
    else:
        classifiers.append(my_list[i][1].split('|')[0])
print "Classifiers", classifiers

classifiers.remove('Finding Labels')
print classifiers

classifiers_dict = {}
for i in classifiers:
    classifiers_dict[i] = []

print "Classifiers Dictionary:", classifiers_dict

for j in xrange(len(classifiers_dict)):
    for i in xrange(len(my_list)):
        if my_list[i][0] == classifiers_dict[j]:
            classifers_dict[j].append(my_list)[i][0]
print "New Classifiers Dictionary", classifiers_dict
