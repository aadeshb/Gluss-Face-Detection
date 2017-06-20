from flask import Flask, render_template
from facedetect import center

center = int(input())

app = Flask(__name__, static_folder='script',  template_folder='templates')
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', center=center)
@app.route('/three.js')
def three():
    return render_template('three.js')



if __name__ == "__main__":
    app.run(debug=True)
    

