import datetime
import os


#Creating the core math functions here
def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b

def div(a, b):
    if b == 0: raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

class FileHandler:
    def __init__(self, filename):
        self.filename = filename