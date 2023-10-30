import random

# Primero comprobamos que todos sean INT, luego creamos el rango en el cual trabajara nuestra funcion.
# Comprobamos si los numeros que queremos entran en el rango, creamos la lista randomizando la lista del rango
# y cuantos numeros queremos. Por ultimo los convertimos en una string uniendo el separador que hayamos puesto
def generate_nums(limit_1, limit_2, numbers_to_show, separator=', '):
	if not (isinstance(limit_1, int) and isinstance(limit_2, int) and isinstance(numbers_to_show, int)):
		print("Error INT: The number is too big or too small ")
		return
	range_n = abs(limit_2 - limit_1) + 1
	if range_n < numbers_to_show:
		print("Error quantity : The difference between the limits must be greater than or equal to the number of numbers to be displayed.")
		return
	if limit_1 < limit_2:
		list_possibilities = list(range(limit_1, limit_2 + 1))
	else:
		list_possibilities = list(range(limit_2, limit_1 + 1))
	list_result = random.sample(list_possibilities, numbers_to_show)
	string_list_pos = [str(num) for num in list_result]
	result = separator.join(string_list_pos)
	print(f"Select numbers : {result}")


# Añadimos a las variables los valores con los que trabajaremos comprobando que el input sea el correcto
try:
	limit_1 = int(input("Please, insert first limit: "))
	limit_2 = int(input("Please, insert second limit: "))
	numbers_to_show = int(input("Please, insert the quantity of numbers to show: "))
except ValueError:
	print("Error parsing : Please, insert valid numbers.")
else:
	separator = input("Enter the separator (default ', '): ") or ', '


# ejecutamos la funcion principal con los parametros seleccionados
generate_nums(limit_1, limit_2, numbers_to_show, separator)
