# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:39:58 2022

@author: omarl
"""
import numpy as np 
import cv2 as c


def mediaAritmetica(name,option): 
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = 0
            verde = 0
            azul = 0
            for j in range(3):
                for i in range(3):
                    rojo = rojo +temp[j,i,2]
                    verde= verde + temp[j,i,1]
                    azul = azul + temp[j,i,0]
            aux[y,x] = [(1/9)*azul,(1/9)*verde,(1/9)*rojo]
    c.imwrite('img/filtros/mediaAritmetica.jpg',aux)
    c.imshow('Media Aritmetica',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
    
def mediaGeometrica(name,option): 
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = 1
            verde = 1
            azul = 1
            for j in range(3):
                for i in range(3):
                    rojo = rojo *pow(temp[j,i,2],1/9)
                    verde= verde * pow(temp[j,i,1],1/9)
                    azul = azul * pow(temp[j,i,0],1/9)
                    
            
            aux[y,x] = [azul,verde,rojo]
    c.imwrite('img/filtros/mediaGeometrica.jpg',aux)
    c.imshow('Media Geometrica',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
def mediaHarmonica(name,option): 
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = 0
            verde = 0
            azul = 0
            for j in range(3):
                for i in range(3):
                    if temp[j,i,2] == 0:
                        rojo = rojo +1
                    else:
                        rojo = rojo +(1/temp[j,i,2])
                    if temp[j,i,1] == 0:
                        verde = verde +1
                    else:
                        verde = verde +(1/temp[j,i,1])
                    if temp[j,i,0] == 0:
                        azul = azul +1
                    else:
                        azul = azul +(1/temp[j,i,0])
            aux[y,x] = [9/azul,9/verde,9/rojo]
    c.imwrite('img/filtros/mediaHarminca.jpg',aux)
    c.imshow('Media Harmonica',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
def mediana(name,option): 
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = []
            verde = []
            azul = []
            for j in range(3):
                for i in range(3):
                    rojo.append(temp[j,i,2])
                    verde.append(temp[j,i,1])
                    azul.append(temp[j,i,0])
            aux[y,x] = [np.median(azul),np.median(verde),np.median(rojo)]
    c.imwrite('img/filtros/mediana.jpg',aux)
    c.imshow('Mediana',aux)
    c.waitKey(0)
    c.destroyAllWindows()

def maximo(name,option): 
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = []
            verde = []
            azul = []
            for j in range(3):
                for i in range(3):
                    rojo.append(temp[j,i,2])
                    verde.append(temp[j,i,1])
                    azul.append(temp[j,i,0])
            aux[y,x] = [max(azul),max(verde),max(rojo)]
    c.imwrite('img/filtros/maximo.jpg',aux)   
    c.imshow('Maximo',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
def minimo(name,option): 
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = []
            verde = []
            azul = []
            for j in range(3):
                for i in range(3):
                    rojo.append(temp[j,i,2])
                    verde.append(temp[j,i,1])
                    azul.append(temp[j,i,0])
            aux[y,x] = [min(azul),min(verde),min(rojo)]
    c.imwrite('img/filtros/minimo.jpg',aux)  
    c.imshow('Minimo',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
def puntoMedio(name,option): 
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = []
            verde = []
            azul = []
            for j in range(3):
                for i in range(3):
                    rojo.append(temp[j,i,2])
                    verde.append(temp[j,i,1])
                    azul.append(temp[j,i,0])
            aux[y,x] = [(max(azul)+min(azul))*1/2,(max(verde)+min(verde))*1/2,(max(rojo)+min(rojo))*1/2]
    c.imwrite('img/filtros/puntoMedio.jpg',aux)  
    c.imshow('Punto Medio',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
def mediaAlfaRecortado(name,option,d):
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            rojo = 0
            verde = 0
            azul = 0
            for j in range(3):
                for i in range(3):
                    rojo = rojo +temp[j,i,2]
                    verde= verde + temp[j,i,1]
                    azul = azul + temp[j,i,0]
            aux[y,x] = [(1/(9-d))*azul,(1/(9-d))*verde,(1/(9-d))*rojo]
    c.imwrite('img/filtros/mediaAlfaRecortado.jpg',aux)
    c.imshow('Media Alfa Recortado',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
def calculateProm(mat):
    altura,anchura,color = mat.shape
    rojo = []
    verde = []
    azul = []
    for y in range(altura):
        for x in range(anchura):
            rojo.append(mat[y,x,2])
            verde.append(mat[y,x,1])
            azul.append(mat[y,x,0])
    return [np.mean(azul),np.mean(verde),np.mean(rojo)]

def calculateVarianza(mat):
    altura,anchura,color = mat.shape
    rojo = []
    verde = []
    azul = []
    for y in range(altura):
        for x in range(anchura):
            rojo.append(mat[y,x,2])
            verde.append(mat[y,x,1])
            azul.append(mat[y,x,0])
    return [int(np.var(azul))+1,int(np.var(verde))+1,int(np.var(rojo))+1]

def ruidoLocalAdaptativo(name,option):
    imagen = c.imread(name,option)
    altura,anchura,color = imagen.shape
    aux = np.zeros((altura,anchura,color))
    media = calculateProm(imagen)
    varianza = calculateVarianza(imagen)
    for y in range(1,altura-1):
        for x in range(1,anchura-1):
            temp = imagen[y-1:y+2 , x-1:x+2]
            var = calculateVarianza(temp)
            aux[y,x,0] = imagen[y,x,0] - ((varianza[0]/var[0]) * (imagen[y,x,0]-media[0]))
            aux[y,x,1] = imagen[y,x,1] - ((varianza[1]/var[1]) * (imagen[y,x,1]-media[1]))
            aux[y,x,0] = imagen[y,x,2] - ((varianza[2]/var[2]) * (imagen[y,x,2]-media[2]))
    c.imwrite('img/filtros/ruidoLocalAdaptativo.jpg',aux)  
    c.imshow('Rudio Local Adaptativo',aux)
    c.waitKey(0)
    c.destroyAllWindows()
    
def Gaussiano(name,option) : 
    imagen = c.imread(name,option)
    result = c.GaussianBlur(imagen, (5,5),0)
    c.imwrite('img/filtros/Gaussiano.jpg',result) 
    c.imshow('Gaussiano',result)
    c.waitKey(0)
    c.destroyAllWindows()

def EstContraste(name,option):
    imagen = c.imread(name,option)
    xp = [0, 64, 128, 192, 255]
    fp = [0, 16, 128, 240, 255]
    x = np.arange(256)
    table = np.interp(x, xp, fp).astype('uint8')
    imagenSalida2 = c.LUT(imagen, table)
    c.imwrite("img/filtros/EstiramientoContraste.jpg", imagenSalida2)
    c.imwrite('img/Bordes/EstirarContraste.jpg',imagenSalida2) 
    c.imshow('Estirar Contraste',imagenSalida2)
    c.waitKey(0)
    c.destroyAllWindows()
                   
def NivGris(name,option):
    imagen = c.imread(name,option)
    l = 156
    rows, columns = imagen.shape
    imagenSalida2 = np.zeros((rows, columns), dtype=np.uint8)
    for x in range(rows):
        for y in range(columns):
            imagenSalida2[x, y] = (l - 1) - imagen[x, y]
    c.imwrite("img/Bordes/NivelesGris.jpg", imagenSalida2)
    c.imshow('Niveles de Gris',imagenSalida2)
    c.waitKey(0)
    c.destroyAllWindows()
    
def TransformacionGamma(name,option):
    imagen = c.imread(name,option)
    porcentaje = 2.9
    for gamma in [porcentaje]:
        gamma = np.array(255 * (imagen / 255) ** gamma, dtype='uint8')
    c.imwrite('img/Bordes/TransformacionGamma.jpg', gamma)
    c.imshow('Transformacion Gamma',gamma)
    c.waitKey(0)
    c.destroyAllWindows()
    
def PlanoBits(name,option):
    imagen = c.imread(name,option)
    lst = []
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            lst.append(np.binary_repr(imagen[i][j], width=8))
    imagenSalida2 = (np.array([int(i[0]) for i in lst], dtype=np.uint8) * 128).reshape(imagen.shape[0], imagen.shape[1])
    c.imwrite('img/Bordes/PlanoBits.jpg', imagenSalida2)
    c.imshow('Plano de Bits',imagenSalida2)
    c.waitKey(0)
    c.destroyAllWindows()
    
def ConvSobel(name,option,threshold):
    imagen = c.imread(name,option)
    #Mascara Sobel Vertical
    X = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    #Mascara Sobel Horizontal
    Y = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
    alto,ancho = imagen.shape
    imagenSalida2 = np.zeros((alto,ancho))
    for i in range(0, alto - 2):
        for j in range(0, ancho - 2):
            #Obtenemos el gradiente Vertical
            v = sum(sum(X * imagen[i:i+3, j:j+3])) 
            #Obtenemos el gradiente Horizontal
            h = sum(sum(Y * imagen[i:i+3, j:j+3])) 
            #Obetenmos la distancia  
            imagenSalida2[i+1, j+1] = np.sqrt((v ** 2) + (h ** 2))
    #Verificamos si no hay valores negativos           
    for i in range(0, alto):
        for j in range(0, ancho):
            if imagenSalida2[i, j] < threshold:
                imagenSalida2[i, j] = 0
    c.imwrite("img/Bordes/convolusionSobel.jpg",imagenSalida2)
    c.imshow('Convolusion Sobel',imagenSalida2)
    c.waitKey(0)
    c.destroyAllWindows()
    
def Prewitt(name,option, threshold):
    imagen=c.imread(name,option)
    #Mascara Sobel Vertical
    X = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
    #Mascara Sobel Horizontañ
    Y = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])
    alto,ancho = imagen.shape
    imagenSalida2 = np.zeros(imagen.shape)
    for i in range(0, alto - 2):
        for j in range(0, ancho - 2):
            #Obtenemos el gradiente Vertical
            v = sum(sum(X * imagen[i:i+3, j:j+3])) 
            #Obtenemos el gradiente Horizontal
            h = sum(sum(Y * imagen[i:i+3, j:j+3])) 
            #Obetenmos la distancia  
            imagenSalida2[i+1, j+1] = np.sqrt((v ** 2) + (h ** 2))

    #Verificamos si no hay valores negativos           
    for i in range(0, alto):
        for j in range(0, ancho):
            if imagenSalida2[i, j] < threshold:
                imagenSalida2[i, j] = 0
    c.imwrite("img/Bordes/Prewitt.jpg",imagenSalida2)
    c.imshow('Prewitt',imagenSalida2)
    c.waitKey(0)
    c.destroyAllWindows()