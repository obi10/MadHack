import numpy as np
import cv2

#this is the cascade we just made. Call what you want
lego_cascade = cv2.CascadeClassifier('data/cascade.xml')

cap = cv2.VideoCapture(2)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    legos = lego_cascade.detectMultiScale(gray, 50, 50)
    
    for (x,y,w,h) in legos:
        cv2.rectangle(img, (x, y), (x+w, y+h),(255,255,0),2)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img,'Watch',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()