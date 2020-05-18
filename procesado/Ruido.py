'''
Created on 14 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


def cargar_immg():
    img = cv2.imread(r'C:\Users\Frodo\eclipse-workspace\DATA\bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def mostrar(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()

'''
Aplicar gamma filtro: GAMMA FILTER
Hacer que una imagen aparezca mas o menos oscura o brillante dependiendo del valor de Gamma

'''
i = cargar_immg()
mostrar(i)
gamma = 15
img_gamma = np.power(i, gamma)
mostrar(img_gamma)

''' BLUR: desenfoque para detectar mejor formas:
--> filter2D(img,-1,kernelsize) : Convolucion 2D
'''

img = cargar_immg()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=3)
mostrar(img)
print(img)

# Crear kernel para el filtro, matriz 5x5 con valorres de 1/25

kernel = np.ones(shape=(5, 5), dtype=np.float32) / 20
print(kernel)
dst = cv2.filter2D(img, -1, kernel)
mostrar(dst)

'''
--> Blur kernel por defecto
'''
img = cargar_immg()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=3)
mostrar(img)

blurred=cv2.blur(img,ksize=(5,5))
mostrar(blurred)


'''
--> GaussianBlur y medianBlur: Coge un grupo de pixeles, calculan su promedio y sacan un valor
medianBlur(img,ksize(1)))
GaussianBlur(img, kernelsize,desviacion(valor entero))
'''
img = cargar_immg()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=3)


gaussian=cv2.GaussianBlur(img,(5,5),10)
mostrar(gaussian)

'''El mejor para reducir imagen y mantener detalles en la imagen, y sobre todo contornos'''
median= cv2.medianBlur(img,ksize=(5))
mostrar(median)


'''EMJEMPLO DE REDUCIR RUIDO'''
img = cv2.imread(r'C:\Users\Frodo\eclipse-workspace\DATA\sammy_face.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mostrar(img)

noise_img=cv2.imread(r'C:\Users\Frodo\eclipse-workspace\DATA\sammy_noise.jpg')
noise_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2RGB)
mostrar(noise_img)

median= cv2.medianBlur(noise_img,ksize=(3))
mostrar(median)

