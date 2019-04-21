class heap:

	def __init__(self):
		self.__content = []

	def __smaller(self, index):
		if 2 * index + 1 < len(self.__content):
			smaller = 2 * index + 1
			if 2 * index + 2 < len(self.__content) and self.__content[2 * index + 2] < self.__content[smaller]:
				smaller = 2 * index + 2
			return smaller
		else:
			return None

	def __percolate_up(self, index):
		while index > 0 and self.__content[index] < self.__content[(index - 1) // 2]:
			temp = self.__content[index]
			self.__content[index] = self.__content[(index - 1) // 2]
			self.__content[(index - 1) // 2] = temp
			index = (index - 1) // 2

	def __percolate_down(self, index):
		while self.__smaller(index) is not None and self.__content[index] > self.__content[self.__smaller(index)]:
			smaller = self.__smaller(index)
			temp = self.__content[index]
			self.__content[index] = self.__content[smaller]
			self.__content[smaller] = temp
			index = smaller

	def insert_element(self, value):
		self.__content.append(value)
		self.__percolate_up(len(self.__content) - 1)

	def remove(self):
		if len(self.__content) == 0:
			return
		to_return = self.__content[0]
		self.__content[0] = self.__content[len(self.__content) - 1]
		self.__content.pop()
		self.__percolate_down(0)
		return to_return

	def __len__(self):
		return len(self.__content)

	def __str__(self):
		return str(self.__content)

if __name__ == '__main__':
	test = heap()
	for k in range(6, 0, -1):
		test.insert_element(k)
	test.remove()
	print(test)