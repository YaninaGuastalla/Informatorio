'''
GRUPO 11:
Guastalla Yanina
Sosa Carlos Ezequiel
Espinoza Matías Exequiel
Alejandra Diaz RACH
Ayala Rivero, Fredi Gabriel
Maidana Elizabeth
Flores Vanina Andrea
Fernandez Axel
SOTELO Franco Ariel
Rony Sebastian Mari
Rocio cardozo
Fernandez Miguel Angel

Desafío entregable 3: Adivina el número
'''

nombre=input('Ingrese su nombre aqui: ')
print(f"Hola {nombre}! intenta adivinar el numero secreto, es un numero entero que esta entre el 1 y el 100. Solo tenes 8 intentos para lograrlo...")

import random
intentosFaltantes = 8
intentosRealizados = 0

número = random.randint(1,100)

while intentosRealizados < 8:
 	estimación = input('Ingresa un numero entero: ')
 	if not estimación.isdigit():
 		print('Error, no ingresó un número entero. Puede volver a ingresar sin perder este intento')
 	else:
 		estimación = int(estimación)
 		intentosRealizados = intentosRealizados + 1
 		intentosFaltantes = intentosFaltantes - 1
 		if estimación < número:
 			print(f'Tu estimación es muy baja. Te quedan {intentosFaltantes} intentos')
 		elif estimación > número:
 			print(f'Tu estimación es muy alta. Te quedan {intentosFaltantes} intentos')
 		else:
 			print(f'Lo lograste {nombre}! adivinaste el numero secreto en el intento nro: {intentosRealizados}')
 			break

if intentosRealizados ==  8:
	print (f'Ya se te acabaron los intentos ! El numero secreto era {número}')