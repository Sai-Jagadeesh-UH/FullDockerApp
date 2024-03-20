from flask import Flask

# creating Flask Obj reference
app = Flask(__name__)


@app.route('/')
def index():
    return "Hai Mr.Jagadeesh"


if __name__ == '__main__':
    app.run()
