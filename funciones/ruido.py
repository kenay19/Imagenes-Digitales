# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:53:43 2022

@author: omarl
"""

import numpy as np
import cv2 as cv
import random

def Sal(name,option, porcentaje):
    imagen = cv.imread(name,option)
    imagenSalida = np.zeros(imagen.shape, np.uint8())
    thres = 1 - porcentaje
    
    for y in range (imagen.shape[0]):
        for x in range (imagen.shape[1]):
            rdn = random.random()
            
            if rdn < porcentaje:
                imagenSalida[y][x] = 255
            elif rdn > thres:
                imagenSalida[y][x] = 255
            else:
                imagenSalida[y][x] = imagen[y][x]
    cv.imwrite('img/ruido/Sal.jpg',imagenSalida)
    cv.imshow('Sal ',imagenSalida)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Pimienta(name,option, porcentaje):
    imagen = cv.imread(name,option)
    imagenSalida = np.zeros(imagen.shape, np.uint8())
    thres = 1 - porcentaje
    
    for y in range (imagen.shape[0]):
        for x in range (imagen.shape[1]):
            rdn = random.random()
            
            if rdn < porcentaje:
                imagenSalida[y][x] = 0
            elif rdn > thres:
                imagenSalida[y][x] = 0
            else:
                imagenSalida[y][x] = imagen[y][x]
    cv.imwrite('img/ruido/Pimienta.jpg',imagenSalida)
    cv.imshow('Pimienta ',imagenSalida)
    cv.waitKey(0)
    cv.destroyAllWindows()

def SalyPimienta(name,option, porcentaje):
    imagen = cv.imread(name,option)
    imagenSalida = np.zeros(imagen.shape, np.uint8())
    thres = 1 - porcentaje
    
    for y in range (imagen.shape[0]):
        for x in range (imagen.shape[1]):
            rdn = random.random()
            
            if rdn < porcentaje:
                imagenSalida[y][x] = 0
            elif rdn > thres:
                imagenSalida[y][x] = 255
            else:
                imagenSalida[y][x] = imagen[y][x]
    cv.imwrite('img/ruido/SalyPimienta.jpg',imagenSalida)
    cv.imshow('Sal y Pimienta',imagenSalida)
    cv.waitKey(0)
    cv.destroyAllWindows()