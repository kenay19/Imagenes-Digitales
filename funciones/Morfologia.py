# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:18:51 2022

@author: omarl
"""

import numpy as np
import cv2 as c


def erosion(name,option):
    img = c.imread(name,option)
    kernel = np.ones((5,5),np.uint8) 
    erosion = c.erode(img,kernel,iterations = 1)
    c.imwrite('img/Morfologia/erosion.jpg', erosion)
    c.imshow('erosion',erosion)
    c.waitKey(0)
    c.destroyAllWindows()
    
    
def dilatacion(name,option):
    img = c.imread(name,option) 
    kernel = np.ones((5,5),np.uint8) 
    dilata = c.dilate(img,kernel,iterations = 1)
    c.imwrite('img/Morfologia/dilatacion.jpg', dilata)
    c.imshow('dilatacion',dilata)
    c.waitKey(0)
    c.destroyAllWindows()
    
    
def apertura(name,option):
    img = c.imread(name,option) 
    kernel = np.ones((5,5),np.uint8) 
    apertu = c.morphologyEx(img,c.MORPH_OPEN,kernel)
    c.imwrite('img/Morfologia/apertura.jpg', apertu)
    c.imshow('Apertura',apertu)
    c.waitKey(0)
    c.destroyAllWindows()
    
    
def cierre(name,option):
    img = c.imread(name,option)
    kernel = np.ones((5,5),np.uint8) 
    cier = c.morphologyEx(img,c.MORPH_CLOSE,kernel)
    c.imwrite('img/Morfologia/cierre.jpg', cier)
    c.imshow('Cierre',cier)
    c.waitKey(0)
    c.destroyAllWindows()

def grad(name,option):
    img = c.imread(name,option) 
    kernel = np.ones((5,5),np.uint8) 
    grad = c.morphologyEx(img,c.MORPH_GRADIENT,kernel)
    c.imwrite('img/Morfologia/gradiente.jpg', grad)
    c.imshow('Gradiente',grad)
    c.waitKey(0)
    c.destroyAllWindows()
    
def esqueleto(name,option):
    img = c.imread(name,option)
    img = c.cvtColor(img, c.COLOR_BGR2GRAY)
    size = np.size(img)
    skel = np.zeros(img.shape,np.uint8)
    
    ret,img = c.threshold(img,172,255,0)
    element = c.getStructuringElement(c.MORPH_CROSS,(3,3))
    done = False
    
    while( not done):
        eroded = c.erode(img,element)
        temp = c.dilate(eroded,element)
        temp = c.subtract(img,temp)
        skel = c.bitwise_or(skel,temp)
        img = eroded.copy()
    
        zeros = size - c.countNonZero(img)
        if zeros==size:
            done = True
    c.imwrite('img/Morfologia/esqueleto.jpg',skel)
    c.imshow('Esqueleto',skel)
    c.waitKey(0)
    c.destroyAllWindows()
    
    
    