import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    #  set up limit
    self.limit = limit
    # set up storage dll
    self.storage = DoublyLinkedList()
    # set up reference dict
    self.reference = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # access storage dict key
    # if not self.reference:
    #   return None
    # Update to most recently used
    # return self.reference[key]['value'] if key in self.reference.keys() else None

    # check if reference exists
    if not self.reference: # potential refactor if self.ref and key in
      return None;
    # check if this key exists
    if key in self.reference.keys():
      # move reference node to end
      self.storage.move_to_end(self.reference[key]['node'])
      # return reference value
      return self.reference[key]['value']

    return None;

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # are we updating an existing key
    if key in self.reference.keys():
      # We are updating an existing key
      self.reference[key]['value'] = value
      # Update it's order to reflect recently used
      self.storage.move_to_end(self.reference[key]['node'])
      return

    # it is a new key, is there room in the cache
    if self.storage.length < self.limit:
      # there is room in the cache, just add key
      node = self.storage.add_to_tail((key, value))
      self.reference[key] = {
        'value': value,
        'node': node
      }
      return
    
    # unlink storage.head
    old_key, old_value = self.storage.remove_from_head()
    # add value to tail
    node = self.storage.add_to_tail((key, value))
    # remove old reference, del reference[key]
    del self.reference[old_key]
    # add new reference with value/node
    self.reference[key] = {
      'value': value,
      'node': node
    }
    return


if __name__ == '__main__':
  cache = LRUCache(2);
  cache.set('abc', 123)
  cache.set('def', 456)
  cache.set('abc', 789)
  cache.set('ghi', 321)
  print(cache.get('def'))