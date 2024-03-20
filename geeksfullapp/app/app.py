from flask import Flask, render_template
import os
import sys
from utils import logging
# creating Flask Obj reference
app = Flask(__name__)


@app.route('/')
def index():
    logging.info(f'logging {os.getcwd()}')
    print("\nI am printing")
    print()
    return os.getcwd()


if __name__ == '__main__':
    index()
    app.run()
