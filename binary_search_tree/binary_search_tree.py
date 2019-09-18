import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

    # Set our initial maximum value to initial value
    self.max = value

  def insert(self, value):
    pass

  def contains(self, target):
    pass

  def get_max(self):
    return self.max

  def for_each(self, cb):
    # while self.left
    #   recursive function with left node
    # while self.right
    #   recursive function with right node
    pass

if __name__ == '__main__':
  print('hello')
