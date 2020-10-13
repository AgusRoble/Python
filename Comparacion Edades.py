
print("Ingrese un nombre: ")
Nombre1 = input()
print("Ingrese su edad: ")
Edad1 = input()
print("Ingrese otro nombre: ")
Nombre2 = input()
print("Ingrese su edad: ")
Edad2 = input()

if Edad1 < Edad2:
	print(f"{Nombre1} es menor que {Nombre2}")
elif Edad1 > Edad2:
	print(f"{Nombre1} es mayor que {Nombre2}")
elif Edad1 == Edad2:
	print(f" {Nombre1} y {Nombre2} tienen la misma edad")
else:
	print("Datos no validos")