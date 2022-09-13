import time    # importamos libreria de tiempo
import random  # Importamos la librería random

#Variables fijas de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#oportunidades
oportunidades = 1

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)

#Bienvenida a la trivia
print ('Bienvenido a trivia acerca de cuanto sabes de Historia del Perú')
print ('Pondremos a prueba tus conocimientos')

#Agregaremos personalización consultando nombre
nombre = input('\nIngresa tu nombre: ')

print(YELLOW +'\nHola',nombre, 'responde las siguientes preguntas escribiendo la letra de la alternativa y presionando "Enter" para enviar tu respuesta.\n'+ RESET)

#Preguntas y respuestas
print(RED+ '1) ¿Cuándo se dio la declaración de la independencia del Perú '+ RESET)
print('a) 28 de Julio de 1821')
print('b) 29 de Julio de 1821')
print('c) 29 de Julio de 1823')
print('d) 28 de Julio de 1823')

# Respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input('\nTu respuesta: ')

#Condicional While
while respuesta_1 not in ('a', 'b', 'c', 'd','x'):
  respuesta_1 = input('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

#condicional if/elif/else para verificar respuesta
if respuesta_1 == 'b':
  print(MAGENTA +'Incorrecto!', nombre, ',29 de Julio de 1821 no es la respuesta correcta'+ RESET)
elif respuesta_1 == 'c':
  print(MAGENTA +'Incorrecto!', nombre, ',29 de Julio de 1821 no es la respuesta correcta'+ RESET)
elif respuesta_1 == 'd':
  print(MAGENTA +'Incorrecto!', nombre, ',29 de Julio de 1821 no es la respuesta correcta'+ RESET)
elif respuesta_1 == 'x':
  print(nombre,'Este es un mensaje secreto')
else:
  puntaje = puntaje + 10
  print(GREEN +'Muy bien', nombre, '!'+ RESET)

time.sleep(2) # Espera 2 segundos antes de continuar.
# Pregunta 2
print (RED+ '\n1) ¿Qué hecho historico se conmemora el 8 de Octubre?'+ RESET)
print ('a) Batalla de Arica')
print ('b) Combate de Iquique')
print ('c) Batalla de Ayacucho')
print ('d) Combate de Angamos')

# Almacenamos la rspuesta del usuario en la variable "respuesta_2"
respuesta_2 = input('\nTu respuesta: ')

while respuesta_2 not in ('a', 'b', 'c', 'd'):
  respuesta_2 = input ('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_2 == 'a':
  print (MAGENTA +'Incorrecto!', nombre, 'La batalla de Arica fue el 7 de junio de 1880'+ RESET)
elif respuesta_2 == 'b':
  print (MAGENTA +'Incorrecto!', nombre, 'El combate de Iquique fue el 21 de Mayo de 1879'+ RESET)
elif respuesta_2 == 'c':
  print (MAGENTA +'Incorrecto!', nombre, 'La batalla de Ayacucho fue el 9 de Diciembre de 1824'+ RESET)
else:
  puntaje += 10
  print (GREEN +'Muy bien', nombre, '!'+ RESET)

time.sleep(2) # Espera 2 segundos antes de continuar.
# Pregunta 3
print (RED+ '\n1) ¿A quién se le conocía como el “Brujo de los andes?'+ RESET)
print ('a) Miguel Grau Seminario')
print ('b) Andrés Avelino Cáceres')
print ('c) José Faustino Sánchez Carríon')
print ('d) José Gabriel Condorcanqui')

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input('\nTu respuesta: ')

while respuesta_3 not in ('a', 'b', 'c', 'd'):
  respuesta_3 = input ('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

if respuesta_3 == 'a':
  print (MAGENTA +'Totalmente incorrecto! ...'+ RESET)
  puntaje = puntaje / 2
elif respuesta_3 == 'd':
  print (MAGENTA +"Incorrecto!..."+ RESET)
  puntaje = puntaje - 5
elif respuesta_3 == 'c':
  print (MAGENTA +'Incorrecto! ...'+ RESET)
  puntaje = puntaje - 5
else:
  print (GREEN +'Correcto! ...'+ RESET)
  puntaje = puntaje + 5
  
# Pregunta 4
pregunta_4 = print(RED + '\n 4) ¿Cúal de estas maravillas del mundo se encuentra en Perú?'+ RESET)
print('a) La ciudad de Petra')
print('b) Chichén Itzá')
print('c) La Gran Muralla China')
print('d) Machu Picchu.')

respuesta_4 = 'd'

#Bucle for
for i in range(oportunidades):
    respuesta = input('Pon tu respuesta: ')
    if (respuesta.lower() == respuesta_4):
        print(GREEN +'Muy bien !',nombre, 'Eres un master'+ RESET)
        puntaje = puntaje + 5
        break
    else:
        print(MAGENTA +'Incorrecto!!Repasando mejorarás\n'+ RESET)
        puntaje = puntaje - 5
        time.sleep(0.5)
        print("La respuesta correcta es", respuesta_4,'Machu Picchu es la maravilla que se encuentra en el Perú''\n\n')
  
#Puntaje obtenido
print('Gracias', nombre,'por juegar mi trivia, alcanzaste', puntaje,'puntos')