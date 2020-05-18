'''
Created on 16 may. 2020

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


def mostrar_img(img):
    plt.imshow(img)
    plt.show()
    print(img1.shape)

    
def redimensionar_img(img, x, y):
    img = cv2.resize(img, (x, y))
    return img


#mostrar_img(img2)
#mostrar_img(img1)

'''REDIMENSIONAR AL MISMO TAMANHO'''
img1 = redimensionar_img(img1, 1200, 1200)
img2 = redimensionar_img(img2, 1200, 1200)
#mostrar_img(img1)
#mostrar_img(img2)

'''JUNTAR DOS IMAGENES:
alpha y beta das más o menos brillo a una imagen sobre otra.
'''

nueva_img = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
mostrar_img(nueva_img)