'''
Created on 12 may. 2020

@author: Frodo
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2
from lib2to3.fixes import fix_imports2

# Error comun con cv2, si ponemos una ruto a un archivo que no existe, nos guarda un NoeType
# Le pasamos la ruta absoluta del archivo, imagen, jpeg, png
img=cv2.imread(r"C:\Users\Frodo\Downloads\mascarilla.jpg")
print(type(img)) # Como vemos ya nos transforma la imagen en un array
print(img.shape)
print(img)
plt.imshow(img)
plt.show()

# OPENCV ----> Lee la imagen como BLUE GREEN RED y MATPLOTLIB lo muestra como una imagen RED GREEN BLUE, asi que los colores azul y rojo se intercambian
# Para transformarlo a RGB
img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

# leer una imagen en escala de grises
img_gray = cv2.imread(r"C:\Users\Frodo\Downloads\mascarilla.jpg",cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)
plt.imshow(img_gray,cmap='gray')
plt.show()

# Redimensionar el tamanhoo de las imagenes
fix_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
plt.show()

print(fix_img.shape)
nueva_img=cv2.resize(fix_img,(1000,400))

# reducir por un porcentaje (50%)
w_ratio=0.8
h_ratio=0.1
nueva_img=cv2.resize(fix_img,(0,0),fix_img,w_ratio,h_ratio)
plt.imshow(nueva_img)
plt.show()

# para rotar imagenes, (img,[0,1,-1])
nueva_img = cv2.flip(fix_img,0)
plt.imshow(nueva_img)
plt.show()
# guardar una imagen
cv2.imwrite(r"C:\Users\Frodo\Downloads\new_img.jpg",nueva_img) # devuelve True si lo hizo

