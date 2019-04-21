import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_
  #testing deque
  def test_empty_deque_string(self):
  	self.assertEqual('[ ]', str(self.__deque)) #an empty deque should be '[ ]'

  def test_push_front_empty(self):
  	self.__deque.push_front('Data')
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_push_front_one(self):
  	self.__deque.push_front('Structure')
  	self.__deque.push_front('Data')
  	self.assertEqual('[ Data, Structure ]', str(self.__deque))

  def test_push_front_two(self):
  	self.__deque.push_front('Structure')
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Love')
  	self.assertEqual('[ Love, Data, Structure ]', str(self.__deque))

  def test_push_back_empty(self):
  	self.__deque.push_back('Data')
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_push_back_one(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structure')
  	self.assertEqual('[ Data, Structure ]', str(self.__deque))

  def test_push_back_two(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structure')
  	self.__deque.push_back('Project')
  	self.assertEqual('[ Data, Structure, Project ]', str(self.__deque))

  def test_front_back(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_back('Structure')
  	self.assertEqual('[ Data, Structure ]', str(self.__deque))

  def test_back_front(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_front('Structure')
  	self.assertEqual('[ Structure, Data ]', str(self.__deque))

  def test_get_empty_length(self):
  	self.assertEqual(0, len(self.__deque))

  def test_get_one_length_front(self):
  	self.__deque.push_front('Yangchen')
  	self.assertEqual(1, len(self.__deque))

  def test_get_two_length_front(self):
  	self.__deque.push_front('Yangchen')
  	self.__deque.push_front('Ye')
  	self.assertEqual(2, len(self.__deque))

  def test_get_one_length_back(self):
  	self.__deque.push_back('Yangchen')
  	self.assertEqual(1, len(self.__deque))

  def test_get_two_length_back(self):
  	self.__deque.push_back('Yangchen')
  	self.__deque.push_back('Ye')
  	self.assertEqual(2, len(self.__deque))

  def test_get_two_length_front_back(self):
  	self.__deque.push_front('Yangchen')
  	self.__deque.push_back('Ye')
  	self.assertEqual(2, len(self.__deque))

  def test_get_two_length_back_front(self):
  	self.__deque.push_back('Ye')
  	self.__deque.push_front('Zhang')
  	self.assertEqual(2, len(self.__deque))

  def test_pop_front_empty_return_value(self):
  	to_return = self.__deque.pop_front()
  	self.assertEqual(None, to_return)

  def test_pop_front_empty_remaining_deque(self):
  	to_return = self.__deque.pop_front()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_empty_length(self):
  	to_return = self.__deque.pop_front()
  	self.assertEqual(0, len(self.__deque))

  def test_pop_front_leaving_empty_return_value(self):
  	self.__deque.push_front('Yangchen')
  	to_return = self.__deque.pop_front()
  	self.assertEqual('Yangchen', to_return)

  def test_pop_front_leaving_empty_remaining_deque(self):
  	self.__deque.push_back('Data')
  	to_return = self.__deque.pop_front()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_leaving_empty_length(self):
  	self.__deque.push_back('Data')
  	to_return = self.__deque.pop_front()
  	self.assertEqual(0, len(self.__deque))

  def test_pop_front_leaving_one_return_value(self):
  	self.__deque.push_front('Yangchen')
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.pop_front()
  	self.assertEqual('Ye', to_return)

  def test_pop_front_leaving_one_remaining_deque(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.pop_front()
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_pop_front_leaving_one_length(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structure')
  	to_return = self.__deque.pop_front()
  	self.assertEqual(1, len(self.__deque))

  def test_pop_back_empty_return_value(self):
  	to_return = self.__deque.pop_back()
  	self.assertEqual(None, to_return)

  def test_pop_back_empty_remaining_deque(self):
  	to_return = self.__deque.pop_back()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_empty_length(self):
  	to_return = self.__deque.pop_back()
  	self.assertEqual(0, len(self.__deque))

  def test_pop_back_leaving_empty_return_value(self):
  	self.__deque.push_front('Yangchen')
  	to_return = self.__deque.pop_back()
  	self.assertEqual('Yangchen', to_return)

  def test_pop_back_leaving_empty_remaining_deque(self):
  	self.__deque.push_back('Data')
  	to_return = self.__deque.pop_back()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_leaving_empty_length(self):
  	self.__deque.push_back('Data')
  	to_return = self.__deque.pop_back()
  	self.assertEqual(0, len(self.__deque))

  def test_pop_back_leaving_one_return_value(self):
  	self.__deque.push_front('Yangchen')
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.pop_back()
  	self.assertEqual('Yangchen', to_return)

  def test_pop_back_leaving_one_remaining_deque(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.pop_back()
  	self.assertEqual('[ Structure ]', str(self.__deque))

  def test_pop_back_leaving_one_length(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structure')
  	to_return = self.__deque.pop_back()
  	self.assertEqual(1, len(self.__deque))

  def test_pop_front_leaving_empty_push_front(self):
  	self.__deque.push_front('Data')
  	to_return = self.__deque.pop_front()
  	self.__deque.push_front('Structure')
  	self.assertEqual('[ Structure ]', str(self.__deque))

  def test_pop_front_leaving_empty_push_back(self):
  	self.__deque.push_front('Data')
  	to_return = self.__deque.pop_front()
  	self.__deque.push_back('Structure')
  	self.assertEqual('[ Structure ]', str(self.__deque))

  def test_pop_front_leaving_one_push_front(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.pop_front()
  	self.__deque.push_front('Ye')
  	self.assertEqual('[ Ye, Data ]', str(self.__deque))

  def test_pop_front_leaving_one_push_back(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.pop_front()
  	self.__deque.push_back('Ye')
  	self.assertEqual('[ Data, Ye ]', str(self.__deque))

  def test_pop_back_leaving_empty_push_front(self):
  	self.__deque.push_front('Data')
  	to_return = self.__deque.pop_back()
  	self.__deque.push_front('Structure')
  	self.assertEqual('[ Structure ]', str(self.__deque))

  def test_pop_back_leaving_empty_push_back(self):
  	self.__deque.push_front('Data')
  	to_return = self.__deque.pop_back()
  	self.__deque.push_back('Structure')
  	self.assertEqual('[ Structure ]', str(self.__deque))

  def test_pop_back_leaving_one_push_front(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.pop_back()
  	self.__deque.push_front('Ye')
  	self.assertEqual('[ Ye, Structure ]', str(self.__deque))

  def test_pop_back_leaving_one_push_back(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.pop_back()
  	self.__deque.push_back('Ye')
  	self.assertEqual('[ Structure, Ye ]', str(self.__deque))

  def test_peek_front_empty_return_value(self):
  	to_return = self.__deque.peek_front()
  	self.assertEqual(None, to_return)

  def test_peek_front_empty_remaining_deque(self):
  	to_return = self.__deque.peek_front()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_peek_front_empty_length(self):
  	to_return = self.__deque.peek_front()
  	self.assertEqual(0, len(self.__deque))

  def test_peek_front_one_return_value(self):
  	self.__deque.push_front('Yangchen')
  	to_return = self.__deque.peek_front()
  	self.assertEqual('Yangchen', to_return)

  def test_peek_front_one_remaining_deque(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_front()
  	self.assertEqual('[ Ye ]', str(self.__deque))

  def test_peek_front_one_length(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_front()
  	self.assertEqual(1, len(self.__deque))

  def test_peek_front_two_return_value(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.peek_front()
  	self.assertEqual('Structure', to_return)

  def test_peek_front_two_remaining_deque(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_retuen = self.__deque.peek_front()
  	self.assertEqual('[ Structure, Data ]', str(self.__deque))

  def test_peek_front_two_length(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_retuen = self.__deque.peek_front()
  	self.assertEqual(2, len(self.__deque))

  def test_peek_back_empty_return_value(self):
  	to_return = self.__deque.peek_back()
  	self.assertEqual(None, to_return)

  def test_peek_back_empty_remaining_deque(self):
  	to_return = self.__deque.peek_back()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_peek_back_empty_length(self):
  	to_return = self.__deque.peek_back()
  	self.assertEqual(0, len(self.__deque))

  def test_peek_back_one_return_value(self):
  	self.__deque.push_front('Yangchen')
  	to_return = self.__deque.peek_back()
  	self.assertEqual('Yangchen', to_return)

  def test_peek_back_one_remaining_deque(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_back()
  	self.assertEqual('[ Ye ]', str(self.__deque))

  def test_peek_back_one_length(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_back()
  	self.assertEqual(1, len(self.__deque))

  def test_peek_back_two_return_value(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_return = self.__deque.peek_back()
  	self.assertEqual('Data', to_return)

  def test_peek_back_two_remaining_deque(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_retuen = self.__deque.peek_back()
  	self.assertEqual('[ Structure, Data ]', str(self.__deque))

  def test_peek_back_two_length(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structure')
  	to_retuen = self.__deque.peek_back()
  	self.assertEqual(2, len(self.__deque))

  def test_peek_front_push_front_remaining_deque(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_front()
  	self.__deque.push_front('Yangchen')
  	self.assertEqual('[ Yangchen, Ye ]', str(self.__deque))

  def test_peek_front_push_front_length(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_front()
  	self.__deque.push_front('Yangchen')
  	self.assertEqual(2, len(self.__deque))

  def test_peek_front_push_back_remaining_deque(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_front()
  	self.__deque.push_back('Yangchen')
  	self.assertEqual('[ Ye, Yangchen ]', str(self.__deque))

  def test_peek_front_push_back_length(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_front()
  	self.__deque.push_back('Yangchen')
  	self.assertEqual(2, len(self.__deque))

  def test_peek_back_push_front_remaining_deque(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_back()
  	self.__deque.push_front('Yangchen')
  	self.assertEqual('[ Yangchen, Ye ]', str(self.__deque))

  def test_peek_back_push_front_length(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_back()
  	self.__deque.push_front('Yangchen')
  	self.assertEqual(2, len(self.__deque))

  def test_peek_back_push_back_remaining_deque(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_back()
  	self.__deque.push_back('Yangchen')
  	self.assertEqual('[ Ye, Yangchen ]', str(self.__deque))

  def test_peek_back_push_back_length(self):
  	self.__deque.push_front('Ye')
  	to_return = self.__deque.peek_back()
  	self.__deque.push_back('Yangchen')
  	self.assertEqual(2, len(self.__deque))

  #testing stack
  def test_empty_stack_string(self):
  	self.assertEqual('[ ]', str(self.__stack))

  def test_push_empty(self):
  	self.__stack.push('Data')
  	self.assertEqual('[ Data ]', str(self.__stack))

  def test_push_one(self):
  	self.__stack.push('Data')
  	self.__stack.push('Structure')
  	self.assertEqual('[ Structure, Data ]', str(self.__stack))

  def test_empty_stack_length(self):
  	self.assertEqual(0, len(self.__stack))

  def test_one_stack_length(self):
  	self.__stack.push('Data')
  	self.assertEqual(1, len(self.__stack))

  def test_two_stack_length(self):
  	self.__stack.push('Data')
  	self.__stack.push('Structure')
  	self.assertEqual(2, len(self.__stack))

  def test_pop_empty_return_value(self):
  	to_return = self.__stack.pop()
  	self.assertEqual(None, to_return)

  def test_pop_empty_remaining_stack(self):
  	to_return = self.__stack.pop()
  	self.assertEqual('[ ]', str(self.__stack))

  def test_pop_empty_length(self):
  	to_return = self.__stack.pop()
  	self.assertEqual(0, len(self.__stack))

  def test_pop_one_return_value(self):
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.pop()
  	self.assertEqual('Yangchen', to_return)

  def test_pop_one_remaining_stack(self):
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.pop()
  	self.assertEqual('[ ]', str(self.__stack))

  def test_pop_one_length(self):
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.pop()
  	self.assertEqual(0, len(self.__stack))

  def test_pop_two_return_value(self):
  	self.__stack.push('Yangchen')
  	self.__stack.push('Ye')
  	to_return = self.__stack.pop()
  	self.assertEqual('Ye', to_return)

  def test_pop_two_remaining_stack(self):
  	self.__stack.push('Ye')
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.pop()
  	self.assertEqual('[ Ye ]', str(self.__stack))

  def test_pop_two_length(self):
  	self.__stack.push('Ye')
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.pop()
  	self.assertEqual(1, len(self.__stack))

  def test_peek_empty_return_value(self):
  	to_return = self.__stack.peek()
  	self.assertEqual(None, to_return)

  def test_peek_empty_remaining_stack(self):
  	to_return = self.__stack.peek()
  	self.assertEqual('[ ]', str(self.__stack))

  def test_peek_empty_length(self):
  	to_return = self.__stack.peek()
  	self.assertEqual(0, len(self.__stack))

  def test_peek_one_return_value(self):
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.peek()
  	self.assertEqual('Yangchen', to_return)

  def test_peek_one_remaining_stack(self):
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.peek()
  	self.assertEqual('[ Yangchen ]', str(self.__stack))

  def test_peek_one_length(self):
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.peek()
  	self.assertEqual(1, len(self.__stack))

  def test_peek_two_return_value(self):
  	self.__stack.push('Yangchen')
  	self.__stack.push('Ye')
  	to_return = self.__stack.peek()
  	self.assertEqual('Ye', to_return)

  def test_peek_two_remaining_stack(self):
  	self.__stack.push('Ye')
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.peek()
  	self.assertEqual('[ Yangchen, Ye ]', str(self.__stack))

  def test_peek_two_length(self):
  	self.__stack.push('Ye')
  	self.__stack.push('Yangchen')
  	to_return = self.__stack.peek()
  	self.assertEqual(2, len(self.__stack))

  #testing queue
  def test_empty_queue_string(self):
  	self.assertEqual('[ ]', str(self.__queue))

  def test_enqueue_empty(self):
  	self.__queue.enqueue('Data')
  	self.assertEqual('[ Data ]', str(self.__queue))

  def test_enqueue_one(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structure')
  	self.assertEqual('[ Data, Structure ]', str(self.__queue))

  def test_enqueue_two(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structure')
  	self.__queue.enqueue('241')
  	self.assertEqual('[ Data, Structure, 241 ]', str(self.__queue))

  def test_dequeue_empty_return_value(self):
  	to_return = self.__queue.dequeue()
  	self.assertEqual(None, to_return)

  def test_dequeue_empty_remaining_queue(self):
  	to_return = self.__queue.dequeue()
  	self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_empty_length(self):
  	to_return = self.__queue.dequeue()
  	self.assertEqual(0, len(self.__queue))

  def test_dequeue_one_return_value(self):
  	self.__queue.enqueue('Yangchen')
  	to_return = self.__queue.dequeue()
  	self.assertEqual('Yangchen', to_return)

  def test_dequeue_one_remaining_queue(self):
  	self.__queue.enqueue('Yangchen')
  	to_return = self.__queue.dequeue()
  	self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_one_length(self):
  	self.__queue.enqueue('Yangchen')
  	to_return = self.__queue.dequeue()
  	self.assertEqual(0, len(self.__queue))

  def test_dequeue_two_return_value(self):
  	self.__queue.enqueue('Yangchen')
  	self.__queue.enqueue('Ye')
  	to_return = self.__queue.dequeue()
  	self.assertEqual('Yangchen', to_return)

  def test_dequeue_two_remaining_queue(self):
  	self.__queue.enqueue('Yangchen')
  	self.__queue.enqueue('Ye')
  	to_return = self.__queue.dequeue()
  	self.assertEqual('[ Ye ]', str(self.__queue))

  def test_dequeue_empty_length(self):
  	self.__queue.enqueue('Yangchen')
  	self.__queue.enqueue('Ye')
  	to_return = self.__queue.dequeue()
  	self.assertEqual(1, len(self.__queue))


uif __name__ == '__main__':
  unittest.main()

