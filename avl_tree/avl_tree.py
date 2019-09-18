"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()
        
        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                f'[{self.height}:{self.balance}]',
                'L' if self.height == 0 else ' ')
        if self.node.left != None:
            self.node.left.display(level + 1, '<')
        if self.node.right != None:
            self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        left = 0
        right = 0

        if self.node.left:
            left = self.node.left.update_height()
        
        if self.node.right:
            right = self.node.right.update_height()
        
        #  Get the height of this node
        self.height = left if left >= right else right
        return self.height + 1



    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        left = 0
        right = 0
        if self.node.left:
            left = self.node.left.height
        if self.node.right:
            right = self.node.right.height

        # balanceFactor = height(left subtree) - height(right subtree)
        self.balance = left - right

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        next_self = self.node.right
        temp_left = AVLTree(self.node)

        if self.node.right.node.left:
            temp_right = self.node.right.node.left
            temp_left.node.right = temp_right

        next_self.node.left = temp_left

        self.node = next_self.node


    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        next_self = self.node.left
        temp_right = AVLTree(self.node)

        if self.node.left.node.right:
            temp_left = self.node.left.node.right
            temp_right.node.left = temp_left
        
        next_self.node.right = temp_right

        self.node = next_self.node

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        # if left height > right height, rotate right
        # else rotate left
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        # insert logic
        if self.node is None:
            self.node = Node(key)
            return # DEBUG: How will this work in recursion?
        
        if key >= self.node.key:
            # move down right tree
            if self.node.right is None:
                self.node.right = AVLTree(Node(key))
            else:
                self.node.right.insert(key)
        
        else:
            # move down left tree
            if self.node.left is None:
                self.node.left = AVLTree(Node(key))
            else:
                self.node.left.insert(key)

        # update_height
        self.update_height()
        # update_balance
        self.update_balance()
        # if balance < -1 or > 1, rebalance
        if self.balance < -1 or self.balance > 1:
            self.rebalance()
