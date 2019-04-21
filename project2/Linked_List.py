class Linked_List:
	
	class __Node:
		
		def __init__(self, val):
			# declare and initialize the private attributes
			# for objects of the Node class.
			self.element = val
			self.prev = None
			self.next = None

	def __init__(self):
		# declare and initialize the private attributes
		# for objects of the sentineled Linked_List class
		self.__header = self.__Node(None)
		self.__trailer = self.__Node(None)
		self.__header.next = self.__trailer
		self.__trailer.prev = self.__header
		self.__size = 0

	def __len__(self):
		# return the number of value-containing nodes in 
		# this list.
		return self.__size

	def __locate_index(self, index):
		if index <= self.__size // 2:
			current_node = self.__header.next
			for k in range(index):
				current_node = current_node.next
			return current_node
		else:
			current_node = self.__trailer.prev
			for k in range(self.__size - 1 - index, 0, -1):
				current_node = current_node.prev
			return current_node

	def append_element(self, val):
		# increase the size of the list by one, and add a
		# node containing val at the new tail position. this 
		# is the only way to add items at the tail position.
		new_node = self.__Node(val)
		new_node.prev = self.__trailer.prev
		new_node.next = self.__trailer
		self.__trailer.prev.next = new_node
		self.__trailer.prev = new_node
		self.__size = self.__size + 1

	def insert_element_at(self, val, index):
		# assuming the head position (not the header node)
		# is indexed 0, add a node containing val at the 
		# specified index. If the index is not a valid 
		# position within the list, raise an IndexError 
		# exception. This method cannot be used to add an 
		# item at the tail position.
		if index < 0 or index >= self.__size:
			raise IndexError
		current_node = self.__locate_index(index)
		predecessor = current_node.prev
		new_node = self.__Node(val)
		new_node.prev = predecessor
		new_node.next =current_node
		predecessor.next = new_node
		current_node.prev = new_node
		self.__size = self.__size + 1


	def remove_element_at(self, index):
		# assuming the head position (not the header node)
		# is indexed 0, remove and return the value stored 
		# in the node at the specified index. If the index 
		# is invalid, raise an IndexError exception.
		if index < 0 or index >= self.__size:
			raise IndexError
		current_node = self.__locate_index(index)	
		predecessor = current_node.prev
		successer = current_node.next
		predecessor.next = successer
		successer.prev = predecessor

		value = current_node.element
		current_node.element = None; current_node.prev = None; current_node.next = None
		self.__size = self.__size - 1
		return value
	
	def get_element_at(self, index):
		# assuming the head position (not the header node)
		# is indexed 0, return the value stored in the node 
		# at the specified index, but do not unlink it from 
		# the list. If the specified index is invalid, raise 
		# an IndexError exception.
		if index < 0 or index >= self.__size:
			raise IndexError
		current_node = self.__locate_index(index)
		return current_node.element

	def rotate_left(self):
		# rotate the list left one position. Conceptual indices
		# should all decrease by one, except for the head, which
		# should become the tail. For example, if the list is
		# [ 5, 7, 9, -4 ], this method should alter it to
		# [ 7, 9, -4, 5 ]. This method should modify the list in
		# place and must not return a value.
		if self.__size == 0:
			return
		else:	
			rotated_element = self.remove_element_at(0)
			self.append_element(rotated_element)

		
	def __str__(self):
		# return a string representation of the list's
		# contents. An empty list should appear as [ ].
		# A list with one element should appear as [ 5 ].
		# A list with two elements should appear as [ 5, 7 ].
		# You may assume that the values stored inside of the
		# node objects implement the __str__() method, so you
		# call str(val_object) on them to get their string
		# representations.
		if self.__size == 0:
			return '[ ]'
		else:
			result = '[ '
			current_node = self.__header.next
			while current_node.next is not self.__trailer:
				result = result + str(current_node.element) + ', '
				current_node = current_node.next
			result = result + str(current_node.element) + ' ]'
		return result


	def __iter__(self):
		# initialize a new attribute for walking through your list
		# TODO insert your initialization code before the return
		# statement. do not modify the return statement.
		self.__iter_node = self.__header.next
		return self

	def __next__(self):
		# using the attribute that you initialized in __iter__(),
		# fetch the next value and return it. If there are no more 
		# values to fetch, raise a StopIteration exception.
		if self.__iter_node is self.__trailer:
			raise StopIteration
		else:
			to_return = self.__iter_node.element
			self.__iter_node = self.__iter_node.next
			return to_return

