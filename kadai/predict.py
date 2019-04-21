import nltk
import sys
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import operator
import mysql.connector
# for delay
import time
# for escape string
import html
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# restart if return false
# import subprocess
# filename = 'predict.py'
# restore all of data structures

file_dir = os.path.dirname(os.path.abspath(__name__))
training_data_js_path = os.path.join(file_dir, 'train/data.json')
model_data_path = os.path.join(file_dir, 'model.tflearn')
load_pickle_path = os.path.join(file_dir, 'training_data')
# print(file_dir)
# print(training_data_js_path)
# print(model_data_path)
# print(load_pickle_path)
# exit()
import pickle
# data = pickle.load( open( "training_data", "rb" ) )
data = pickle.load( open( load_pickle_path, "rb" ) )
#install Location class
from location import Location
location = Location
# place = location.getLocationName('kawasaki')
# print(place)
# exit()
#import Weather class
from weatherdata import Weather
weather = Weather()
# api_key = "c0c04cd3ca1920f3864260b49e44a68e"
# print(data)
# exit()
from database import Database
database = Database()


words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']
# import our chat-bot intents file
import json
with open(training_data_js_path) as json_data:
    intents = json.load(json_data)
# print(intents)
# exit()
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# load our saved model
# model.load('./model.tflearn')
model.load(model_data_path)

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

# p = bow('who are you?', words)
# print(p)
# exit()
# data structure to hold user context
context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
    results = model.predict([bow(sentence, words)])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list

def findBestTag(sentence):
    results = classify(sentence)
    # print(results)
    # print(len(results))
    # exit()
    results_set = {}
    for i in range(len(results)):
        return_set = results_set.update({results[i][0]:results[i][1]})
    # best_result = max(results_set.items())
    # print(best_result)
    best_result = max(results_set.items(), key=lambda k: k[1])
    # print(best_tag)
    # print(best_result)
    # exit()
    if (best_result[1] > 0.5):
        return best_result[0]
    # return best_tag
    # for result in results:
    #     if result[1] > 0.6:
    #         break
    #         print(result[0], result[1])
    # return result[0]

def response(sentence, userID='1', show_details=False):
    results = classify(sentence)
    # print(results)
    if results:
        for result in results:
            # print(result)
            # exit()
            while results:
                for i in intents['intents']:
                    if i['tag'] == results[0][0]:
                        if 'context_set' in i:
                            if show_details: print ('context:', i['context_set'])
                            context[userID] = i['context_set']
                        if not 'context_filter' in i or \
                            (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                            if show_details: print ('tag:', i['tag'])
                            return print(random.choice(i['responses']))

                results.pop(0)

# text = input(">>: ")
# tag = findBestTag(text)
# print(tag)
# exit()
# classify('Hi')
condition = True

while condition:
    text = input(">>: ")
    tag = findBestTag(text)
    if (tag == 'goodbye'):
        response(text)
        condition = False
    elif (tag is None):
        # print('sr, I don\'t understand')
        print('sr, I don\'t understand, can you explain to me?')
        time.sleep(1)
        unknow = input("<<: ")
        time.sleep(1.5)
        print('thank you. It\'s mean "' + unknow + '"')
        time.sleep(1.5)
        print('I\'ll save it to my data')    
        sql = """ INSERT INTO `chat_logs`
                          (`theme`, `log`) VALUES (%s,%s)"""
        log = (unknow, text)
        # time.sleep(2)
        database.insertLog(sql, log)
        # p = subprocess.Popen('/usr/bin/python3 '+filename, shell=True).wait(endtime=None)
    elif (tag == 'weather'):
        print('Where do you want to search?')
        location_text = input(">>: ")
        response(text)
        coordinate = location.getLocationByCoordinate(location_text)
        weather_data = weather.getWeatherData(coordinate['latitude'], coordinate['longitude'])
        result = weather.getWeatherCurrently(weather_data) 
    else:
        response(text)
# while text:
# # print(findBestTag(text))
# # exit()
# # print(findTag(text))
# # exit()
#     while (findBestTag(text) != None):
#         if (findBestTag != 'goobye'):
#             response(text)
#             exit()
#         else:
#             response(text)
#             re_text = input(">>: ")

#     while (findBestTag(text) is None):
#         print('sorry, Tinker don\'t understand, what is it mean?')
#         re_text = input("<<:")
#         if (findBestTag != 'goobye'):
#             response(text)
#             exit()
#         else:
#             response(text)
#             re_text = input(">>: ")

# if findBestTag(text) is None:
#     response(text)
#     exit()
# elif findTag(text) is None:
#     print("Sorry, I don\'t understand. What is it mean")
#     retext = input(">>:")
#     while findTag(retext) != 'goodbye':
#         if findTag(retext) != 'goodbye':
#             response(retext)
#         elif findTag(retext) is None:
#             print("Sorry, I don\'t understand. What is it mean")
#             retext = input("<<:")
#             if findTag(text) != 'goodbye':
#                 response(text)
#             else:
#                 response(text)
#                 exit()
            
#         else:
#             response(retext)
#             exit()
# else:
#     while findTag(text) != 'goodbye':
#         retext = input(">>>: ")
#         if findTag(retext) != 'goodbye':
#             response(retext)
#         else:
#             response(retext)
#             exit()

# tag = findTag(text)
# print(tag)
# https://github.com/sigilioso/tensorflow-build/raw/master/tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl