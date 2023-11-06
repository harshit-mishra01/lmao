
from flask import Flask , render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
   # return 'HELLO WORLD!'
   return render_template('index.html')
   

@app.route('/index.html')


def login():
    return render_template('index.html')

@app.route('/lmao.html')
def lmaos():
    return 'LMAO DAWG'

@app.route('/myprofile.html')
def profile():
    return render_template('myprofile.html')

@app.route('/')
def back():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True , port=3000)