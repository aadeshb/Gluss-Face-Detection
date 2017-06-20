from flask import Flask, render_template
# from facedetect import center

import numpy
import cv2
import matplotlib


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

center = int(input())

app = Flask(__name__, static_folder='script',  template_folder='templates')
@app.route('/')
@app.route('/index')
def index():
def getFace:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print faces;
#    for (x,y,w,h) in faces:
#        center = x+(w/2)
#        print "this is x: %d" % center
    face = faces[0]
    center = face.x+(face.w/2)
    print "this is x: %d" % center    
    return render_template('index.html', center=center)
@app.route('/three.js')
def three():
    return render_template('three.js')



if __name__ == "__main__":
    app.run(debug=True)
    

