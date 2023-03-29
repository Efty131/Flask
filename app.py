from flask import Flask

app = Flask(__name__)
app.debug = True # for auto reloading. Server host korar somoy eta false korte hobe.

@app.route("/")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "This is about page"

if __name__ == "__main__":
    app.run()