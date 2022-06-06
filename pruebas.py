# -*- coding: utf-8 -*-
"""
Created on Wed May 25 20:25:49 2022

@author: omarl
"""


import funciones.ruido as ruido 
import funciones.filros as filtros
import funciones.Morfologia as morfologia
import funciones.colors as colors
import funciones.segmentacion as seg

def selectRuidos() :
    opcion = "s"
    while opcion == "S" or opcion =="s":
        print("1) Ruido Sal")
        print("2) Ruido Pimienta")
        print("3) Ruido Sal y Pimienta")
        opcion = int(input("Seleccionar una operacion: "))
        if opcion == 1:
            ruido.Sal('img/ruido/test.jpg',1,float(input("Da un porcentaje de ruido (de 0 a 1): ")))
        elif opcion == 2:
            ruido.Pimienta('img/ruido/test.jpg',1,float(input("Da un porcentaje de ruido (de 0 a 1): ")))
        elif  opcion == 3:
            ruido.SalyPimienta('img/ruido/test.jpg',1,float(input("Da un porcentaje de ruido (de 0 a 1): ")))
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")
        
def chooseImg():
    print("1) Aplicar en sal")
    print("2) Aplicar en Pimienta")
    print("3) Aplicar en Sal y Pimienta")
    try:
        opcion = int(input("Elige una opcion: "))
        if opcion >= 1 and opcion <= 3:
            return opcion-1
        else:
            print("Elige un un numero dentro de las opciones")
            return chooseImg()-1
    except:
        print("Digita un numero")
        return chooseImg()-1
    
def selectFiltros():
    opcion = "s"
    opciones = ['img/ruido/Sal.jpg','img/ruido/Pimienta.jpg','img/ruido/SalyPimienta.jpg']
    while opcion == "S" or opcion =="s":
        print("1) Media Aritmetica")
        print("2) Media Geometrica")
        print("3) Media Harmonica")
        print("4) Mediana")
        print("5) Maximo")
        print("6) Minimo")
        print("7) Punto Medio")
        print("8) Media Alfa Recortado")
        print("9) Ruido Local Adaptativo")
        print("10) Filtro Gaussiano")
        opcion = int(input("Seleccionar una operacion: "))
        if opcion == 1:
            filtros.mediaAritmetica(opciones[chooseImg()],1)
        elif opcion == 2:
            filtros.mediaGeometrica(opciones[chooseImg()],1)
        elif  opcion == 3:
            filtros.mediaHarmonica(opciones[chooseImg()],1)
        elif opcion == 4:
            filtros.mediana(opciones[chooseImg()],1)
        elif opcion == 5:
            filtros.maximo(opciones[chooseImg()],1)
        elif opcion == 6:
            filtros.minimo(opciones[chooseImg()],1)
        elif opcion == 7:
            filtros.puntoMedio(opciones[chooseImg()],1)
        elif opcion == 8:
            filtros.mediaAlfaRecortado(opciones[chooseImg()],1,int(input("introduce un numero entre 0 y 9: ")))
        elif opcion == 9:
            filtros.ruidoLocalAdaptativo(opciones[chooseImg()],1)
        elif opcion == 10:
            filtros.Gaussiano(opciones[chooseImg()],1)
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")
        
        
def selectBordes():
    opcion = "s"
    while opcion == "S" or opcion =="s":
        print("1) Estirar Constraste")
        print("2) Niveles de Gris")
        print("3) Transformcacion Gamma")
        print("4) Plano de Bits")
        print("5) Sobel")
        print("6) Prewwitt")
        print("7) Cany")
        opcion = int(input("Selecciona uno: "))
        if opcion == 1:
            filtros.EstContraste('img/Bordes/test.jpg',1)
        elif opcion == 2:
            filtros.NivGris('img/Bordes/test.jpg',0)
        elif opcion == 3:
            filtros.TransformacionGamma('img/Bordes/test.jpg',1)
        elif opcion == 4:
            filtros.PlanoBits('img/Bordes/test.jpg',0)
        elif opcion == 5: 
            filtros.ConvSobel('img/Bordes/test.jpg',0,int(input("Da un numero: ")))
        elif opcion == 6:
            filtros.Prewitt('img/Bordes/test.jpg',0,int(input("Da un numero: ")))
        elif opcion == 7:
            filtros.Canny('img/Bordes/test.jpg')
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")    
        
