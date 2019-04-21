import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with open('train/data.json') as json_data:
    intents = json.load(json_data)
# print(intents)
# exit()
words = []
classes = []
documents = []
stop_words = ['?', 'a', 'an', 'the', '\'s', 'is', 'will', 'about']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # print(pattern)
        # exit()
        w = nltk.word_tokenize(pattern)
        # print(w)
        # exit()
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(documents)
# exit()
words = [stemmer.stem(w.lower()) for w in words if w not in stop_words]
# print(words)
# exit()
words = sorted(list(set(words)))
# print(words)
# exit()
classes = sorted(list(set(classes)))
# print(classes)
# exit()
# create our training data
training = []
output = []
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)
# print(training)
# exit()
# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])
# print(train_x)
# print(train_y)
# exit()
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')
# https://www.pugetsystems.com/labs/hpc/The-Best-Way-to-Install-TensorFlow-with-GPU-Support-on-Windows-10-Without-Installing-CUDA-1187/
# save all of our data structures
import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )
