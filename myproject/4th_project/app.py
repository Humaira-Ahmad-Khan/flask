from flask import Flask, render_template
app = Flask(__name__)
from app import app
from model.user_model import Ctn
obj = Ctn()
@app.route('/home')

def home():
   return obj.humaira()





@app.route('/about')

def lala():
   return obj.ayesha()




if __name__ == "__main__" :
   app.run(debug =True)
   