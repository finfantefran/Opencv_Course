'''
Created on 12 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''CREAR UNA IMAGEN NEGRA'''
blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)  # imagen en principio negro puro, toda la matriz es de 0s
print(blank_img.shape)
plt.imshow(blank_img)
plt.show()

''' DIBUJAR UN RECTANGULO en la imagen, le damos la coordenada de dos puntos, que son tuplas'''
cv2.rectangle(blank_img, pt1=(384, 10), pt2=(495, 150), color=(0, 255, 0),thickness=10)
print(blank_img)
plt.imshow(blank_img)
plt.show()

'''los dos puntos que definimos son el inferior izquierdo y el superior derecho'''
cv2.rectangle(blank_img, pt1=(200, 200), pt2=(300, 300), color=(0, 0, 255),thickness=10)
plt.imshow(blank_img)
plt.show()

''' DIBUJAR UN CIRCULO, line, circle 
thickness=-1 significa que es un circulo relleno, no solo la circunferencia
'''
cv2.circle(img=blank_img,center=(100,100),radius=50,color=(255,0,0),thickness=-1)
plt.imshow(blank_img)
plt.show()

'''DIBUJAR UNA LINEA'''
cv2.line(img=blank_img,pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=5)
plt.imshow(blank_img)
plt.show()

'''ESCRIBIR TEXTO EM UNA IMAGEN'''
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(blank_img,text='HOLA MUNDO', org=(10,500), fontFace=font, fontScale=1,color=(255,255,255))
plt.imshow(blank_img)
plt.show()

'''DIBUJAR UN POLIGONO'''
blank_img2=blank_img.copy()
vertices=np.array([[100,300],[200,200],[400,300],[200,400]],dtype=np.int32 )
# Hya que redimensionar los vertices a 3 dimensiones
puntos=vertices.reshape((-1,1,2))
polygon=cv2.polylines(blank_img2,[puntos],isClosed=True,color=(255,0,0), thickness=5)
plt.imshow(polygon)
plt.show()










