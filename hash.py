from utils import *

class HashTable:  
  def __init__(self,size) -> None:
    self.size = size
    self.table = [None] * size
  

  def my_hash(self,key):
    hash_value = 0
    for char in key:
      hash_value += ord(char)
    return hash_value % self.size
  
  def _hash(self,key):
    return self.my_hash(key)
  
  def set(self,key,value):
      hash_index = self._hash(key)
      node = self.table[hash_index]
      prev = None
      if node is not None:
          self.table[hash_index] = Node(key,value)
      else:
          while node is not None:
              if node.key == key:
                  node.value = value
                  return
              prev = node
              node = node.next
          if prev is None:
              self.table[hash_index] = Node(key,value)
          else:
              prev.next = Node(key,value)
      prev.next = Node(key,value)
  
  def get(self,key):
    hash_index = self._hash(key)
    node = self.table[hash_index]
    while node is not None and node.key != key:
      node = node.next
    if node is None:
      raise KeyError(f'Contact {key} not found')
    else:
      return node.value
  
  def remove(self, key):
      hash_index = self._hash(key)
      node = self.table[hash_index]
      if node is None:
          raise KeyError(f"Contact {key} not found")
          return
      if node.key == key:  # If the node to be removed is the first node
          self.table[hash_index] = node.next
      else:
          prev = node
          node = node.next
          while node is not None and node.key != key:
              prev = node
              node = node.next
          if node is None:
              raise KeyError(f"Contact {key} not found")
          else:
              prev.next = node.next