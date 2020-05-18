'''
Created on 14 may. 2020

@author: Frodo
'''
from cv2.cv2 import THRESH_BINARY

"""
Un metodo para segmentar una imagen en diferentes partes, y consiste en 2 valores, blanco y negro.
Convetimos una imagen a color en binario, escala de grises, obtenemos mas informacion.
Pero obtenemos los datos con mucha menos informacion, con valores de 0 o 255
"""
import cv2
import matplotlib.pyplot as plt
import os

# para leer en escala de grises una imagen, anhadimos un cero(img, 0)
img=cv2.imread(r"C:\Users\Frodo\Downloads\mascarilla.jpg",0)
plt.imshow(img, cmap='gray')
plt.show()


# threshold, parametros: el threshold, valor minimo
# maxval que se aplica de forma que cualquier valor por debajo se vuelve 0 y cualquiera por encima 255
# tipo de threshold

# Si el valor del pixel >threshold 127 --> maxval  y pixel < threshold --> 0
ret, thresh1= cv2.threshold(img,255,255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap='gray')
plt.show()

# Si el valor del pixel >threshold 127 --> 0  y pixel < threshold --> maxval
ret, thresh1= cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
plt.imshow(thresh1, cmap='gray')
plt.show()
# Si el valor del pixel >threshold 127 --> threshold  y pixel < threshold --> actual valor
ret, thresh1= cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
plt.imshow(thresh1, cmap='gray')

# Si el valor del pixel > threshold 127 --> valor actual  y pixel < threshold --> 0
ret, thresh1= cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
plt.imshow(thresh1, cmap='gray')
plt.show()
# Si el valor del pixel >threshold 127 --> 0  y pixel < threshold --> valor actual
ret, thresh1= cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
plt.imshow(thresh1, cmap='gray')
plt.show()

