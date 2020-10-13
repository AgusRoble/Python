
print("Ingrese un nombre: ")
Nombre1 = input()
print("Ingrese un apellido: ")
Apellido1 = input()
print("Ingrese su edad: ")
Edad1 = input()
print("Ingrese otro nombre: ")
Nombre2 = input()
print("Ingrese un apellido: ")
Apellido2 = input()
print("Ingrese su edad: ")
Edad2 = input()

if Nombre1 == Nombre2 or Apellido1 == Apellido2:
	print("no pueden haber mismos nombres y apellidos")
else:
	if Edad1 < Edad2:
		print(f"{Nombre1} es menor que {Nombre2}")
	elif Edad1 > Edad2:
		print(f"{Nombre1} es mayor que {Nombre2}")
	elif Edad1 == Edad2:
		print(f" {Nombre1} y {Nombre2} tienen la misma edad")
	else:
		print("Datos no validos")
