# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:09:51 2022

@author: omarl
"""

import cv2 as c
import numpy as np
from matplotlib import pyplot as plt



def HistogramSegmentation(name,umbral):
    imagen = c.imread(name,0)
    hist = c.calcHist([imagen],[0],None,[256],[0,256])
    plt.plot(hist,color="b")
    altura,anchura = imagen.shape
    aux = np.zeros((altura,anchura,1))
    for y in range(altura):
        for x in range(anchura):
            if(imagen[y,x] >= umbral):
                aux[y,x] = 255
    plt.savefig('img/segmentacion/histograma/histograma.jpg')
    c.imwrite('img/segmentacion/histograma/10.png', aux)
    plt.show()
    c.imshow('img',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
'''def SegmenationBords(name):
    imagen = c.imread(name,0)
    img = c.Canny(imagen,100,200) 
    c.imwrite('../img/segmentacion/Bordes/deteccion.jpg',img)'''


#SegmenationBords('../img/test.jpg')

def TransHough(name):
    imagen = c.imread(name,0)
    altura,anchura = imagen.shape
    imagen = c.blur(imagen,(9,9))
    circulos = c.HoughCircles(imagen, c.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)
    if circulos is not None:
        circulos=np.uint16(np.around(circulos))
        for pt in circulos[0,:]:
            a,b,r = pt[0],pt[1],pt[2]
            c.circle(imagen,(a,b),r,255,-1)
    for y in range(altura):
        for x in range(anchura):
            if imagen[y,x] != 255:
                imagen[y,x] = 0
    c.imwrite('img/segmentacion/transformada/transf.jpg',imagen)
    c.imshow('img',imagen)
    c.waitKey(0)
    c.destroyAllWindows()
    




