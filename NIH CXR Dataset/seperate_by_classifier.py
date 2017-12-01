import csv

with open('classifications.csv', 'rb') as f:
    reader = csv.reader(f)
    my_list = list(reader)
print my_list[1]

count = 0
classifiers = []

for i in xrange(len(my_list)-1):
    if (my_list[i][0].split('|')[0] in classifiers):
         pass
    else:
        classifiers.append(my_list[i][0])
print(classifiers)
