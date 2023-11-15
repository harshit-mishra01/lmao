
from flask import Flask , render_template

#initializing apps
app = Flask(__name__)

#creating routes
@app.route('/')
def home():
   return render_template('index_0.html')
   
@app.route('/login')
def login():
    return render_template('index_1.html')

@app.route('/lmao')
def lmaos():
    return render_template('lmao.html')

@app.route('/myprofile')
def profile():
    return render_template('myprofile.html')




if __name__ == "__main__":
    app.run(debug=True , port=3000)