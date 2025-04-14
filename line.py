def line():
	A = float(input("ingrese el coeficiente A:"))
	B = float(input("ingrese el coeficiente B:"))
	X1 = float(input("ingrese el coeficiente X1:"))
	X2 = float(input("ingrese el coeficiente X2:"))
	print(f"El coeficinete A de su ecuación de la recta es: {A}")
	print(f"El coeficinete A de su ecuación de la recta es: {B}")
	print(f"El coeficinete A de su ecuación de la recta es: {X1}")
	print(f"El coeficinete A de su ecuación de la recta es: {X2}")
	print("\n")
	print ("Para la siguinete ecuación:")
	print(f"\t y= {A}X + {B}")
	print("\n")
	print (f"Dados los siguientes puntos:")
	Y1= A*X1+B
	Y2= A*X2+B
	print (f"\tP1({X1}, {Y1})")
	print (f"\tP2({X2}, {Y2})")
	print ("\n")
	distancia = ((X1-X2)**2+(Y1-Y2)**2)**(1/2)
	print(f"La distancia entre ellos es:{distancia}")

	año = int(input('Ingrese un año: '))
	If ((año % 4 == 0) and (año % 100 != 0)):
		print(f'El año {año} es bisiesto') or ((año % 4 == 0) and (año % 400 == 0))
	else: 
		print(f'el año {año} no es bisiesto')