def selectMorfo():
    opcion = "s"
    while opcion == "S" or opcion =="s":
        print("1) Erosion")
        print("2) Dilatacion")
        print("3) Apertura")
        print("4) Cierre")
        print("5) Gradiente")
        print("6) esqueleto")
        opcion = int(input("Selecciona uno: "))
        if opcion == 1:
            morfologia.erosion('img/Morfologia/test.jpg', int(input('De un umbral: ')))
        elif opcion == 2:
            morfologia.dilatacion('img/Morfologia/test.jpg', int(input('De un umbral: ')))
            
        elif opcion == 3:
            morfologia.apertura('img/Morfologia/test.jpg', int(input('De un umbral: ')))
        elif opcion == 4:
            morfologia.cierre('img/Morfologia/test.jpg', int(input('De un umbral: ')))
        elif opcion == 5: 
            morfologia.grad('img/Morfologia/test.jpg', int(input('De un umbral: ')))
        elif opcion == 6:
            morfologia.esqueleto('img/Morfologia/test.jpg', 1)
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")    
        
def selectColor():
    opcion = "s"
    while opcion == "S" or opcion =="s":
        print("1) RGB a YCbCr")
        print("2) YCbCr a RGB")
        print("3) RGB a HSI")
        print("4) HSI a RGB") 
        print("5) RGB a CMYK")
        print("6) CMYK a RGB")
        print("7) Separar RGB")
        print("8) Separar HSI")
        print("9) Separar YCbCr")
        opcion = int(input("Selecciona uno: "))
        if opcion == 1:
            colors.BGRtoYCbCr('img/colors/test.jpg')
        elif opcion == 2:
            colors.YCbCrtoBGR('img/colors/YCbCr/YCbCr.jpg')
        elif opcion == 3:
            colors.BGRtoHSI('img/colors/test.jpg')
        elif opcion == 4:
            colors.HSItoBGR('img/colors/HSI/HSI.jpg')
        elif opcion == 5: 
            colors.BGRtoCMYK('img/colors/test.jpg')
        elif opcion == 6:
            colors.CMYKtoBGR('img/colors/CMYK/CMYK.pdf')
        elif opcion == 7:
            colors.separetaRGB('img/colors/test.jpg')
        elif opcion == 8:
            colors.separateHSI('img/colors/test.jpg')
        elif opcion == 9:
            colors.separateYCbCr('img/colors/test.jpg')
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")
       
def selectSeg():
    opcion = "s"
    while opcion == "S" or opcion =="s":
        print("1) Por historgrama")
        print("2) Por Bordes")
        print("3) Por transformada hough")
        opcion = int(input("Selecciona uno: "))
        if opcion == 1:
            seg.HistogramSegmentation('img/segmentacion/test.jpg',int(input('Ingrese un umbral: ')))
        elif opcion == 2:
            colors.YCbCrtoBGR('img/colors/YCbCr/YCbCr.jpg')
        elif opcion == 3:
            seg.TransHough('img/segmentacion/test.jpg')
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")

def selectMain():
    opcion = "s"
    while opcion == "S" or opcion =="s":
        print("1) Ruidos")
        print("2) Filtros ")
        print("3) Deteccion de Bordes")
        print("4) Colores")
        print("5) Morfologia")
        print('6) Segmentacion')
        opcion = int(input("Seleccionar un tipo: "))
        if opcion == 1:
            selectRuidos()
        elif opcion == 2:
            selectFiltros()
        elif opcion == 3:
            selectBordes()
        elif opcion == 4:
            selectColor()
        elif opcion == 5:
            selectMorfo()
        elif opcion == 6:
            selectSeg()
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")
        
        
                

selectMain()

