# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:25:49 2021

@author: Steven
"""
# Imprimir titulo tabulado y autor del código
print("\t\t\t\t\tEmpezando a trabajar con Python\n")
print("Realizado por: Steven Rondal\n")

# Consultar tipos de valores
print("Consultando los tipos de valores:")
# Consultar tipos de datos particulares usando la funcion type(dato)
print("El tipo de dato de 875 es:", type(875))
print("El tipo de dato de 4.89 es:", type(4.89))
print("El tipo de dato del texto: Now is better than never. es:", type("Now is better than never."))
print("El tipo de dato de 1.32 es:", type(1.32))
# Consultar a traves de un booleano (True/False) si se tiene un tipo de dato en concreto
# mediante la funcion isinstance(dato, tipo de dato)
print("¿El valor 5 + 8i corresponde a un valor entero?", isinstance(5 + 8j, int))
print("¿El valor 8.2 corresponde a un valor entero?", isinstance(8.2, int))
print("¿El texto: Readability counts. corresponde a un string?", isinstance("Readability counts.", str))