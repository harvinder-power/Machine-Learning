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

cardiomegaly_count = 0
cardiomegaly_list = []
classifiers = []

for i in xrange(len(my_list)):
    if my_list[i][1] == 'Cardiomegaly':
        cardiomegaly_count += 1
        cardiomegaly_list.append(my_list[i][0])

#print cardiomegaly_count
#print cardiomegaly_list

#initialise the classifiers - only adding original ones to the list - classifiers
for i in xrange(len(my_list)-1):
    if ((my_list[i][1]).split('|')[0] in classifiers):
         pass
    else:
        classifiers.append(my_list[i][1].split('|')[0])
print "Classifiers", classifiers


count = 0
for i in xrange(len(my_list)):
    for j in xrange(len(classifiers)):
        if my_list[i][1] == classifiers[j]:
            count += 1
            print count
