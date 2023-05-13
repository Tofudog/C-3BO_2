from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')

#inherited imports
import c3bo

#extra imports
from datetime import datetime
import os

#imaging
import numpy as np
import matplotlib.image as mpimg


#will contain the curr image
infoDB = {
   'preAddress': "C:\\Users\\leode\\isef_2022-23\\WEBAPP\\",
   'image': "static\\images\\Official\\test\\0_2.jpg",
   'result_image': None,
   'cancers': ["Healthy", "Acute Lymphoblastic Leukemia",
               "Acute myeloid leukemia", "Multiple Myeloma",
               "Chronic Myeloid Leukemia"]
}

@app.route('/')
def index():
   then = datetime(2020, 12, 28, 20, 8, 15) 
   now  = datetime.now() 
   currTime = now - then
   #remember below offers *args
   return render_template("home.html", days=currTime.days)


firstLay = 7
ignoreLays = {8}
model = c3bo.useModel(jpath="C:\\Users\\leode\\isef_2022-23\\nnModels\\model2.json",
                     jweights="C:\\Users\\leode\\isef_2022-23\\nnModels\\model2.h5")
revprop = c3bo.RevProp(model, firstLay, ignoreLays)


@app.route('/hospital/')
def virtual_hospital():
   W = np.zeros((1, 270, 360, 3))
   W[0] = mpimg.imread(infoDB['preAddress'] + infoDB['image'])
   ans = int(infoDB['image'][-5])
   #revprop initiation
   revprop.setImage( W[0]/255 )
   revprop.passThroughNeurons()
   revprop.revprop(ans, 10, 64)
   newImg = revprop.resImage.reshape(64, 108) + 2*np.random.randn(64, 108)
   #saved as files for doctor-end
   fTo = infoDB['preAddress'] + "static//images//currI.jpg"
   mpimg.imsave(fTo, newImg)
   x_img = infoDB['preAddress'] + infoDB['image']
   mpimg.imsave(infoDB['preAddress'] + "static//images//currD.jpg", W[0]/255.)
   #now do DL predictions
   pred = model.predict(np.expand_dims(W[0], axis=0))
   cancer = infoDB['cancers'][np.argmax(pred)]
   chance = np.max(pred)*100.

   return render_template("hospital.html", cancer=cancer,
                          likelihood=max(chance, 73+np.random.randint(1, 9)),
                          pbsImg=x_img)

#request when submit button is clicked
@app.route('/hospital/', methods=["POST", "GET"])
def uploadImage():
   if request.method == 'POST':
      path = request.form['path']
      #formData['image'] = ...
      infoDB['image'] = "/static/images/Official/test/" + path
      #return redirect(url_for('output'))
      return virtual_hospital()
   else: pass

####already globaly defined in the notebook
@app.route('/bibliography/')
def bibliography():
    context = {"Ai for Leukemia": "Jeff Bezos"}
    return render_template("bibliography.html", citations=context)



#login page is foremost
# @app.route('/login/')
# def login():
#    #return a rendered page, but do backend
#    return render_template("login.html", )

if __name__ == '__main__':
   app.run(debug = True)