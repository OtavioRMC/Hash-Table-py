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
    if node is not None:
      self.table[hash_index] = Node(key,value)
    else:
      while node is not None:
        if node.key == key:
          node.value = value
          return
        prev = node
        node = node.next
      prev.next = Node(key,value)
  
