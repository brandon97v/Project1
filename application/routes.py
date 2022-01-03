from application import app, db

@app.route('/')
def home ():
    return "This is the homepage"

