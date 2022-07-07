

nested_list = [
	['a', ['b', 'b2'], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator(object):
	"""docstring for FlatIterator"""
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
			return 
		else:
			self.flatten_list.append(elem)
			return elem



flatter = FlatIterator(nested_list)
for item in flatter:
	print(f'{item}') #  

flat_list = [item for item in flatter]
print(flat_list)