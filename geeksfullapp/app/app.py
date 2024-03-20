from flask import Flask
import os
# creating Flask Obj reference
app = Flask(__name__)


@app.route('/')
def index():
    return str(os.getcwd())+" Hai"


if __name__ == '__main__':
    app.run()
