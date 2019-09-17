import unittest
from text_buffer import TextBuffer


class TextBufferTests(unittest.TestCase):
  def setUp(self):
    self.buffer_one = TextBuffer()
    self.buffer_two = TextBuffer()

  def test_empty_buffer(self):
    self.assertEqual(self.buffer_one.__str__(), '')


  def test_buffer_append(self):
    self.buffer_one.append('x')
    self.assertEqual(self.buffer_one.__str__(), 'x')
    self.buffer_one.append('y')
    self.assertEqual(self.buffer_one.__str__(), 'xy')


  def test_buffer_prepend(self):
    self.buffer_one.prepend('y')
    self.assertEqual(self.buffer_one.__str__(), 'y')
    self.buffer_one.prepend('x')
    self.buffer_one.append('z')
    self.assertEqual(self.buffer_one.__str__(), 'xyz')


  def test_buffer_delete_front(self):
    self.buffer_one.append('a')
    self.buffer_one.append('b')
    self.buffer_one.append('c')
    self.buffer_one.prepend('x')
    self.buffer_one.delete_front()
    self.assertEqual(self.buffer_one.__str__(), 'abc')


  def test_buffer_delete_back(self):
    self.buffer_one.append('a')
    self.buffer_one.append('b')
    self.buffer_one.append('c')
    self.buffer_one.append('x')
    self.buffer_one.delete_back()
    self.assertEqual(self.buffer_one.__str__(), 'abc')


  def test_buffer_handle_multiple_characters(self):
    self.buffer_one.append('abc')
    self.buffer_one.delete_front()
    self.assertEqual(self.buffer_one.__str__(), 'bc')


  def test_buffer_join(self):
    self.buffer_one.append('abc')
    self.buffer_two.append('xyz')
    self.buffer_one.join(self.buffer_two)
    self.assertEqual(self.buffer_one.__str__(), 'abcxyz')

if __name__ == '__main__':
  unittest.main()
