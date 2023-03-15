from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')

#inherited imports
import c3bo

#extra imports
from datetime import datetime




""" Stuff Left:
* connect CSS file to this...
* inherit from deep neural net class to do stuff!

"""

@app.route('/')
def index():
   currTime = datetime.now()
   then = datetime(2020, 12, 28, 20, 8, 15) 
   now  = datetime.now() 
   currTime = now - then
   #remember below offers *args
   return render_template("home.html", days=currTime.days)

@app.route('/hospital/')
def virtual_hospital():
   model = c3bo.useModel(jpath="C:\\Users\\leode\\isef_2022-23\\model2.json",
                      jweights="C:\\Users\\leode\\isef_2022-23\\model2.h5")
   return render_template("hospital.html", model=model)


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