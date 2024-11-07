from flask import Flask
obj = Flask(__name__)
@app.route('/')
def ctn():
    return"This is my city."
if __name__ == "__main__":
    app.run(debug=True)