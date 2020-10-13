Nombre1,Edad1 = input("Ingrese un nombre: "),int(input("Ingrese su edad: "))
Nombre2,Edad2 = input("Ingrese otro nombre: "),int(input("Ingrese su edad: "))

if Edad1 < Edad2:
	print(f"{Nombre1} es menor que {Nombre2}")
elif Edad1 > Edad2:
	print(f"{Nombre1} es mayor que {Nombre2}")
elif Edad1 == Edad2:
	print(f" {Nombre1} y {Nombre2} tienen la misma edad")
else:
	print("Datos no validos")