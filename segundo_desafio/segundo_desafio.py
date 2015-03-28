# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 09:43:11 2015

@autor: danne
@email: daniel.epm12@gmail.com

"EL ARTE NO ES UN ESPEJO DE LA REALIDAD
SINO  UN MARTILLO PARA TRANSFORMARLA"
                        BERTORLT BRECHT
"""

#!/usr/bin/python
import os
import glob
import readline
import numpy as np
import random

print ("Digite el directorio de trabajo:")
directorio=raw_input()

while os.path.exists(directorio)==False:
    print"Directorio Invalido digite de nuevo:"
    directorio=raw_input()

os.chdir(directorio)
actual= os.getcwd()
print "Su directorio actual es: "
print ""
print "%s" %actual

lista = (glob.glob("*.txt") and glob.glob("*"))
print "Este directorio contiene los siguientes archivos"
print ""
print "%s" %lista
print ""
print "Desea continuar (s). Volver al paso anterior(n): "
confirmacion=raw_input()

while confirmacion!="s":
    print ("Digite el directorio de trabajo:")
    directorio=raw_input()

    while os.path.exists(directorio)==False:
        print"Directorio Invalido digite de nuevo:"
        directorio=raw_input()
    os.chdir(directorio)
    actual= os.getcwd()
    print "Su directorio actual es:"
    print ""
    print "%s" %actual
    print ""
    lista = glob.glob("*.txt") and glob.glob("*")
    print "Este directorio contiene los siguientes archivos"
    print ""
    print "%s"%lista
    print ""
    print "Desea continuar (s) Volver al paso anterior(n): "
    confirmacion=raw_input()


listNames = np.array([])
for i in lista:
    xfile=i
    stringx=np.loadtxt(open(xfile, "r"),dtype=np.str)
    listNames = np.append(listNames,stringx)

print "Los elementos que seran aleatorizados son:"
print ""
print listNames
print ""
print "Presione (s) para continuar, (n) para salir"
confirmacion=raw_input()
if confirmacion != "s":
    print "Que tenga un buen día y recuerde:"
    print "A ESTUDIAR PARA LUCHAR"
    print "A LUCHAR PARA ESTUDIAR"

else:
    random.shuffle(listNames)
    print "El orden para los siguientes desafios, es el siguiente:"
    print ""
    for w in listNames:
        print w
    print ""
    print "Que tenga un buen día y recuerde:"
    print "A ESTUDIAR PARA LUCHAR   "
    print "A LUCHAR PARA ESTUDIAR"
    print ""
    print "Presione enter para salir"
    raw_input()
