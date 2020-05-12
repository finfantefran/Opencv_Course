'''
Created on 12 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\Frodo\Downloads\mascarilla.jpg")
plt.imshow(img)
plt.show()

# pasar a RGB
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

# pasar a HSV
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
plt.imshow(img)
plt.show()