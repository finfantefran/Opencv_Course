'''
Created on 12 may. 2020

@author: Frodo
'''

import cv2
import numpyejemplos as np
import matplotlib.pyplot as plt



# funcion a la que le pasamos cordenadas del mouse. el evento que hizo, parametros adicionales
def dibujar_Circulo(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)


cv2.namedWindow(winname='mi_dibujo')
cv2.setMouseCallback('mi_dibujo', dibujar_Circulo)

img = np.zeros(shape=(512, 512, 3), dtype=np.int8)

while True:
    cv2.imshow('mi_dibujo', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
