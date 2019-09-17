import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    """
    Our TextBuffer class keeps a buffer of characters
    that can be printed out as text.
    """
    def __init__(self):
        self.buffer = DoublyLinkedList()
    
    def __str__():
        """
        Allows us to print out the text in our buffer
        """
        # somehow allows us to call print
        pass

    def append(char):
        """
        Adds a new character to the back of the buffer
        """
        # Add character to tail of buffer
        pass
    
    def prepend(char):
        """
        Adds a new character to the front of the buffer
        """
        # Add character to the head of buffer
        pass
    
    def delete_front():
        """
        Removes a character from the front of the buffer
        """
        # removes head from buffer
        pass

    def delete_back():
        """
        Removes a character from the back of the buffer
        """
        # removes tail from buffer
        pass
    
    def join():
        """
        Concatenates two text buffers together
        """
        # sets tail of buffer to head of new buffer
        pass
