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

   def calculate(self):
      a = random.randint(1, 10)
      b = random.randint(1, 10)
      operation = random.choice(['add', 'sub', 'mul', 'div', 'square'])
      
      if operation == 'add':
         result = self.operations.add(a, b)
         return f"Addition of {a} and {b}: {result}"
      
      elif operation == 'sub':
         result = self.operations.sub(a, b)
         return f"Subtraction of {a} and {b}: {result}"
      
      elif operation == 'mul':
         result = self.operations.mul(a, b)
         return f"Multiplication of {a} and {b}: {result}"
      
      elif operation == 'div':
         result = self.operations.div(a, b)
         return f"Division of {a} by {b}: {result}"
      
      elif operation == 'square':
         val = random.randint(1, 10)
         result = self.square.getVal(val)
         return f"Square of {val}: {result}"
