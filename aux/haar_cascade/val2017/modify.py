import cv2
import numpy as np
import os
#from pathlib import Path
from glob import glob

def resize_images():
    pic_num = 1
            
    #for filename in Path('val2017').rglob('*091.jpg'):
    for filename in glob('*.jpg'):
        try:
            print(filename, "hola")
            #''.join()
            #print(filename_concatenated)
            img = cv2.imread(filename ,cv2.IMREAD_GRAYSCALE)
            #img = cv2.imread(filename)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("../neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))

'''
def resize_images():
    try:
        img = cv2.imread("val2017/000000000139.jpg" ,cv2.IMREAD_GRAYSCALE)
        #img = cv2.imread(filename)
        # should be larger than samples / pos pic (so we can place our image on it)
        resized_image = cv2.resize(img, (100, 100))
        cv2.imwrite("neg/"+str(1)+".jpg",resized_image)
        
    except Exception as e:
        print(str(e))
'''

resize_images()
