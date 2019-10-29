import os, sys
os.system("cls")


# Inicio de la Aplicación

print("********* Hola, bienvenido a esta nueva plataforma de aprendizaje.***********")

nombre = str(input("¿Cuál es tu nombre? -----------> "))

print("Hola", nombre)
print("Este programa consiste en responder 20 preguntas de cultura" 
+ " general, \n las cuales te ayudarán a expandir tus conociminetos.")

comenzar = str(input("Comenzamos? "))


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "¿Cuál es un tipo de sabor primario?\n(a) Quemado\n(b)Rostizado\n(c)Umami\n(d)Sabroso\n\n",
     "¿Cuál es el lugar más frío de la tierra??\n(a) Antartida\n(b)Suecia\n(c)Groenlandia\n(d)Islandia\n\n"













     "¿Cuál es el país más poblado del mundo?\n(a)Rusia \n(b)China\n (c)EE.UU\n (d)Canada \n\n",
     
     3
     4
     5
     6
     7
     8
     9
     10
     11
     12
     13
     14
     15
     1
     2
     3
     4
     5
     6
     7
     8
     9
     10
     11
     12
     13
     14
     15
     ]

questions = [
     Question(question_prompts[0], "c"),
     Question(question_prompts[1], "b"),
     











     #Jean













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



