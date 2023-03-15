#list imports here
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import keras
#from keras.layers import Input, Dense, Flatten
from keras.models import model_from_json



def useModel(jpath="C:\\Users\\leode\\isef_2022-23\\model2.json",
            jweights="C:\\Users\\leode\\isef_2022-23\\model2.h5", *args):
    jfile = open(jpath, 'r')
    loaded_model_jfile = jfile.read()
    jfile.close()
    load_model = model_from_json(loaded_model_jfile)
    load_model.load_weights(jweights)
    load_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

class C3BO:

    def __init__(self, ):
        self.a = None


    


