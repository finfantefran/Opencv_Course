'''
Created on 12 may. 2020

@author: Frodo
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2
from lib2to3.fixes import fix_imports2

''' Error comun con cv2, si ponemos una ruto a un archivo que no existe, nos guarda un NoeType
Le pasamos la ruta absoluta del archivo, imagen, jpeg, png
'''

'''LEER IMAGEN'''
img=cv2.imread(r"C:\Users\Frodo\eclipse-workspace\DATA\00-puppy.jpg")
print(type(img)) # Como vemos ya nos transforma la imagen en un array
print(img.shape)
print(img)
plt.imshow(img)
plt.show()

''' REDIMENSIONAR UNA IMAGEN'''
porcentaje=img.shape[0]*100/img.shape[1]
print(porcentaje)
vfinal=int(porcentaje*200/100)
print(vfinal)
nueva_img=cv2.resize(img,(vfinal,150))
plt.imshow(nueva_img)
plt.show()


''' OPENCV ----> Lee la imagen como BLUE GREEN RED y MATPLOTLIB lo muestra como una imagen RED GREEN BLUE, asi que los colores azul y rojo se intercambian
# Para transformarlo a RGB'''
img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

''' LEER UNA IMAGENE EN ESCALA DE GRISES'''
img_gray = cv2.imread(r"C:\Users\Frodo\eclipse-workspace\DATA\00-puppy.jpg",cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)
cv2.imwrite(r"C:\Users\Frodo\Downloads\pquppy_gray.jpg",img_gray) 
plt.imshow(img_gray,cmap='gray') # cmap='gray' para visualizarla como escala de grises
plt.show()

''' CONVERTIR BGR 2 RGB'''
fix_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
plt.show()

''' REDIMENSIONAR EL TAMAÑO DE IMAGENES'''
print(fix_img.shape)
nueva_img=cv2.resize(fix_img,(1000,400))

'''REDIMENSIONAR por un porcentaje (50%)'''
w_ratio=0.8
h_ratio=0.1
nueva_img=cv2.resize(fix_img,(0,0),fix_img,h_ratio,w_ratio)
plt.imshow(nueva_img)
plt.show()

''' ROTAS imagenes, (img,[0,1,-1])'''
nueva_img = cv2.flip(fix_img,0)
plt.imshow(nueva_img)
plt.show()
# guardar una imagen
cv2.imwrite(r"C:\Users\Frodo\Downloads\new_img.jpg",nueva_img) # devuelve True si lo hizo

