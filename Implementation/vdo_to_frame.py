#import numpy as np
import cv2

cap = cv2.VideoCapture('Write_jigyasa.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    face_cascade = cv2.CascadeClassifier('data/haarcascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('data/haarcascade/haarcascade_eye.xml')
    img = frame
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    The detection works only on grayscale images. So it is important to convert the color image to grayscale. (line 8)
#    detectMultiScale function (line 10) is used to detect the faces. It takes 3 arguments — the input image, scaleFactor and minNeighbours. scaleFactor specifies how much the image size is reduced with each scale. minNeighbours specifies how many neighbors each candidate rectangle should have to retain it. You can read about it in detail here. You may have to tweak these values to get the best results.
#    faces contains a list of coordinates for the rectangular regions where faces were found. We use these coordinates to draw the rectangles in our image.
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()