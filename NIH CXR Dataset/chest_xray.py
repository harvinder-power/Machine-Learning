import os
from os import listdir
import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.metrics import confusion_matrix
import time
from datetime import timedelta
import math
import matplotlib.pyplot as plt



#Conv Layer 1
filter_size1 = 5
num_filters1 = 16

#Conv Layer 2
filter_size2 = 5
num_filters2 = 36

#Fully Connected Layer
fc_size = 128

#Direct to the data source
train_directory = '/Volumes/SAMSUNG/Kaggle/NIH CXR Dataset/images1/images'
test_directory = '/Volumes/SAMSUNG/Kaggle/NIH CXR Dataset/images1/images 2'
print train_directory, test_directory
