import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):

	#test cases are built through three dimensions:
	#Through the x-axis, cases are built to test the functionality of update methods, insert and remove (Error)
	#Through the y-axis, the testing of functionality is constructed in terms of in_order, pre_order, post_order and height
	#Through the z-axis, the size of the tested tree are increasing from empty to 4.

	def setUp(self):
		self.__bst = Binary_Search_Tree()

	#Four element of empty tree
	def test_empty_tree_string_inorder(self):
		#test the in_order format of an empty tree
		self.assertEqual('[ ]', str(self.__bst))

	def test_empty_tree_preorder(self):
		self.assertEqual('[ ]', self.__bst.pre_order())

	def test_empty_tree_post_order(self):
		self.assertEqual('[ ]', self.__bst.post_order())

	def test_empty_tree_height(self):
		self.assertEqual(0, self.__bst.get_height())

	#Four element of one_element tree
	def test_insert_one_inorder(self):
		self.__bst.insert_element(5)
		self.assertEqual('[ 5 ]', str(self.__bst))

	def test_insert_one_preorder(self):
		self.__bst.insert_element(5)
		self.assertEqual('[ 5 ]', self.__bst.pre_order())

	def test_insert_one_postorder(self):
		self.__bst.insert_element(5)
		self.assertEqual('[ 5 ]', self.__bst.post_order())

	def test_insert_one_height(self):
		self.__bst.insert_element(5)
		self.assertEqual(1, self.__bst.get_height())

	#Four element of two_element tree, with possibility of ValueError
	def test_insert_two_left_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.assertEqual('[ 3, 5 ]', str(self.__bst))

	def test_insert_two_left_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.assertEqual('[ 5, 3 ]', self.__bst.pre_order())

	def test_insert_two_left_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.assertEqual('[ 3, 5 ]', self.__bst.post_order())

	def test_insert_two_left_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.assertEqual(2, self.__bst.get_height())

	def test_insert_two_right_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.assertEqual('[ 5, 8 ]', str(self.__bst))

	def test_insert_two_right_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.assertEqual('[ 5, 8 ]', self.__bst.pre_order())

	def test_insert_two_right_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.assertEqual('[ 8, 5 ]', self.__bst.post_order())

	def test_insert_two_right_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.assertEqual(2, self.__bst.get_height())

	def test_insert_two_error_inorder(self):
		#should be ValueError, value exists
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(5)
		self.assertEqual('[ 5 ]', str(self.__bst))

	def test_insert_two_error_preorder(self):
		#should be ValueError, value exists
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(5)
		self.assertEqual('[ 5 ]', self.__bst.pre_order())

	def test_insert_two_error_postorder(self):
		#should be ValueError, value exists
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(5)
		self.assertEqual('[ 5 ]', self.__bst.post_order())

	def test_insert_two_error_height(self):
		#should be ValueError, value exists
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(5)
		self.assertEqual(1, self.__bst.get_height())

	#Four element of three_element tree with possibility of error
	#Test the insert works fine with a perfect tree with three element
	def test_insert_three_height_two_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.assertEqual('[ 3, 5, 8 ]', str(self.__bst))

	def test_insert_three_height_two_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.assertEqual('[ 5, 3, 8 ]', self.__bst.pre_order())

	def test_insert_three_height_two_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.assertEqual('[ 3, 8, 5 ]', self.__bst.post_order())

	def test_insert_three_height_two_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.assertEqual(2, self.__bst.get_height())

	#Test that the insert works fine when the tree acts like a linked list
	def test_insert_three_height_three_left_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual('[ 2, 3, 5 ]', str(self.__bst))

	def test_insert_three_height_three_left_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual('[ 5, 3, 2 ]', self.__bst.pre_order())

	def test_insert_three_height_three_left_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual('[ 2, 3, 5 ]', self.__bst.post_order())

	def test_insert_three_height_three_left_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual(3, self.__bst.get_height())

	def test_insert_three_height_three_right_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(7)
		self.__bst.insert_element(9)
		self.assertEqual('[ 5, 7, 9 ]', str(self.__bst))

	def test_insert_three_height_three_right_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(7)
		self.__bst.insert_element(9)
		self.assertEqual('[ 5, 7, 9 ]', self.__bst.pre_order())

	def test_insert_three_height_three_right_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(7)
		self.__bst.insert_element(9)
		self.assertEqual('[ 9, 7, 5 ]', self.__bst.post_order())

	def test_insert_three_height_three_left_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(7)
		self.__bst.insert_element(9)
		self.assertEqual(3, self.__bst.get_height())

	#Test that the insert works fine with a tree that goes left then right
	def test_insert_three_height_three_left_right_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		self.assertEqual('[ 3, 4, 5 ]', str(self.__bst))

	def test_insert_three_height_three_left_right_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		self.assertEqual('[ 5, 3, 4 ]', self.__bst.pre_order())

	def test_insert_three_height_three_left_right_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		self.assertEqual('[ 4, 3, 5 ]', self.__bst.post_order())

	def test_insert_three_height_three_left_right_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		self.assertEqual(3, self.__bst.get_height())

	#Test the cases of error
	def test_insert_three_error_inroder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual('[ 3, 5 ]', str(self.__bst))

	def test_insert_three_error_preroder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual('[ 5, 3 ]', self.__bst.pre_order())

	def test_insert_three_error_postroder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual('[ 3, 5 ]', self.__bst.post_order())

	def test_insert_three_error_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual(2, self.__bst.get_height())

	#Test the four element updated by insert with a four-element tree
	def test_insert_four_height_three_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(2)
		self.assertEqual('[ 2, 3, 5, 8 ]', str(self.__bst))

	def test_insert_four_height_three_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(2)
		self.assertEqual('[ 5, 3, 2, 8 ]', self.__bst.pre_order())

	def test_insert_four_height_three_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(2)
		self.assertEqual('[ 2, 3, 8, 5 ]', self.__bst.post_order())

	def test_insert_four_height_three_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(2)
		self.assertEqual(3, self.__bst.get_height())

	def test_insert_four_height_four_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.assertEqual('[ 2, 3, 4, 5 ]', str(self.__bst))

	def test_insert_four_height_four_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.assertEqual('[ 5, 2, 4, 3 ]', self.__bst.pre_order())

	def test_insert_four_height_four_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.assertEqual('[ 3, 4, 2, 5 ]', self.__bst.post_order())

	def test_insert_four_height_four_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.assertEqual(4, self.__bst.get_height())

	def test_insert_four_left_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual('[ 2, 3, 4, 5 ]', str(self.__bst))

	def test_insert_four_left_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual('[ 5, 4, 3, 2 ]', self.__bst.pre_order())

	def test_insert_four_left_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual('[ 2, 3, 4, 5 ]', self.__bst.post_order())

	def test_insert_four_left_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.assertEqual(4, self.__bst.get_height())

	def test_insert_four_error_height_two_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual('[ 3, 5, 8 ]', str(self.__bst))

	def test_insert_four_error_height_two_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(8)
		self.assertEqual('[ 5, 3, 8 ]', self.__bst.pre_order())

	def test_insert_four_error_height_two_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(5)
		self.assertEqual('[ 3, 8, 5 ]', self.__bst.post_order())

	def test_insert_four_error_height_two_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual(2, self.__bst.get_height())

	def test_insert_four_error_height_three_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual('[ 3, 4, 5 ]', str(self.__bst))

	def test_insert_four_error_height_three_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(4)
		self.assertEqual('[ 5, 3, 4 ]', self.__bst.pre_order())

	def test_insert_four_error_height_three_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(5)
		self.assertEqual('[ 4, 3, 5 ]', self.__bst.post_order())

	def test_insert_four_error_height_three_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(3)
		self.assertEqual(3, self.__bst.get_height())

	#Test Remove
	#Test remove on an empty tree
	def test_remove_empty_inorder(self):
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual('[ ]', str(self.__bst))

	def test_remove_empty_preorder(self):
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual('[ ]', self.__bst.pre_order())

	def test_remove_empty_postorder(self):
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual('[ ]', self.__bst.post_order())

	def test_remove_empty_height(self):
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual(0, self.__bst.get_height())

	#Test remove on an one-element tree
	def test_remove_leaving_empty_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.remove_element(5)
		self.assertEqual('[ ]', str(self.__bst))

	def test_remove_leaving_empty_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.remove_element(5)
		self.assertEqual('[ ]', self.__bst.pre_order())

	def test_remove_leaving_empty_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.remove_element(5)
		self.assertEqual('[ ]', self.__bst.post_order())

	def test_remove_leaving_empty_height(self):
		self.__bst.insert_element(5)
		self.__bst.remove_element(5)
		self.assertEqual(0, self.__bst.get_height())

	def test_remove_one_error_inorder(self):
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(3)
		self.assertEqual('[ 5 ]', str(self.__bst))

	def test_remove_one_error_preorder(self):
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(3)
		self.assertEqual('[ 5 ]', self.__bst.pre_order())

	def test_remove_one_error_postorder(self):
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(3)
		self.assertEqual('[ 5 ]', self.__bst.post_order())

	def test_remove_one_error_height(self):
		self.__bst.insert_element(5)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(3)
		self.assertEqual(1, self.__bst.get_height())

	#Test remove on a two-element tree
	def test_remove_leaf_leaving_one_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(8)
		self.assertEqual('[ 5 ]', str(self.__bst))

	def test_remove_leaf_leaving_one_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(8)
		self.assertEqual('[ 5 ]', self.__bst.pre_order())

	def test_remove_leaf_leaving_one_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(8)
		self.assertEqual('[ 5 ]', self.__bst.post_order())

	def test_remove_leaf_leaving_one_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(8)
		self.assertEqual(1, self.__bst.get_height())

	def test_remove_root_leaving_one_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual('[ 8 ]', str(self.__bst))
	
	def test_remove_root_leaving_one_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual('[ 8 ]', self.__bst.pre_order())

	def test_remove_root_leaving_one_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual('[ 8 ]', self.__bst.post_order())

	def test_remove_root_leaving_one_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual(1, self.__bst.get_height())

	def test_remove_two_error_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(12)
		self.assertEqual('[ 5, 8 ]', str(self.__bst))

	def test_remove_two_error_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(12)
		self.assertEqual('[ 5, 8 ]', self.__bst.pre_order())

	def test_remove_two_error_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(12)
		self.assertEqual('[ 8, 5 ]', self.__bst.post_order())

	def test_remove_two_error_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(12)
		self.assertEqual(2, self.__bst.get_height())

	#Test remove on a three-element tree
	def test_remove_root_leaving_two_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual('[ 3, 8 ]', str(self.__bst))
	
	def test_remove_root_leaving_two_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual('[ 8, 3 ]', self.__bst.pre_order())

	def test_remove_root_leaving_two_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual('[ 3, 8 ]', self.__bst.post_order())
	
	def test_remove_root_leaving_two_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(5)
		self.assertEqual(2, self.__bst.get_height())

	def test_remove_leaf_leaving_two_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(3)
		self.assertEqual('[ 5, 8 ]', str(self.__bst))

	def test_remove_leaf_leaving_two_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(3)
		self.assertEqual('[ 5, 8 ]', self.__bst.pre_order())

	def test_remove_leaf_leaving_two_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(3)
		self.assertEqual('[ 8, 5 ]', self.__bst.post_order())

	def test_remove_leaf_leaving_two_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.remove_element(3)
		self.assertEqual(2, self.__bst.get_height())

	def test_remove_three_error_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual('[ 3, 5, 8 ]', str(self.__bst))

	def test_remove_three_error_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual('[ 5, 3, 8 ]', self.__bst.pre_order())

	def test_remove_three_error_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual('[ 3, 8, 5 ]', self.__bst.post_order())

	def test_remove_three_error_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(4)
		self.assertEqual(2, self.__bst.get_height())

	#Test remove on a four-element tree
	def test_remove_leaf_leaving_three_height_two_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(16)
		self.assertEqual('[ 3, 5, 8 ]', str(self.__bst))

	def test_remove_leaf_leaving_three_height_two_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(16)
		self.assertEqual('[ 5, 3, 8 ]', self.__bst.pre_order())

	def test_remove_leaf_leaving_three_height_two_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(16)
		self.assertEqual('[ 3, 8, 5 ]', self.__bst.post_order())

	def test_remove_leaf_leaving_three_height_two_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(16)
		self.assertEqual(2, self.__bst.get_height())

	def test_remove_inner_leaving_three_height_two_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(8)
		self.assertEqual('[ 3, 5, 16 ]', str(self.__bst))

	def test_remove_inner_leaving_three_height_two_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(8)
		self.assertEqual('[ 5, 3, 16 ]', self.__bst.pre_order())

	def test_remove_inner_leaving_three_height_two_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(8)
		self.assertEqual('[ 3, 16, 5 ]', self.__bst.post_order())

	def test_remove_inner_leaving_three_height_two_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(8)
		self.assertEqual(2, self.__bst.get_height())

	def test_remove_root_leaving_three_height_two_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(5)
		self.assertEqual('[ 3, 8, 16 ]', str(self.__bst))

	def test_remove_root_leaving_three_height_two_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(5)
		self.assertEqual('[ 8, 3, 16 ]', self.__bst.pre_order())

	def test_remove_root_leaving_three_height_two_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(5)
		self.assertEqual('[ 3, 16, 8 ]', self.__bst.post_order())

	def test_remove_root_leaving_three_height_two_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(16)
		self.__bst.remove_element(5)
		self.assertEqual(2, self.__bst.get_height())

	def test_remove_leaf_leaving_three_height_three_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.remove_element(2)
		self.assertEqual('[ 3, 4, 5 ]', str(self.__bst))

	def test_remove_leaf_leaving_three_height_three_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.remove_element(2)
		self.assertEqual('[ 5, 4, 3 ]', self.__bst.pre_order())

	def test_remove_leaf_leaving_three_height_three_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.remove_element(2)
		self.assertEqual('[ 3, 4, 5 ]', self.__bst.post_order())

	def test_remove_leaf_leaving_three_height_three_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(4)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.remove_element(2)
		self.assertEqual(3, self.__bst.get_height())

	def test_remove_inner_leaving_three_height_three_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.remove_element(3)
		self.assertEqual('[ 2, 4, 5 ]', str(self.__bst))

	def test_remove_inner_leaving_three_height_three_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.remove_element(3)
		self.assertEqual('[ 5, 4, 2 ]', self.__bst.pre_order())

	def test_remove_inner_leaving_three_height_three_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.remove_element(3)
		self.assertEqual('[ 2, 4, 5 ]', self.__bst.post_order())

	def test_remove_inner_leaving_three_height_three_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		self.__bst.remove_element(3)
		self.assertEqual(3, self.__bst.get_height())

	def test_remove_four_error_height_three_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(8)
		self.assertEqual('[ 2, 3, 4, 5 ]', str(self.__bst))

	def test_remove_four_error_height_three_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(8)
		self.assertEqual('[ 5, 3, 2, 4 ]', self.__bst.pre_order())

	def test_remove_four_error_height_three_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(8)
		self.assertEqual('[ 2, 4, 3, 5 ]', self.__bst.post_order())

	def test_remove_four_error_height_three_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(2)
		self.__bst.insert_element(4)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(8)
		self.assertEqual(3, self.__bst.get_height())

	def test_remove_root_leaving_four_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(10)
		self.__bst.remove_element(5)
		self.assertEqual('[ 3, 6, 8, 10 ]', str(self.__bst))

	def test_remove_root_leaving_four_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(10)
		self.__bst.remove_element(5)
		self.assertEqual('[ 6, 3, 8, 10 ]', self.__bst.pre_order())

	def test_remove_root_leaving_four_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(10)
		self.__bst.remove_element(5)
		self.assertEqual('[ 3, 10, 8, 6 ]', self.__bst.post_order())

	def test_remove_root_leaving_four_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(10)
		self.__bst.remove_element(5)
		self.assertEqual(3, self.__bst.get_height())

	def test_remove_inner_leaving_four_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(6)
		self.assertEqual('[ 3, 5, 7, 8 ]', str(self.__bst))

	def test_remove_inner_leaving_four_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(6)
		self.assertEqual('[ 5, 3, 8, 7 ]', self.__bst.pre_order())

	def test_remove_inner_leaving_four_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(6)
		self.assertEqual('[ 3, 7, 8, 5 ]', self.__bst.post_order())

	def test_remove_inner_leaving_four_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(6)
		self.assertEqual(3, self.__bst.get_height())

	def test_remove_leaf_leaving_four_inorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(7)
		self.assertEqual('[ 3, 5, 6, 8 ]', str(self.__bst))

	def test_remove_leaf_leaving_four_preorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(7)
		self.assertEqual('[ 5, 3, 8, 6 ]', self.__bst.pre_order())

	def test_remove_leaf_leaving_four_postorder(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(7)
		self.assertEqual('[ 3, 6, 8, 5 ]', self.__bst.post_order())

	def test_remove_leaf_leaving_four_height(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(8)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.__bst.remove_element(7)
		self.assertEqual(3, self.__bst.get_height())




if __name__ == '__main__':
	unittest.main()