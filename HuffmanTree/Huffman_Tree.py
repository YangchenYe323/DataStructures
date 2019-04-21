from Heap import heap
from collections import OrderedDict

def insertion_sort(string):
	#static method to sort the given text in alphabetical order
	str_list = list(string)
	for k in range(1, len(str_list)):
		pivot = str_list[k]
		j = k
		while j > 0 and ord(str_list[j-1]) > ord(pivot):
			str_list[j] = str_list[j-1]
			j -= 1
		str_list[j] = pivot
	return str_list

class Huffman_Tree:
	#prompt the readers for a string,
	#provide the huffman encoding of the string
	#make the reference heap in alphabetical order

	class __Node:
		def __init__(self, value, frequency):
			self.value = value
			self.freq = frequency
			self.left = None
			self.right = None

		def __lt__(self, other):
			return self.freq < other.freq

		def __gt__(self, other):
			return self.freq > other.freq

	def __init__(self, text):
		self.__text = text
		self.__freq_dict = self.__make_frequency_dict(self.__text)
		self.__heap = heap()
		self.__encoding_dict = {}
		self.__decoding_dict = {}

		self.__make_heap(self.__freq_dict)
		self.__huffman_tree_construct()
		self.__recursive_coding(self.__heap.remove(), '')

	def __make_frequency_dict(self, text):
		freq_dict = OrderedDict()
		for char in insertion_sort(text):
			freq_dict[char] = 1 + freq_dict.get(char, 0)
		return freq_dict

	def __make_heap(self, freq_dict):
		for key in freq_dict:
			node = self.__Node(key, freq_dict[key])
			self.__heap.insert_element(node)

	def __huffman_tree_construct(self):
		while len(self.__heap) > 1:
			tree_1 = self.__heap.remove()
			tree_2 = self.__heap.remove()
			new_node = self.__Node(None, tree_1.freq + tree_2.freq)
			new_node.left = tree_1
			new_node.right = tree_2
			self.__heap.insert_element(new_node)

	def __recursive_coding(self, node, current_code):
		if node.value is not None:
			self.__encoding_dict[node.value] = current_code
			self.__decoding_dict[current_code] = node.value
			return
		self.__recursive_coding(node.left, current_code + '0')
		self.__recursive_coding(node.right, current_code + '1')

	def get_encoded_text(self, text):
		encoded_text = ''
		for char in text:
			encoded_text += self.__encoding_dict[char]
		return encoded_text

	def get_decoded_text(self, text):
		current_text = ''
		decoded_text = ''
		for char in text:
			current_text += char
			if current_text in self.__decoding_dict:
				decoded_text += self.__decoding_dict[current_text]
				current_text = ''
		return decoded_text

	def get_encoding_dict(self):
		return self.__encoding_dict

	def get_decoding_dict(self):
		return self.__decoding_dict

if __name__ == '__main__':
	text = input('enter the text to be encoded')
	encoding = Huffman_Tree(text)
	print('The optimal encoding is: ' + encoding.get_encoded_text(text))
	code = input('enter a binary string to be decoded')
	print('The decoded text is: '+ encoding.get_decoded_text(code))