"""
Nombre : Ruben Luquin Sanchez
Grupo  : 2I
Fecha  :11/03/26 
"""
#-------------------------------------------------------------------------#
#Escribir un metodo que acepte el porcentaje de un alumno y evalue el grado de acuerdo al siguiente criterio
#Calificacion	Grado
#   >90				A
#   >80 y <= 90		B
#   >=60 y <=80		C
#   menor a 60		D
porcentaje = float(input("Porcentaje: "))

if porcentaje > 90:   grado = "A"
elif porcentaje > 80: grado = "B"
elif porcentaje >= 60:grado = "C"
else:                 grado = "D"

print("Grado:", grado)


#-------------------------------------------------------------------------#
#Escribir un metodo que capture el precio de una bicicleta y muestre los impuestos que debe pagar siguiendo los criterios siguientes:
# Costo					Impuesto
# >100000				15%
# >50000 y <= 100000	10% 
#<=50000				 5%
costo=float(input("precio de la bicicleta?: "))
if costo > 100000:impuesto="15%"
elif costo > 50000:impuesto="10%"
else:   impuesto="5%"


#-------------------------------------------------------------------------#
#Escribir un metodo que verifique si un año es bisiesto o no


#-------------------------------------------------------------------------#
#Escribir un metodo que capture un numero del 1 al 7 y muestre el nombre del dia de la semana
#Por ejemplo el 1 seria Domingo y el 2 Lunes


#-------------------------------------------------------------------------#
#Escribir un metodo que acepte un numero del 1 al 12 y muestre el nombre del mes asi como los dias que contiene
#Ejemplo 1 seria Enero tiene 31 dias

#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales

#-------------------------------------------------------------------------#
#Escibir un programa que imprima los primeros 10 numeros impares

#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales en orden descendente

#-------------------------------------------------------------------------#
#Escribir un programa que escriba la tabla de multiplicar de un numero especificado por el usuario

#-------------------------------------------------------------------------#
#Escribir un programa que escriba el producto de los digitos de un numero especificado por el usuario
