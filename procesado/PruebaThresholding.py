'''
Created on 14 may. 2020

@author: Frodo
'''

import cv2
import matplotlib.pyplot as plt
from cv2.cv2 import ADAPTIVE_THRESH_MEAN_C

img2 = cv2.imread(r"C:\Users\Frodo\Downloads\periodico.jpg", 0)
plt.imshow(img2, cmap='gray')
plt.show()

# ampliamos la imagen un poco
def aumentar_img(img2):
    '''
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    '''
    plt.imshow(img2, cmap='gray')
    plt.show()


ret, thresh1= cv2.threshold(img2,125,255,cv2.THRESH_BINARY)
aumentar_img(thresh1)

ret, thresh1= cv2.threshold(img2,125,255,cv2.THRESH_BINARY_INV)
aumentar_img(thresh1)

ret, thresh1= cv2.threshold(img2,125,255,cv2.THRESH_BINARY)
aumentar_img(thresh1)

'''
# THREHOLDING ADAPTIVE

imagen
valor maximo
meqtodo adaptativo
tipo de threhold
blocksize, tamanhoo del pixel vecino para calcular el threshold  (3,5,7,11)
valor de C, 8
'''


thresh2= cv2.adaptiveThreshold(img2,255,ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,11)
aumentar_img(thresh2)



'''
Juntar varios threshold
'''
blended = cv2.addWeighted(src1=thresh1,alpha=0.6,src2=thresh2,beta=0.4,gamma=0)
aumentar_img(blended)