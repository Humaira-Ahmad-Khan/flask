from app import app  # Importing app after it's been defined in app.py

@app.route('/product/add')
def add():
    return "the product page is given"
