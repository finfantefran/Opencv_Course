'''
Created on 12 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''LEER IMAGEN'''
img=cv2.imread(r"C:\Users\Frodo\eclipse-workspace\DATA\00-puppy.jpg")
plt.imshow(img)
plt.show()

'''BGR 2 RGB'''
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

'''RGB 2 HSV'''
img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
plt.imshow(img)
plt.show()

'''BGR 2 GRAY '''
img=cv2.imread(r"C:\Users\Frodo\eclipse-workspace\DATA\00-puppy.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img, cmap='gray')
plt.show()