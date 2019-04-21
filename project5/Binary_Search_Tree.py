class Binary_Search_Tree:

	class __BST_Node:
		__slots__ = 'value', 'left', 'right', 'height'
		def __init__(self, value):
			self.value = value
			self.left = None
			self.right = None
			self.height = 1

		def update_height(self):
		#update the node's height by adding one to the bigger height of its children if both are not None
		#if left is None, right is not None, then add one to the right's height
		#if right is None, left is not None, then add one to the left's height
		#if both are None, do nothing.
			if self.left is None and self.right is not None:
				self.height = self.right.height + 1
			elif self.right is None and self.left is not None:
				self.height = self.left.height + 1
			elif self.right is not None and self.left is not None:
				if self.right.height > self.left.height:
					self.height = self.right.height + 1
				else:
					self.height = self.left.height + 1
			else:
				self.height = 1

	def __init__(self):
		self.__root = None

	def insert_element(self, value):
		# Insert the value specified into the tree at the correct
		# location based on "less is left; greater is right" binary
		# search tree ordering. If the value is already contained in
		# the tree, raise a ValueError. Your solution must be recursive.
		# This will involve the introduction of additional private
		# methods to support the recursion control variable.
			self.__root = self.__recursive_insert(value, self.__root)  #might raise an error

	def __recursive_insert(self, value, node):
		if node is None:
			return self.__BST_Node(value)  #base case, return a newly created node
		elif value == node.value:
			raise ValueError('Value Exist')
		elif value < node.value:
			node.left = self.__recursive_insert(value, node.left)  #update the left subtree to insert the value
			node.update_height()
			return self.__balance(node)
		else:
			node.right = self.__recursive_insert(value, node.right)  #update the right subtree to insert the value
			node.update_height()
			return self.__balance(node)

	def remove_element(self, value):
		# Remove the value specified from the tree, raising a ValueError
		# if the value isn't found. When a replacement value is necessary,
		# select the minimum value to the from the right as this element's
		# replacement. Take note of when to move a node reference and when
		# to replace the value in a node instead. It is not necessary to
		# return the value (though it would reasonable to do so in some 
		# implementations). Your solution must be recursive. 
		# This will involve the introduction of additional private
		# methods to support the recursion control variable.
			self.__root = self.__recursive_remove(value, self.__root)

	def __recursive_remove(self, value, node):
		if node is None:
			raise ValueError('Value does not exist')
		elif value > node.value:
			node.right = self.__recursive_remove(value, node.right)
			node.update_height()
			return self.__balance(node)
		elif value < node.value:
			node.left = self.__recursive_remove(value, node.left)
			node.update_height()
			return self.__balance(node)
		else:  #find the node, begin removing
			if node.left is None and node.right is None:
				return None
			elif node.left is not None and node.right is None:
				return node.left
			elif node.left is None and node.right is not None:
				return node.right
			else:
				current_node = node.right  #locating the leftmost node in the right subtree
				while current_node.left is not None:
					current_node = current_node.left
				node.value = current_node.value
				node.right = self.__recursive_remove(current_node.value, node.right) #delete the current_node whose value has been duplicated
				node.update_height()
				return self.__balance(node)

	def __balance(self, node):
		#return the subtree rooted at node after balancin
		if self.__compute_balance(node) == 0 or self.__compute_balance(node) == 1 or self.__compute_balance(node) == -1: 
		#balanced, return node
			return node
		elif self.__compute_balance(node) == 2:
			#right imbalance by 2
			if self.__compute_balance(node.right) == 1 or self.__compute_balance(node.right) == 0:
			#right child also right imbalanced or blanced, rotate once
				return self.__rotate_left(node)
			else:
			#right child left imbalanced, double rotate
				node.right = self.__rotate_right(node.right)
				return self.__rotate_left(node)
		else:
			#left imbalance by 2
			if self.__compute_balance(node.left) == -1 or self.__compute_balance(node.left) == 0:
			#left child also left imabalnced or balanced, rotate once
				return self.__rotate_right(node)
			else:
			#left child right imbalanced, double rotate
				node.left = self.__rotate_left(node.left)
				return self.__rotate_right(node)

	def __compute_balance(self, node):
		#return the balance of a given node by subtracting height of its left child from its right child.
		#left/right height is 0 is left/right child is None
		if node.left is None:
			height_left = 0
		else:
			height_left = node.left.height
		if node.right is None:
			height_right = 0
		else:
			height_right = node.right.height
		return height_right - height_left

	def __rotate_left(self, node):
		#rotate left, making the right child the new subroot
		#float the left child of right child to be the right child of the old subroot
		new_subroot = node.right
		floater = new_subroot.left
		new_subroot.left = node
		new_subroot.left.right = floater
		new_subroot.left.update_height()
		new_subroot.update_height()
		return new_subroot

	def __rotate_right(self, node):
		#rotate right, making the left child the new subroot
		#float the right child of left child to be the left child of the old subroot
		new_subroot = node.left
		floater = new_subroot.right
		new_subroot.right = node
		new_subroot.right.left = floater
		new_subroot.right.update_height()
		new_subroot.update_height()
		return new_subroot

	def in_order(self):
		# Construct and return a string representing the in-order
		# traversal of the tree. Empty trees should be printed as [ ].
		# Trees with one value should be printed as [ 4 ]. Trees with more
		# than one value should be printed as [ 4, 7 ]. Note the spacing.
		# Your solution must be recursive. This will involve the introduction
		# of additional private methods to support the recursion control 
		# variable.
		if self.__root is None:
			result = '[ ]'
		else:
			result = '[ '
			result = result + self.__recursive_inorder(self.__root)[:-2]
			result = result + ' ]'
		return result

	def __recursive_inorder(self, node):
		result = ''
		if node.left is not None:
			result = result + self.__recursive_inorder(node.left)
		result = result + str(node.value) + ', '
		if node.right is not None:
			result = result + self.__recursive_inorder(node.right)
		return result

	def pre_order(self):
		# Construct and return a string representing the pre-order
		# traversal of the tree. Empty trees should be printed as [ ].
		# Trees with one value should be printed in as [ 4 ]. Trees with
		# more than one value should be printed as [ 4, 7 ]. Note the spacing.
		# Your solution must be recursive. This will involve the introduction
		# of additional private methods to support the recursion control 
		# variable.
		if self.__root is None:
			result = '[ ]'
		else:
			result = '[ '
			result = result + self.__recursive_preorder(self.__root)[:-2]
			result = result + ' ]'
		return result

	def __recursive_preorder(self, node):
		result = ''
		result = result + str(node.value) + ', '
		if node.left is not None:
				result = result + self.__recursive_preorder(node.left)
		if node.right is not None:
				result = result + self.__recursive_preorder(node.right)
		return result

	def post_order(self):
		# Construct an return a string representing the post-order
		# traversal of the tree. Empty trees should be printed as [ ].
		# Trees with one value should be printed in as [ 4 ]. Trees with
		# more than one value should be printed as [ 4, 7 ]. Note the spacing.
		# Your solution must be recursive. This will involve the introduction
		# of additional private methods to support the recursion control 
		# variable.
		if self.__root is None:
			result = '[ ]'
		else:
			result = '[ '
			result = result + self.__recursive_postorder(self.__root)[:-2]
			result = result + ' ]'
		return result

	def __recursive_postorder(self, node):
		result = ''
		if node.left is not None:
				result = result + self.__recursive_postorder(node.left)
		if node.right is not None:
				result = result + self.__recursive_postorder(node.right)
		result = result + str(node.value) + ', '
		return result

	def get_height(self):
		# return an integer that represents the height of the tree.
		# assume that an empty tree has height 0 and a tree with one
		# node has height 1. This method must operate in constant time.
		if self.__root is None:
			return 0
		else:
			return self.__root.height

	def __str__(self):
		return self.in_order()

	def to_list(self):
		# Construct and Reteun a list representing the in-order traversal of the tree.
		return self.__recursive_to_list(self.__root)

	def __recursive_to_list(self, node):
		result = []
		if node.left is not None:
			result = result + self.__recursive_to_list(node.left)
		result = result + [node.value]
		if node.right is not None:
			result = result + self.__recursive_to_list(node.right)
		return result
