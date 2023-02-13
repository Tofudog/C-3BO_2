
from sklearn.externals import joblib
from keras.models import Sequential, model_from_json

class ML_Model:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
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
        
    #includes KNN, Logistic Regression, Decision Trees, etc...
    def SklearnModel(self, clfFile):
        #below extension must be .pkl for loading
        modelscorev2 = joblib.load(clfFile , mmap_mode ='r')
        algorithm = modelscorev2 #should be able to do algorithm.predict_proba(<data>)
    
    def __str__(self): return self.name + " is a " + self.kind + " ML algorithm"
    

class Ensemble(ML_Model):

    def __init__(self, n_estimators, *ml_models):
        self.n_estimators = n_estimators
        self.models = ml_models
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

cnn1 =  ML_Model("CNN_1", "Convolutional Neural Network")
cnn1.NeuralNet("model.json", "model.h5")
#knn1 = ML_Model("KNN_1", "K-Nearest Neighbors")
voting_clf = Ensemble(n_estimators=2, cnn1)
vote_pred = voting_clf.predict()

#given that the ensemble has made an accurate prediction
def patchImage(image, clf, window_size=(3,3)):
    pred_score = clf.predict(image) #should output five distinct float values
    patch_scores = np.ones((image.nrows, image.ncols))
    idx = np.argmax(pred_scores)
    row_end, col_end = window_size
    while row_end < image.shape[0]:
        while col_end < image.shape[1]:
            #the patch is applied to coordinates with row_end and col_end

            col_end += window_size[0]
        col_end = window_size[0]
        row_end += window_size[1]
    
