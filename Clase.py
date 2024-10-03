import random

class BasicOperations:
   def add(self, a, b):
      return a + b
       
   def sub(self, a, b):
      return a - b
   
   def mul(self, a, b):
      return a * b
   
   def div(self, a, b):
      if b != 0:
         return a / b
      else:
         return "No se puede dividir por cero"


        #eleva el numero por un valor
class Square:
   def getVal(self, val):
      return val * val

class RandomCalculator:
   def __init__(self):
      self.operations = BasicOperations()
      self.square = Square()

