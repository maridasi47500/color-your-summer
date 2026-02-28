from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>share sporty photos and add dynamic text styling &#127946; &#x1F60E; &#128095;</p>"
