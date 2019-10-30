import os,sys
os.system("cls")
import random

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

sel1 = random.choice(question_prompts)
question_prompts = [
     "¿Cuál es un tipo de sabor primario?\na) Quemado\nb)Rostizado\nc)Umami\nd)Sabroso\n\n",
     "¿Cuál es el lugar más frío de la tierra??\n(a) Antartida\n(b)Suecia\n(c)Groenlandia\n(d)Islandia\n\n"
]

questions = [
     Question(question_prompts[0], "c"),
     Question(question_prompts[1], "b")
]



        
