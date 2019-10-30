import os, sys
os.system("cls")
import random


# Inicio de la Aplicación

print("********* Hola, bienvenido a esta nueva plataforma de aprendizaje.***********")

nombre = str(input("¿Cuál es tu nombre? -----------> "))

print("Hola", nombre)
print("Este programa consiste en responder 20 preguntas de cultura" 
+ " general, \nlas cuales te ayudarán a expandir tus conociminetos.")
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")
print("¿Estas preparado?")
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "¿Cuál es un tipo de sabor primario?\na) Quemado\nb)Rostizado\nc)Umami\nd)Sabroso\n\n",
     "¿Cuál es el lugar más frío de la tierra??\n(a) Antartida\n(b)Suecia\n(c)Groenlandia\n(d)Islandia\n\n",













     "¿Cuál es el país más poblado del mundo?\na)Rusia\nb)China\nc)EE.UU\nd)Canadá \n\n",
     "¿Quién fue el líder de los nazis durante la Segunda Guerra Mundial? \n a)Mussolini \nb)Stalin \n c)Hitler \nd)F.Roosevelt",
     "¿En qué país se encuentra la torre de Pisa? \na)Italia \nb)Francia \nc)España \ndAlemania)",
     "¿Cuantos huesos tiene el cuerpo humano? \na)214 \nb)206 \nc)216 \nd)202",
     "¿Cual de los siguientes animales es un marsupial? \na) \nb) \nc) \nd)",
     "\na) \nb) \nc) \nd)"  
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "\na) \nb) \nc) \nd)"
     "¿ Cuantas fueron las principales cruzadas(1095 - 1291)?\na)3 \nb)6 \nc)8 \nd)5\n\n",
     "¿ Quién fue el primer presidente del Perú?\na)Don José de San Martín \nb)José Mariano de la Riva Agüero y Sánchez Boquete \nc)José Bernardo de Torre Tagle \nd)José de la Mar\n\n",
     "¿ Cómo se la nombró a la primera computadora programable ?\na)Maquina de turing \nb)Z1 \nc)Eniac \nd)Osborne\n\n",
     "¿ Cuál ha sido la guerra más sangrienta de la historia?\na)1ra guerra mundial \nb)2da guerra mubdial \nc)Guerra de vietnam \nd)Guerra civil española\n\n",
     "¿ Cuántas patas tiene una abeja?\na)6 \nb)10 \nc)4 \nd)8\n\n",
     "¿ Cuantos años tiene un lustro ?\na)5 \nb)10 \nc)25 \nd)50\n\n",
     "¿ Con qué otro nombre se denomina al hexaedro?\na)cono \nb)piramide \nc)esfera \nd)cubo\n\n",
     " La capital de Irlanda es:\na)Budapest \nb)Berlín \nc)Atenas \nd)Dúblin\n\n",
     " Si el radio de un círculo mide 5 centímetros, ¿cuánto mide el diámetro?\na)5 centímetros \nb)20 centímetros \nc)10 centímetros \nd)2 centímetros\n\n",
     " ¿Cuál es el planeta de mayor tamaño del Sistema Solar?\na)Mercurio \nb)Marte \nc)Júpiter \nd)Tierra\n\n",
     " Una carga positiva y otra negativa:\na)No pasa nada \nb)Se atraen \nc)Intercambian sus polos \nd)Se repelen\n\n",
     " Colón se embarcó en su viaje a América en tres embarcaciones, ¿Cuál no fue una de ellas?\na)Pinta \nb)Santa María \nc)La Niña \nd)Santa Cristina\n\n",
     " La unidad de volumen en el Sistema Internacional es:\na)Amperio por metro \nb)Amperio por metro cuadrado \nc)Metro cuadrado \nd)Metro cúbico\n\n",
     " La temperatura a la cual la materia pasa de estado líquido a estado gaseoso se denomina:\na)Ecuación de estado \nb)Punto de ebullición \nc)Transición de fase \nd)Punto de fusión\n\n",
     " ¿Cuántas vueltas da el segundero en una vuelta completa en un reloj de doce horas?\na)720 \nb)800 \nc)420 \nd)360\n\n",
     ]

questions = [
     Question(question_prompts[0], "c"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "b")












    
     













     #Diego














     
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)

     