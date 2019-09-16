import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0 # We're already storing len in Doubly Linked List
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    # store to head
    return self.storage.add_to_head(value)
  
  def dequeue(self):
    # remove from tail
    return self.storage.remove_from_tail()

  def len(self):
    # call len
    return self.storage.__len__()
