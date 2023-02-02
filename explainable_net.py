
from sklearn.externals import joblib
from keras.models import Sequential, model_from_json

class ML_Model:

    def __init__(self, name):
        self.name = name
        self.algorithm = None
    
    def NeuralNet(self, jsonName, h5Name):
        try:
            json_file = open(jsonName, 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            loaded_model.load_weights(h5Name)
        except FileNotFoundError as FE:
            print("Could not find one of the files...")
            print(FE)
        except Exception as e:
            print(type(e))
        else:
            print("Loaded model from disk")
            algorithm = loaded_model
        
    def NearestNeighbors(self, clfFile):
        #below extension must be .pkl for loading
        modelscorev2 = joblib.load('.pkl' , mmap_mode ='r')
        algorithm = modelscorev2 #should be able to do algorithm.predict_proba(<data>)
    

class Ensemble(ML_Model):

    def __init__(self, n_estimators):
        self.n_estimators = n_estimators
        self.models = list()
        self.avg_acc = 0

    def addModel(self, newModel):
        assert type(newModel) == ML_Model
        self.models.append(newModel)
        print("Just added this model:", newModel.name)

    def predict(self, group="all"):
        if group != "all": pass
        consensus = dict()
        for MODEL in self.models:
            algorithm = MODEL.algorithm
            #should be able to simply .predict(<data>)
            pred_class = algorithm.predict()
            if pred_class not in algorithm.keys(): algorithm[pred_class] = 1
            algorithm[pred_class] += 1
        print("The ensemble predicts", consensus)

