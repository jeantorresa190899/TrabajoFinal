import os, sys
os.system("cls")


# Inicio de la Aplicación

print("********* Hola, bienvenido a esta nueva plataforma de aprendizaje.***********")

nombre = str(input("¿Cuál es tu nombre? -----------> "))

print("Hola", nombre)
print("Este programa consiste en responder 20 preguntas de cultura" 
+ " general, \n las cuales te ayudarán a expandir tus conociminetos.")

respuesta = str(input("Comenzamos? "))

print("1. ¿Cuál es un tipo de sabor primario?")
print("a) quemado")
print("b) umami")
print("c) rostizado")
print ("d) sabroso")
respuesta1 = str(input(""))
if respuesta1 == "umami":
    print("Correcto!")
else:
    print("Incorrecto")



