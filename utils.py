"""
Conceitos essenciais sobre Hash Table:
Tamanho:
  Quantidade máxima de elementos na tabela.

Função de Espalhamento:
  Função que gera um código a ser utilizado
  como índice de acesso na tabela.

Colisões:
  Ocorre uma colisão quando a função de espalhamento
  gera o mesmo código para chaves diferentes.

Fator de carga:
  Quantidade de elementos / tamanho da tabela.
"""
class Contact:
  def __init__(self,name,address, telephone_number) -> None:
    self.name = name
    self.address = address
    self.telephone_number = telephone_number

class Node:
  def __init__(self,key,value) -> None:
    self.key = key
    self.value = value
    self.next = None