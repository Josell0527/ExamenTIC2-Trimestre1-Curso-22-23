#1. Crea una copia de este repositorio en tu cuenta de github. Recuerda que no puedes crear uno nuevo y luego copiar este documento, hay una manera más rápida...
#2. Una vez copiado en tu cuenta de github, clona el repositorio en tu ordenador con gitkraken para empezar a trabajar.
#3. Crea un fichero con el nombre "Examen-TUNOMBRE".py
#4. Crea una función que NO reciba ningún parámetro y que imprima por pantalla las opciones: 1-Sumar  2-Salir
#5. Crea una función que reciba dos números y devuelva la suma de estos números. 
#6. El programa principal tiene que mostrar el menú de la función y hasta que se pulse la opción 2-Salir el programa tiene que funcionar.
#7. Si se pulsa la opción 1, el programa pide al usuario dos números y con la ayuda de la función sumar mostrar por pantalla el resultado.
#8. Cuando el usuario introduce dos números se puede equivocar e introducir caracteres con lo que el programa se interrumpe. Realiza los cambios necesarios para controlar estos errores.
#9. Sube los cambios a tu repositorio y copia la dirección en la entrega del examen.

num=0
def imprimir():
   print("1-Sumar")
   print("2-Salir")


def suma(num1,num2):
    sumatorio= num1+num2
    return (sumatorio)



opcion= 0

while (opcion!=2):
    imprimir()
    opcion= int(input("Dime un número"))
    if (opcion==1):
            try:
                num1= int(input("Dime un número"))
                num2= int(input("Dime otro número"))
                print("La suma es:", suma(num1,num2))
                imprimir()
                opcion= int(input("Dime un número"))
            except:
                print("Número inválido")


print("Has salido del programa")
    