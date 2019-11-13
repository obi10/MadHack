import numpy as np
import cv2
import time

#this is the cascade we just made. Call what you want
lego_cascade = cv2.CascadeClassifier('data/cascade.xml')

cap = cv2.VideoCapture(0)
#time.sleep(2) #estabilizar la camara

cont = 0 #repeticiones
aux = 0 #

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    legos = lego_cascade.detectMultiScale(gray, 1.3, 5)
    #print(len(legos))

    #if (primera iteracion) aux = len(legos) #lo que en realidad se deberia hacer (uso de una variable extra "i")

    for (x,y,w,h) in legos: #entra al for cuando detecta el lego
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

    #logica para estar seguros de enviar la informacion (detectar tres repeticiones del mismo numero)
    if len(legos) == aux:
        cont += 1
    else:
        cont = 0

    aux = len(legos) #se actualiza el valor auxiliar
    
    if cont == 3:
        print('se detectaron', aux, 'personas')
        cont = 0

    cv2.imshow('img',img) #mostrar el rectangulo que encierra el rostro del lego

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
