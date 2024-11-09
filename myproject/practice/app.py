from flask import Flask

from  model.user_model import Tea

app = Flask(__name__)

obj=Tea()

@app.route('/about')

def about():
    return obj.humaira()


if __name__ == "__main__" :
   app.run(debug =True)
   