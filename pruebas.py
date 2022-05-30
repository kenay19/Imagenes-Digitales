# -*- coding: utf-8 -*-
"""
Created on Wed May 25 20:25:49 2022

@author: omarl
"""


import funciones.ruido as ruido 
import funciones.filros as filtros
import funciones.Morfologia as morfologia
import funciones.colors as colors

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

def selectFiltros():
    opcion = "s"
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
            filtros.mediaAritmetica('img/filtros/sal.jpg',1)
        elif opcion == 2:
            filtros.mediaGeometrica('img/filtros/sal.jpg',1)
        elif  opcion == 3:
            filtros.mediaHarmonica('img/filtros/sal.jpg',1)
        elif opcion == 4:
            filtros.mediana('img/filtros/sal.jpg',1)
        elif opcion == 5:
            filtros.maximo('img/filtros/sal.jpg',1)
        elif opcion == 6:
            filtros.minimo('img/filtros/sal.jpg',1)
        elif opcion == 7:
            filtros.puntoMedio('img/filtros/sal.jpg',1)
        elif opcion == 8:
            filtros.mediaAlfaRecortado('img/filtros/sal.jpg',1,int(input("introduce un numero entre 0 y 9: ")))
        elif opcion == 9:
            filtros.ruidoLocalAdaptativo('img/filtros/sal.jpg',1)
        elif opcion == 10:
            filtros.Gaussiano('img/filtros/sal.jpg',1)
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
            morfologia.erosion('img/Morfologia/test.jpg', 0)
        elif opcion == 2:
            morfologia.dilatacion('img/Morfologia/test.jpg', 0)
            
        elif opcion == 3:
            morfologia.apertura('img/Morfologia/test.jpg', 0)
        elif opcion == 4:
            morfologia.cierre('img/Morfologia/test.jpg', 0)
        elif opcion == 5: 
            morfologia.grad('img/Morfologia/test.jpg', 0)
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
            colors.CMYKtoBGR('img/colors/CMYK/CMYK.tiff')
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")
       
def selectMain():
    opcion = "s"
    while opcion == "S" or opcion =="s":
        print("1) Ruidos")
        print("2) Filtros ")
        print("3) Deteccion de Bordes")
        print("4) Colores")
        print("5) Morfologia")
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
        opcion = input("Desea Continuar con Alguna Otra Operacion (S/N): ")
        
        
                

selectMain()

