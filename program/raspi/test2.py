from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division

import numpy as np
import cv2

import time
#import gopigo3

import requests
from pprint import pprint

#this is the cascade we just made. Call what you want
#lego_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

#GPG = gopigo3.GoPiGo3() # Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.


cont = 0 #repeticiones
aux = 0 #

try:
    '''
    while True:

        #opencv
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        legos = lego_cascade.detectMultiScale(gray, 1.3, 5)

        #powering engines
        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 80) #forward



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
    '''

    #resp = requests.get('http://localhost:5000/devices')

    device = {"identifier": "smartphone_id", "name": "cellphone", "device_type": "electro", "controller_gateway": "192.168.0.12"}
    resp = requests.post('http://localhost:5000/devices', json=device)
    
    if resp.status_code != 200:
        print("API Error")

    else:
        pprint(resp.json())


except KeyboardInterrupt:
    #GPG.reset_all() # Unconfigure the sensors, disable the motors, and restore the LED to the control of the GoPiGo3 firmware.
    cap.release()
    cv2.destroyAllWindows()