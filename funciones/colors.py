# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:35:48 2022

@author: omarl
"""
import numpy as np
import cv2 as c

def separetaRGB(name):
    imagen = c.imread(name)
    img = c.cvtColor(imagen, c.COLOR_BGR2RGB)
    negra = np.zeros(img.shape[:2], dtype='uint8')
    B, G, R = c.split(img)
    c.imwrite("img/colors/RGB/Blue.jpg", c.merge([B, negra, negra]))
    c.imwrite("img/colors/RGB/Green.jpg", c.merge([negra, G, negra]))
    c.imwrite("img/colors/RGB/Red.jpg", c.merge([negra, negra, R]))
    c.imwrite("img/colors/RGB/Original.jpg", c.merge([R, G, B]))
    
def separateHSI(name):
    imagen = c.imread(name)
    img = c.cvtColor(imagen, c.COLOR_BGR2HLS)
    negra = np.zeros(img.shape[:2], dtype='uint8')
    H, S, I = c.split(img)
    c.imwrite("img/colors/HSI/Hue.jpg", c.merge([H, negra, negra]))
    c.imwrite("img/colors/HSI/Saturation.jpg", c.merge([negra, S, negra]))
    c.imwrite("img/colors/HSI/Lightness.jpg ", c.merge([negra, negra, I]))
    c.imwrite("img/colors/HSI/Original.jpg", c.cvtColor(c.merge(c.split(img)), c.COLOR_HLS2BGR))

def separateYCbCr(name):
    imagen = c.imread(name)
    img = c.cvtColor(imagen, c.COLOR_BGR2YCrCb)
    negra = np.zeros(img.shape[:2], dtype='uint8')
    Y, Cb, Cr = c.split(img)
    c.imwrite("img/colors/YCbCr/Y,jpg", c.merge([Y, negra, negra]))
    c.imwrite("img/colors/YCbCr/Cb.jpg", c.merge([negra, Cb, negra]))
    c.imwrite("img/colors/YCbCr/Cr.jpg", c.merge([negra, negra, Cr]))
    c.imwrite("img/colors/YCbCr/Original.jpg", c.merge(c.split(img)))

def BGRtoYCbCr(name):
    imagen = c.imread(name)
    alto,ancho,colors = imagen.shape
    conversion = np.array([[0.299,0.587,0.114],[-0.16875,0.33216,0.5],[0.5,0.414869,0.09131]])
    altura,anchura,colors = imagen.shape
    aux = np.zeros((altura,anchura,colors))
    Y = np.zeros((altura,anchura,colors))
    for y in range(altura):
        for x in range(anchura):
            aux[y,x] = np.dot(conversion,imagen[y,x])
            Y[y,x] = [aux[y,x,0],0,0]
    c.imwrite('img/colors/YCbCr/YCbCr.jpg',aux)
    c.imshow("YCBCr",aux)
    c.waitKey()
    c.destroyAllWindows()
    
def YCbCrtoBGR(name):
    imagen = c.imread(name)
    alto,ancho,colors = imagen.shape
    conversion = np.array([[0.299,0.587,0.114],[-0.16875,0.33216,0.5],[0.5,0.414869,0.09131]])
    altura,anchura,colors = imagen.shape
    aux = np.zeros((altura,anchura,colors))
    for y in range(altura):
        for x in range(anchura):
            aux[y,x] = np.dot(np.linalg.inv(conversion),imagen[y,x])
    c.imwrite('img/colors/YCbCr/BGR.jpg',aux)
    c.imshow("BGR",aux)
    c.waitKey()
    c.destroyAllWindows()
    
def BGRtoHSI(name):
    imagen = c.imread(name)
    img =c.cvtColor(imagen,c.COLOR_BGR2HSV)
    c.imwrite('img/colors/HSI/HSI.jpg',img)
    c.imshow("HSI",img)
    c.waitKey()
    c.destroyAllWindows()
    
    
    
    
def HSItoBGR(name):
    imagen = c.imread(name)
    img = c.cvtColor(imagen,c.COLOR_HSV2BGR)
    c.imwrite("img/colors/HSI/BGR.jpg",img)
    c.imshow("BGR",img)
    c.waitKey()
    c.destroyAllWindows()

def BGRtoCMYK(name):
    bgr = c.imread(name)
    bgrdash = bgr.astype(float)/255.
    K = 1 - np.max(bgrdash, axis=2)
    C = (1-bgrdash[...,2] - K)/(1-K)
    M = (1-bgrdash[...,1] - K)/(1-K)
    Y = (1-bgrdash[...,0] - K)/(1-K)
    CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
    c.imwrite('img/colors/CMYK/CMYK.tiff',CMYK)
    c.imshow("CMYK",CMYK)
    c.waitKey()
    c.destroyAllWindows()

def CMYKtoBGR(name):
    imagen = c.imread(name,c.IMREAD_UNCHANGED)
    altura,anchura,colors = imagen.shape
    aux = np.zeros((altura,anchura,colors-1))
    for y in range(altura):
        for x in range(anchura):
            C = imagen[y,x,0]
            M = imagen[y,x,1]
            Y = imagen[y,x,2]
            K = imagen[y,x,3]
            R = 255 * (1-(C/100)) * (1-(K/100))
            G = 255 * (1-(M/100)) * (1-(K/100))
            B = 255 * (1-(Y/100)) * (1-(K/100))
            aux[y,x] = [B,G,R]
    c.imwrite('img/colors/CMYK/BGR.jpg',aux)
    c.imshow("BGR",aux)
    c.waitKey()
    c.destroyAllWindows()

