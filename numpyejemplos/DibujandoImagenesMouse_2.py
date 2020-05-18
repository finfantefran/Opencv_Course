'''
Created on 12 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt



''' FUNCION a la que le pasamos cordenadas del mouse. el evento que hizo, parametros adicionales'''
def dibujar_Circulo(event, x, y, flags, param):

    
    if event == cv2.EVENT_LBUTTONDOWN:
        '''CLICK BTN IZQUIERDO'''
        cv2.circle(img, (x, y), 50, (0, 0, 255), -1)
    
    
    elif event == cv2.EVENT_RBUTTONDOWN: 
        '''CLICK BTN DERECHO'''
        cv2.circle(img, (x, y), 50, (0, 255, 0), -1)
        
        


''''''
cv2.namedWindow(winname='mi_dibujo')
'''La funcion le da automaticamente a mi funcion dibujar_Circulo el parametro de coordenadas y el evento click'''
cv2.setMouseCallback('mi_dibujo', dibujar_Circulo)

img = np.zeros(shape=(512, 512, 3))

while True:
    cv2.imshow('mi_dibujo', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
