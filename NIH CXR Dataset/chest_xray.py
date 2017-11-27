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
import fnmatch

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')
test_dir = 'test'


for img in os.listdir('test'):
    if fnmatch.fnmatch(img, '*.png'):
        img_loaded = image.load_img(img, target_size=(224, 224))
        x = image.img_to_array(img_loaded)
        print x
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)


preds = model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])
