import sys
import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv), data manipulation as in SQL
import matplotlib.pyplot as plt # this is used for the plot the graph
import seaborn as sns # used for plot interactive graph. I like it most for plot
from sklearn.linear_model import LogisticRegression # to apply the Logistic regression
from sklearn.model_selection import train_test_split # to split the data into two parts
from sklearn.cross_validation import KFold # use for cross validation
from sklearn.model_selection import GridSearchCV# for tuning parameter
from sklearn.ensemble import RandomForestClassifier # for random forest classifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm # for Support Vector Machine
from sklearn import metrics # for the check the error and accuracy of the model
# Any results you write to the current directory are saved as output.
# dont worry about the error if its not working then insteda of model_selection we can use cross_validation

#Locations of data and which features you want to analyse
data = pd.read_csv(raw_input("Which file should I analyse? : "))
first_column = int(raw_input("What is the starting column number? : "))
last_column = int(raw_input("What is the last column number? : "))
outcome = raw_input('What column should I use as the outcome? : ')

features = list(data.columns[first_column:last_column])
#Setting up the variables for training and testing
train,test = train_test_split(data, test_size=0.25, random_state = 0, stratify = data[outcome])
train_x = train[train.columns[first_column:last_column]]
test_x = test[test.columns[first_column:last_column]]
test_y = test[outcome]
train_y = train[outcome]

comparison_table = []
classifiers = ['Linear SVM', 'Radial SVM', 'Logistic Regression', 'K Nearest Neighbours', 'Decision Tree']
models = [svm.SVC(kernel = 'linear'), svm.SVC(kernel = 'rbf'), LogisticRegression(), KNeighborsClassifier(n_neighbors=3), DecisionTreeClassifier()]

def function_comparator():
    for i in models:
        model = i
        model.fit(train_x, train_y)
        prediction = model.predict(test_x)
        comparison_table.append(metrics.accuracy_score(prediction, test_y))
    best_model = classifiers[np.argmax(prediction)]
    models_dataframe = pd.DataFrame(comparison_table, index = classifiers)
    models_dataframe.columns=['Accuracy']
    print models_dataframe
    print "The best model for this was:", best_model

function_comparator()
