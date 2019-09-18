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
        # if value > max, set max
        if value > self.max:
            self.max = value

        # if value >= self.value
        if value >= self.value:
            # move down right
            # if no node exists, this is our node
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            # value < self.value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)


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
