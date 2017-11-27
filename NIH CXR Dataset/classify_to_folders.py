import pandas as pd
import numpy as np
import os
import time
import csv

#classifiers = pd.read_csv('classifications.csv')
with open('classifications.csv', 'rb') as f:
    reader = csv.reader(f)
    my_list = list(reader)
print my_list[1]

count = 0
for i in xrange(len(my_list)-1):
    if my_list[i+1][1] == "Cardiomegaly":
         count+=1
    print count
