import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json

with open('train/data.json') as json_data:
    data = json.load(json_data)
print(data)