if __name__ == '__main__':
	# Your test code should go here. Be sure to look at cases
	# when the list is empty, when it has one element, and when 
	# it has several elements. Do the indexed methods raise exceptions
	# when given invalid indices? Do they position items
	# correctly when given valid indices? Does the string
	# representation of your list conform to the specified format?
	# Does removing an element function correctly regardless of that
	# element's location? Does a for loop iterate through your list
	# from head to tail? Your writeup should explain why you chose the
	# test cases. Leave all test cases in your code when submitting.
		test_list = Linked_List()
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')
		
		#test append_element_at() method
		#should all work fine
		print()
		print('testing append')
		test_list.append_element(3)
		test_list.append_element(10)
		test_list.append_element(-9)
		test_list.append_element(None) 
		test_list.append_element(0)
		test_list.append_element('CSCI241')
		#a linked list can have '0' and 'None' 
		#without intefering with its methods.
		print(test_list)
		print('test_list has '+ str(len(test_list)) + ' elements')
		print()

		#test insert_element_at() method
		print()
		print('testing insert')
		try:
		#valid index. should work fine.
			test_list.insert_element_at(3,0)
			test_list.insert_element_at(0,3)
			#linked_list can have the same elements in different nodes
			test_list.insert_element_at(23,2)
			test_list.insert_element_at(None, len(test_list)-1)
		except IndexError:
			print('Error: Invalid Index')
		print(test_list)
		print('test_list has '+ str(len(test_list)) + ' elements')

		empty_list = Linked_List()
		try:
		#invalid index. should fail
			empty_list.insert_element_at(35,0)
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(empty_list)
		print('empty_list has '+ str(len(empty_list)) + ' elements')

		try:
		#invalid index. should fail.
			test_list.insert_element_at(30,-1)
			#cannot have negative index
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(test_list)
		print('test_list has '+ str(len(test_list)) + ' elements')

		try:
		#invalid index. should fail.
			test_list.insert_element_at(24,len(test_list))
			#len(linked_list) is not a valid index. use append
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(test_list)
		print('test_list has '+ str(len(test_list)) + ' elements')
		print()

		#test iterator
		print()
		print('testing iterator')
		for element in test_list:
			print(element)
		print()

		#test remove_element_at() method
		print()
		print('testing remove')
		try:
		#should all work fine
			print(test_list.remove_element_at(0))
			print(test_list.remove_element_at(3))
			print(test_list.remove_element_at(len(test_list)-1))
		except IndexError:
			print('Error: Invalid Index')
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')

		try:
		#should fail and print '[]', list is empty
			empty_list.remove_element_at(0)
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(empty_list)
		print('emptye_list has '+ str(len(empty_list)) + ' elements')

		try:
		#invalid index. should fail
			test_list.remove_element_at(-1)
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')

		try:
		#invalid index. should fail
			test_list.remove_element_at(len(test_list))
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')
		print()

		#test get_element_at() method
		print()
		print('testing get_element')
		try:
		#should all work fine
			for index in range(0,len(test_list)):
				print(test_list.get_element_at(index))
		except IndexError:
			print('Error: Invalid Index')
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')
		#should not change the list

		try:
		#invalid index. should fail. empty list
			print(empty_list.get_element_at(0))
		except IndexError:
			print('Succesfully Detected: Invalid Index')
		print(empty_list)
		print('empty_list has ' + str(len(empty_list)) + ' elements')

		try:
		#invalid index. should fail
			print(test_list.get_element_at(-1))
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')

		try:
		#invalid index. should fail
			print(test_list.get_element_at(len(test_list)))
		except IndexError:
			print('Successfully Detected: Invalid Index')
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')
		print()

		#test rotate_left() method
		print()
		print('testing rotate')
		#should work fine
		test_list.rotate_left()
		print(test_list)
		print('test_list has '  + str(len(test_list))  + ' elements')

		#should have no effect
		empty_list.rotate_left()
		print(empty_list)
		print('empty_list has '  + str(len(empty_list))  + ' elements')


