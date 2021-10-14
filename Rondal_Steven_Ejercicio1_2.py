# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:25:49 2021

@author: Steven
"""
# Programa que permite conocer el tipo de dato de un valor ingresado
# por el usuario en 5 iteraciones, el resultado siempre es 'str' ya
# la funcion input() retorna un string

valor = input("Primera Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:", type(valor))

valor = input("Segunda Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:", type(valor))

valor = input("Tercera Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:", type(valor))

valor = input("Cuarta Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:", type(valor))

valor = input("Quinta Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:", type(valor))
print("¡YA NO SE HARÁN MÁS INTERACCIONES!")

# Nota: Se podria cambiar el tipo de dato haciendo un cast
# ej --> int(input("Ingrese un valor:"))