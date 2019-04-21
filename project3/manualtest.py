from Array_Deque import Array_Deque
from Stack import Stack

if __name__ == '__main__':
	print('testing deque')
	test_deque = Array_Deque()
	print(test_deque)
	print('deqeue has ' + str(len(test_deque)) + ' elements')

	test_deque.push_front(1)
	test_deque.push_front(3)
	test_deque.push_front(5)
	print(test_deque)
	print('deqeue has ' + str(len(test_deque)) + ' elements')

	print(test_deque.pop_front())
	print(test_deque.pop_front())
	print(test_deque.pop_front())
	print(test_deque)
	print('deqeue has ' + str(len(test_deque)) + ' elements')

	test_deque.push_back(12)
	test_deque.push_back(24)
	print(test_deque)
	print('deqeue has ' + str(len(test_deque)) + ' elements')

	test_deque.push_back(212)
	test_deque.push_back(111)
	test_deque.push_back(' ')
	print(test_deque)
	print('deqeue has ' + str(len(test_deque)) + ' elements')
	print()

	print('testing stack')
	test_stack = Stack()
	print(test_stack)
	print('test_stack has ' + str(len(test_stack)) + ' elements')

	test_stack.push(1)
	test_stack.push(3)
	test_stack.push(21)
	print(test_stack)
	print('test_stack has ' + str(len(test_stack)) + ' elements')

	print(test_stack.pop())
	print(test_stack)
	print('test_stack has ' + str(len(test_stack)) + ' elements')

	print(test_stack.peek())
