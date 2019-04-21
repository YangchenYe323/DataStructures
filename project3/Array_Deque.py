from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = None
    self.__back = None
    self.__size = 0
    
  def __str__(self):
    if self.__size == 0:
      return '[ ]'
    else:
      result = '[ '
      for k in range(self.__size-1):
        index = (self.__front + k) % self.__capacity
        result = result + str(self.__contents[index]) + ', '
      result = result + str(self.__contents[self.__back]) + ' ]'
      return result
    
  def __len__(self):
    return self.__size

  def __grow(self):
    new_capacity = self.__capacity * 2
    new_contents = [None] * new_capacity
    for k in range(self.__size):
      index = (self.__front + k) % self.__capacity
      new_contents[k] = self.__contents[index]
    self.__contents = new_contents
    self.__capacity = new_capacity
    self.__front = 0
    self.__back = self.__size - 1

  #I use left "-1" as the front direction and right "+1" as the back direction, so
  #pushing front and popping back should result in the "-1" of front/back reference
  #and pushing back and popping front should result in the "+1" of
  #back/front reference
    
  def push_front(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    if self.__front is None:
      #if the deque is empty, a push should initiallize the front and back reference to 0
      self.__front = 0
      self.__back = 0
    else:
      self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
    self.__contents[self.__front] = val
    self.__size = self.__size + 1

    
  def pop_front(self):
    if self.__size == 0:
      return
    value = self.__contents[self.__front]
    self.__front = (self.__front + 1) % self.__capacity
    self.__size = self.__size - 1
    if self.__size == 0:
      #if the deque is empty after popping, reset the front and back reference to None
      self.__front = None
      self.__back = None
    return value

  def peek_front(self):
    if self.__size == 0:
      return
    return self.__contents[self.__front]
    
  def push_back(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    if self.__back == None:
      self.__front = 0
      self.__back = 0
    else:
      self.__back = (self.__back + 1) % self.__capacity
    self.__contents[self.__back] = val
    self.__size = self.__size + 1
  
  def pop_back(self):
    if self.__size == 0:
      return
    value = self.__contents[self.__back]
    self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
    self.__size = self.__size - 1
    if self.__size == 0:
      self.__back = None
      self.__front = None
    return value

  def peek_back(self):
    if self.__size == 0:
      return
    return self.__contents[self.__back]
