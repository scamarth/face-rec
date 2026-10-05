import cv2
import numpy
import sys,os

me = "me"
hhar_file = r"C:\Users\User\OneDrive\Desktop\Open CV with Python\facial reconition\haarcascade_frontalface_default.xml"
datasets = "datasets"
sub_data = "samarth"
path = os.path.join(datasets,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width,height) = (130,100)
face_cascade = cv2.CascadeClassifier(hhar_file)
webcam = cv2.VideoCapture(0)
count = 1
while count < 30:
    (ret,im) = webcam.read()
    grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w, y+h), (255, 69, 0,), 2)
        me = grey[y:y+h, x:x+w]
        face_resize = cv2.resize(me,(width,height))
        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
        count+= 1
    cv2.imshow("opencv",im)
    key = cv2.waitKey(10)
    if key == 27:
        break 
    