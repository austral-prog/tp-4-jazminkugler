def leap_year():
año = int(input('Ingrese un año: '))
If ((año % 4 == 0) and (año % 100 != 0)):
	print(f'El año {año} es bisiesto') or ((año % 4 == 0) and (año % 400 == 0))
else: 
	print(f'el año {año} no es bisiesto')

	
