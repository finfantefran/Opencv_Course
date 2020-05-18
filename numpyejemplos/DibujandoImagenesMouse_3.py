'''
Created on 16 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


'''VARIABLES'''
dibujo = False  # si el raton se presiona y mientras este presionado sera True 
ix = -1
iy = -1
i2x2 = -1
iy2 = -1
        
        
'''FUNCION'''


def dibujar_Rectangulo(event, x, y, flags, param):
    
    global ix,iy,ix2,iy2,dibujo
    
    if event == cv2.EVENT_LBUTTONDOWN:
        dibujo=True
        ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujo==True:
            ix2,iy2=x,y
            #cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0),thickness=10)
    
    elif event == cv2.EVENT_LBUTTONUP:
        dibujo=False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(ix2, iy2), color=(0, 255, 0),thickness=2)
                
        
'''CREAR IMAGEN'''

img = np.zeros(shape=(512, 512, 3))
cv2.namedWindow(winname='mi_dibujo')
cv2.setMouseCallback('mi_dibujo', dibujar_Rectangulo)

while True:
    cv2.imshow('mi_dibujo', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
