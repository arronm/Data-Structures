import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    """
    Our TextBuffer class keeps a buffer of characters
    that can be printed out as text.
    """
    def __init__(self):
        # using doubly linked list because it already exists
        # a singly linked list would be more memory efficient
        self.buffer = DoublyLinkedList()
        self.__len__ = 24
    
    def __str__(self):
        """
        Allows us to print out the text in our buffer
        """
        # somehow allows us to call print
        current_char = self.buffer.head
        string = ''
        while current_char:
            string += current_char.value
            current_char = current_char.next
        return string


    def append(self, chars):
        """
        Adds new characters to the back of the buffer
        """
        # Add characters to tail of buffer
        for letter in chars:
            self.buffer.add_to_tail(letter)
    
    def prepend(self, chars):
        """
        Adds new characters to the front of the buffer
        """
        # Add characters to the head of buffer
        for letter in chars[::-1]:
            self.buffer.add_to_head(letter)
    
    def delete_front(self):
        """
        Removes a character from the front of the buffer
        """
        # removes head from buffer
        self.buffer.remove_from_head()

    def delete_back(self):
        """
        Removes a character from the back of the buffer
        """
        # removes tail from buffer
        self.buffer.remove_from_tail()
    
    def join(self, buffer):
        """
        Concatenates provided buffer to current TextBuffer
        """
        # sets tail of buffer to head of new buffer
        # technically shouldn't modify buffer variables here
        # would otherwise modify dll or use sll
        self.buffer.tail.next = buffer.buffer.head
        buffer.buffer.head.previous = self.buffer.tail

    def __len__(self):
        return self.buffer.length

if __name__ == '__main__':
    buffer = TextBuffer()
    buffer.append('z')
    buffer.append('b')
    buffer.append('c')
    buffer.delete_front()
    buffer.prepend('a')
    buffer.prepend('q')
    buffer2 = TextBuffer()
    buffer2.prepend('y')
    buffer2.prepend('x')
    buffer2.append('z')
    buffer.join(buffer2)
    buffer.delete_front()
    buffer.append('asdfl')
    print(len(buffer))
    print(buffer)