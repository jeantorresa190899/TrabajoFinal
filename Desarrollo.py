import os, sys
os.system("cls")
import random


# Inicio de la Aplicación

print("********* Hola, bienvenido a esta nueva plataforma de aprendizaje.***********")

nombre = str(input("¿Cuál es tu nombre? -----------> "))

print("Hola", nombre)
print("Este programa consiste en responder 20 preguntas de cultura" 
+ " general, \nlas cuales te ayudarán a expandir tus conocimientos.")
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
     "¿Quién escribió La Odisea?\na) Sócrates\nb)Pitágoras\nc)Homero\nd)Aristóteles\n\n",
     "¿Cuántos Estados tiene integrados Estados Unidos? \na) 32\nb)49\nc)50\nd)55\n\n",
     "¿En qué continente está San Marino?\na) América del Norte\nb)América del Sur\nc)Europa\nd)Asia\n\n",
     "¿Quién inventó el primer avión?\na) Los hermanos Wright\nb)Los hermanos Warner\nc)Los hermanos Wachowski\nd)Los hermanos Lumiére\n\n",
     "¿Quién escribió Cien años de soledad?\na) Gabriel García Márquez\nb)Alfredo Bryce Echenique\nc)Cesar Vallejo\nd)Ricardo Úceda\n\n",
     "¿En qué deporte destacaba Toni Elías?\na) Motociclismo\nb)Fútbol\nc)Formula 1\nd)Voley\n\n",
     "¿Qué deporte practicaba Michael Jordan?\na) Baseball\nb)Football\nc)Basketball\nd)Golf\n\n",
     "¿Dónde se inventó el ping-pong?\na) Estados Unidos de América\nb)Inglaterra\nc)Canadá\nd)Irlanda\n\n",
     "¿De qué estilo arquitectónico es la Catedral de Notre Dame en París?\na) Rómanico\nb)Barroco\nc)Neoclásico\nd)Gótico\n\n",
     "¿Quién va a la cárcel?\na) Imputado\nb)Acusado\nc)Condenado\nd)Testigo\n\n",
     "¿A qué país pertenece la ciudad de Varsovia?\na) Polonia\nb)Austria\nc)Rusia\nd)Bielorusia\n\n",
     "¿Cuál es el metal más caro del mundo?\na) Oro\nb)Plata\nc)Rodio\nd)Aluminio\n\n",
     "¿Cuál es la nacionalidad de Pablo Neruda?\na) Chilena\nb)Boliviana\nc)Argentina\nd)Uruguaya\n\n",
     "¿Cuál es el país más poblado del mundo?\na)Rusia\nb)China\nc)EE.UU\nd)Canadá \n\n",
     "¿Quién fue el líder de los nazis durante la Segunda Guerra Mundial? \n a)Mussolini \nb)Stalin \n c)Hitler \nd)F.Roosevelt\n\n",
     "¿En qué país se encuentra la torre de Pisa? \na)Italia \nb)Francia \nc)España \nd)Alemania \n\n",
     "¿Cuantos huesos tiene el cuerpo humano? \na)214 \nb)206 \nc)216 \nd)202 \n\n",
     "¿Cual de los siguientes animales es un marsupial? \na)Gato \nb)Koala \nc)Chimpancé \nd)Conejo\n\n",
     "Si una década tiene 10 años.¿Cuantos años tiene un lustro? \na)20 \nb)10 \nc)5 \nd15)\n\n",  
     "¿En qué año llegó el primer hombre a la Luna?\na)1969 \nb)1979 \nc)1980 \nd)1976)\n\n",
     "¿En que continente se encuentra Haití?\na)Africa \nb)Europa \nc)America \nd)Oceania\n\n",
     "¿Quién pintó “la última cena”?\na)Raffaello Sanzio de Urbino \nb)Miguel Angel \nc)Alessandro di Mariano \nd)Leonardo D'Vinci\n\n",
     "¿Cómo se llama el himno nacional de Francia?\na)Das Lied der Deutschen \nb)The Star-Spangled Banner\nc)Marsellesa \nd)Il Canto degli Italiani\n\n",
     "¿Qué año llegó Cristóbal Colón a América?\na)1512 \nb)1498 \nc)1492 \nd)1495\n\n",
     "¿Cuál es el río más largo del mundo?\na)Yangtsé \nb)Nilo \nc)Amazonas \nd)Misisipi\n\n",
     "¿Cuantos corazones tienen los pulpos?\na)2 \nb)1 \nc)3 \nd)5\n\n",
     "¿Cuál es el libro sagrado del Islam?\na)Biblia \nb)Coran \nc)Credo\nd)Documento de Damasco\n\n",
     "¿En qué país se ubica la Casa Rosada?\na)EE.UU \nb)Uruguay \nc)Argentina \nd)Chile\n\n",
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
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[4], "c"),
     Question(question_prompts[5], "a"),
     Question(question_prompts[6], "a"),
     Question(question_prompts[7], "a"),
     Question(question_prompts[8], "c"),
     Question(question_prompts[9], "b"),
     Question(question_prompts[10], "d"),
     Question(question_prompts[11], "c"),
     Question(question_prompts[12], "a"),
     Question(question_prompts[13], "c"),
     Question(question_prompts[14], "a"),
     Question(question_prompts[15], "b"),
     Question(question_prompts[16], "c"), 
     Question(question_prompts[17], "a"), 
     Question(question_prompts[18], "b"), 
     Question(question_prompts[19], "b"), 
     Question(question_prompts[20], "c"), 
     Question(question_prompts[21], "b"), 
     Question(question_prompts[22], "c"), 
     Question(question_prompts[23], "d"), 
     Question(question_prompts[24], "c"), 
     Question(question_prompts[25], "c"), 
     Question(question_prompts[26], "c"), 
     Question(question_prompts[27], "c"), 
     Question(question_prompts[28], "b"), 
     Question(question_prompts[29], "c"), 
     Question(question_prompts[30], "c"), 
     Question(question_prompts[31], "b"),
     Question(question_prompts[32], "b"),
     Question(question_prompts[33], "b"),
     Question(question_prompts[34], "a"),
     Question(question_prompts[35], "a"),
     Question(question_prompts[36], "d"),
     Question(question_prompts[37], "d"),
     Question(question_prompts[38], "c"),
     Question(question_prompts[39], "c"),
     Question(question_prompts[40], "b"),
     Question(question_prompts[41], "d"),
     Question(question_prompts[42], "d"),
     Question(question_prompts[43], "b"),
     Question(question_prompts[44], "a")
     
]

def run_quiz(questions):
     score = 0
     i = random.randint(0,44)
     question = question_prompts[i]
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)

     