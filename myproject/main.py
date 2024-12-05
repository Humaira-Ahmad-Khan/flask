from flask import Flask , render_template
app=Flask(__name__)

@app.route('/')
def index():
    return "This is pyth"

@app.route('/home')
def home():
    return "This is pyth"

@app.route('/about/<float:name>')
def about(name):
    return (f"This is pyth{name}")


if __name__=='__main__':
    app.run(debug=True)