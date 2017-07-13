import flask
app = flask.Flask(__name__)

@app.route("/")

def index():
    #do whatevr here...
    example.maine()
    return "Hello Heruko"

