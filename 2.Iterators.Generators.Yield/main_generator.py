# Генератор, который принимает список списков, и возвращает их плоское представление
# Обрабатывает списки с любым уровнем вложенности


def flat_generator(nested_list: list):
	flatten_list = []
	def _flat_list(elem):
		if(type(elem) == list):
			for e in elem:
				_flat_list(e)
		else:
			flatten_list.append(elem)
			return elem

	_flat_list(nested_list)
	for elem in flatten_list:
		yield elem


def main():
	nested_list = [
		['a', ['b', 'b2', ['b31','b32']], 'c'],
		['d', 'e', 'f', 'h', {'aa':12,'b':23}, False],
		[1, 2, None],
	]

	for item in flat_generator(nested_list):
		print(f'{item}') #  

	flat_list = [item for item in flat_generator(nested_list)]
	print(flat_list)


if __name__ == '__main__':
	main()
