from app import app  # Importing app after it's been defined in app.py

@app.route('/user/buy')
def buy():
    return "This is for students"
