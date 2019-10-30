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

     