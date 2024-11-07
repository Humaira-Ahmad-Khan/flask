from app import app  # Importing app after it's been defined in app.py
from model.user_model import User_model
object = User_model()

@app.route('/user/signup')
def user_signup_controller():
    return object.user_signup_model()
    


@app.route('/home/birthday')
def humairi():
    return object.abubakar()

@app.route('/home/humaira')
def ayesha():
    return object.humaira()