#list imports here
import numpy as np
#from keras.layers import Input, Dense, Flatten
from keras.models import model_from_json

"""
This entire file will be inherited by the website code (Flask/html), so
the following components will be included:
    * a compiled loaded_model with arbitrary loss function
    * main algorithm highlighting this project
    * other interpretable algorithms used to compare to revprop
    * clear visualization of results
    ? maybe information on lingual scripts

"""

def useModel(jpath="C:\\Users\\leode\\isef_2022-23\\model2.json",
            jweights="C:\\Users\\leode\\isef_2022-23\\model2.h5", *args):
    jfile = open(jpath, 'r')
    loaded_model_jfile = jfile.read()
    jfile.close()
    load_model = model_from_json(loaded_model_jfile)
    load_model.load_weights(jweights)
    load_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    return load_model

#this class assumes the user knows where the flattened and dense layers reside
class RevProp:
    
    def __init__(self, model, startLay, ignoreLays):
        self.layers = model.layers
        self.endLay = startLay
        self.ignoreLays = ignoreLays
        self.denseNeurons = dict() #general call: denseNeurons["lay_i"] = 
        
        self.image = None
        self.resImage = np.zeros(6912,)
        
    """Things to not forget (checklist)
        * consider biases, which differ between answers
        * the call for weights is self.layers[currLay].weights[0][:, answer]
        * experiment on criteria for top Q in currLay (not simply highest values)
        * ...
    """
    
    def setImage(self, newImage):
        #great method for not having to create a million objects of RevProp
        self.image = newImage
        if newImage.ndim == 3:
            self.image = np.expand_dims(self.image, axis=0)
    
    #passing image through dCNN to get the neuron values for dense layers
    def passThroughNeurons(self):
        curr_dense = self.image.copy()
        for L_i in range(len(self.layers)):
            curr_dense = self.layers[L_i](curr_dense)
            print(f"L_i is {L_i} AND ...")
            self.denseNeurons[f"layer_{L_i}"] = curr_dense.numpy()
     
    #there are only five possible permutations for value returns
    #find if there is a way to get different weights/biases when putting an image
    def revprop(self, answer, currLay, Q):
        if currLay==self.endLay-1+1:
            #not sure what to return for base case
            self.resImage[answer] += 1
            return 0
            
        if currLay in self.ignoreLays: 
            self.revprop(answer, currLay-1, Q)
            return 0 #BUG FIXED
        
        highestVals = {}
        print(answer, "--->", currLay)
        neuronVal = self.denseNeurons[f"layer_{currLay}"][0][answer]
        weights = self.layers[currLay].weights[0][:, answer]
        bias = self.layers[currLay].weights[1].numpy()[answer]
        for i, w in enumerate(weights.numpy()):
            connectionVal = neuronVal*w + bias + np.random.rand()/1000
            highestVals[connectionVal] = i
            
        #sort by weights
        valOrder = sorted(highestVals, reverse=True)
        #print(valOrder)
        for A in range(Q):
            vkey = valOrder[A]
            #print(vkey, "---", highestVals[vkey], "---", currLay)
            self.revprop(highestVals[vkey], currLay-1, int(Q/2))
            
            


