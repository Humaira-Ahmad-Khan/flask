from flask import Flask

app = Flask(__name__)

# Import user_controller after creating the app object to avoid circular imports


@app.route('/')
def index():
    return "This is HTML"

from controller import product_controller,user_controller,buy_controller,ECAT_controller
if __name__ == "__main__":
    app.run(debug=True)
