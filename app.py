# importing required modules
import os
from flask import Flask


# initialize the Flask app
app = Flask(__name__)

# application route
@app.route('/')
def index():
    return "Starter Page"


if __name__ == "__main__":

    app.run(debug=True)