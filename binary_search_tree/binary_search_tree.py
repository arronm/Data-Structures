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
        # if self.value == target, return
        if self.value == target:
            return True
        # if target >= self.value, traverse right
        if target >= self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        # else, traverse left
        else:
            if self.left is None:
                return False
            return self.left.contains(target)

    def get_max(self):
        return self.max

    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_dft(self, node):
        # left-first depth-first recursive function
        # if left, left.in_order_dft
        if node.left:
            node.left.in_order_dft(node.left)
        
        # print(value)
        print(node.value)

        # if right, right.in_order_dft
        if node.right:
            node.right.in_order_dft(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Use Queue
        queue = Queue()

        # add root to queue
        queue.enqueue(node)

        # while queue is not empty
        while queue.len() > 0:
            # print root, dequeue
            current = queue.dequeue()
            print(current.value)

            # add left to queue
            if current.left:
                queue.enqueue(current.left)

            # add right to queue
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Use Stack
        stack = Stack()

        # add root to stack
        stack.push(node)

        # while stack is not empty
        while stack.len() > 0:
            # print root, pop
            current = stack.pop()
            print(current.value)

            # add left to stack
            if current.left:
                stack.push(current.left)

            # add right to stack
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)

if __name__ == '__main__':
    bst = BinarySearchTree(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)

    bst.dft_print(bst)