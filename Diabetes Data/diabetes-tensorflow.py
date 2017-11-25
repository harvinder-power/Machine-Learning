import numpy as np
import tensorflow as tf
import pandas as pd


data = data = pd.read_csv("diabetes.csv")
features = list(data.columns[1:8])
outcomes = list(data.columns[9])
#import data and set features to be all data except the diagnosis

train,test = train_test_split(data, test_size=0.25, random_state = 0, stratify = data['Outcome'])
train_x = train[train.columns[:8]]
test_x = test[test.columns[:8]]

test_y = test['Outcome']
train_y = train['Outcome']
#split data into train and test sets - with 25% being for testing.


tf_features = tf.placeholder("float", [0,len(features)])
tf_classifier = tf.placeholder("float", [0, len(outcomes)])
if tf_classifier > tf_features:
    sess.end()
else:
    run.sess()
