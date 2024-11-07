from app import app  # Importing app after it's been defined in app.py

@app.route('/ECAT/test')
def ECAT():
    return "This is for students who want to join the IT universities"
