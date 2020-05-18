'''
Created on 13 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


'''LEER IMAGENES 2RGB'''
img2 = cv2.imread(r"C:\Users\Frodo\eclipse-workspace\DATA\watermark_no_copy.png")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img1 = cv2.imread(r"C:\Users\Frodo\eclipse-workspace\DATA\dog_backpack.png")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

'''REDIMENSIONAR IMAGEN 2'''
img2 = cv2.resize(img2, (600, 600))
plt.imshow(img2)
plt.show()
print(img2.shape)
'''REDIMENSIONAR IMAGEN 1'''
img1 = cv2.resize(img1, (934, 1401))
plt.imshow(img1)
plt.show()
print(img1.shape)

'''PUNTOS DE REFERENCIA PARA HACER UN RECORTE '''
x_offset = 934 - 600
y_offset = 1401 - 600

rows, cols, channels = img2.shape

''' RECORTAR UNA IMAGEN A PARTIR DE 2 PUNTOS:
Cogemos desde la coordenada y_offset hasta el alto total de la imagen, 
y desde la coordenada x_offset hasta el ancho total
'''
roi = img1[y_offset:1401, x_offset:943]
plt.imshow(roi)
plt.show()

'''APLICAR UNA MASCARA nos permito solo recoger la parte del color que queramos de la copia/imagen:
Pasamos la imagen a escala de grises.
'''

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
plt.imshow(img2gray, cmap='gray')
plt.show()
print(img2gray.shape)

'''INVERSA de la imagen, todo lo que es blanco a negro y viceversa:
bitwise_not: 
'''
mask_inv = cv2.bitwise_not(img2gray)
plt.imshow(mask_inv, cmap='gray')
plt.show()

'''CREAR UNA IMAGEN BLANCA con la forma de la imagen2, fondo blanco:
Aplicamos bitwise_or: Aplica la imagen blanca a  la mascaraq
'''

white_background = np.full(img2.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)
plt.imshow(bk)
plt.show()


'''Aplicamos la imagen original con el texto en rojo a la mascara y queda en rojo'''
fg = cv2.bitwise_or(img2, img2, mask=mask_inv)
plt.imshow(fg)
plt.show()
print(fg.shape)



final_roi=cv2.bitwise_or(roi,bk)
plt.imshow(final_roi)
plt.show()

