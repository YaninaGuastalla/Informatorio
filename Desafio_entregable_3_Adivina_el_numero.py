from random import randint 

nombre  =  input ('Ingrese su nombre: ')
numero_aleatorio  =  randint(1,100)
intentos  =  8

print ('Adivine un número entre 1 y 100')

while  intentos  >  0:
    print (f'Intentos restantes: {intentos}')
    numero_usuario  =  input('Ingrese un número entero: ')
    if not numero_usuario.isdigit():
        print('Error, no ingresó un número entero')
    else:
        numero_usuario  =  int (numero_usuario)
        if  numero_usuario  <  numero_aleatorio:
            print ('El número a adivinar es mayor')
            intentos  -=  1
        elif  numero_usuario  >  numero_aleatorio:
            print ('El número a adivinar es menor')
            intentos  -=  1
        else:
            print (f'Felicitaciones {nombre}, adivinaste el número en el intento {9 - intentos}')
            break
if  intentos  ==  0:
    print (f'Se agotaron los intentos, el número a adivinar era {numero_aleatorio}')