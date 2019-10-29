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
     "What color are bananas?\n(a) Red/Green\n(b)Yellow\n\n",
]

questions = [
     Question(question_prompts[0], "c"),
     Question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)



