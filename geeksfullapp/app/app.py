from flask import Flask, render_template
# creating Flask Obj reference
app = Flask(__name__)


@app.route('/')
def homepage():
    return "hai Loging in"


@app.route('/<name>')
def index(name):
    if name == "sai":
        return "Hai Hero, %d!!" % name
    return f"Hello my guest {name}"


if __name__ == '__main__':
    app.run()
