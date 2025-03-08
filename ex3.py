import random
import timeit
import matplotlib.pyplot as plt


# Q1 Implementation of stack that uses internal python .push() and .pop()
class ArrayStack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None


# Q2

# Q3 

# Q4 

# Q5