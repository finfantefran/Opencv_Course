'''
Created on 12 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)  # imagen en principio negro puro, toda la matriz es de 0s
print(blank_img.shape)

plt.imshow(blank_img)
plt.show()

# Dibujar un rectangulo en la imagen, le damos la coordenada de dos puntos, que son tuplas
cv2.rectangle(blank_img, pt1=(384, 10), pt2=(495, 150), color=(0, 255, 0),thickness=10)
print(blank_img)
plt.imshow(blank_img)
plt.show()

# los dos puntos que definimos son el inferior izquierdo y el superior derecho
cv2.rectangle(blank_img, pt1=(200, 200), pt2=(300, 300), color=(0, 0, 255),thickness=10)
plt.imshow(blank_img)
plt.show()

# podemos dibujar, line, circle (circulo relleno thickness -1)

# escribir sobre una imagen
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(blank_img,text='HOLA MUNDO', org=(10,500), fontFace=font, fontScale=1,color=(255,255,255))
plt.imshow(blank_img)
plt.show()