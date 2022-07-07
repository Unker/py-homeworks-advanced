



class FlatIterator(object):
	""" 
	*Итератор обрабатывающий списки с любым уровнем вложенности
	Возвращает плоское представление списков
	"""
	def __init__(self, nested_list: list):
		super(FlatIterator, self).__init__()
		self.nested_list = nested_list
		self.flatten_list = []
		self._flat_list(self.nested_list)


	def __iter__(self):
		self.start = 0
		self.end = len(self.flatten_list)
		return self


	def __next__(self):
		if self.start < self.end:
			self.start += 1
			return self.flatten_list[self.start-1]
		else:
			raise StopIteration


	def _flat_list(self, elem):
		if(type(elem) == list):
			for e in elem:
				self._flat_list(e)
		else:
			self.flatten_list.append(elem)
			return elem


def main():
	nested_list = [
		['a', ['b', 'b2'], 'c'],
		['d', 'e', 'f', 'h', {'aa':12,'b':23}, False],
		[1, 2, None],
	]

	flatter = FlatIterator(nested_list)
	for item in flatter:
		print(f'{item}') #  

	flat_list = [item for item in flatter]
	print(flat_list)


if __name__ == '__main__':
	main()
