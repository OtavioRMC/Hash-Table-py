from utils import Contact

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
  
  
