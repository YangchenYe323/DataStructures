import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  delimiter_dict = {
    '(':')',
    '[':']',
    '{':'}'
  }
  Reference_stack = Stack()
  file = open(filename)
  content = file.read()
  for ch in content:
    if ch in delimiter_dict.keys():
      Reference_stack.push(ch)
    elif ch in delimiter_dict.values():
      if len(Reference_stack) == 0:
        return False
      elif ch != delimiter_dict.get(Reference_stack.pop()):
        return False
  file.close()
  return len(Reference_stack) == 0


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


