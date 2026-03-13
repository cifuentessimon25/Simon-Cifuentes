
nota_1 = float(input("Ingrese la nota 1: "))
while nota_1 <0 or nota_1 >100:
    print("El valor ingresado no es válido. Por favor, ingrese un número entre 0 y 100.")
    nota_1 = float(input("Ingrese BIEN la nota1: "))

nota_2 = float(input("Ingrese la nota 2: "))
while nota_2 <0 or nota_2 >100:
    print("El valor ingresado no es válido. Por favor, ingrese un número entre 0 y 100.")
    nota_2 = float(input("Ingrese BIEN la nota2: "))

nota_3 = float(input("Ingrese la nota 3: "))
while nota_3 <0 or nota_3 >100:
    print("El valor ingresado no es válido. Por favor, ingrese un número entre 0 y 100.")
    nota_3 = float(input("Ingrese BIEN la nota3: "))

nota_4 = float(input("Ingrese la nota 4: "))
while nota_4 <0 or nota_4 >100:
    print("El valor ingresado no es válido. Por favor, ingrese un número entre 0 y 100.")
    nota_4 = float(input("Ingrese BIEN la nota4: "))

nota_5 = float(input("Ingrese la nota 5: "))
while nota_5 <0 or nota_5 >100:
    print("El valor ingresado no es válido. Por favor, ingrese un número entre 0 y 100.")
    nota_5 = float(input("Ingrese BIEN la nota5: "))


promedio = (float(nota_1) + float(nota_2) + float(nota_3) + float(nota_4) + float(nota_5)) / 5
if promedio >= 60:
    print("El estudiante aprobó con un promedio de: ", promedio)
elif promedio >40 and promedio <60:
    print("El estudiante está en recuperación con un promedio de: ", promedio)
else:    print("El estudiante reprobó con un promedio de: ", promedio)