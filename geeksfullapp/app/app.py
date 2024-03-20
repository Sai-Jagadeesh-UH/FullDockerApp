from flask import Flask, render_template
# creating Flask Obj reference
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
