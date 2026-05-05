import datetime
import os


#Creating the core math functions here
def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b

def div(a, b):
    if b == 0: raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


import datetime

class FileHandler:
    def __init__(self, filename="LifeVault_History.txt"):
        self.filename = filename

    def save_to_vault(self, math_input, result):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] INPUT: {math_input} | RESULT: {result}\n"
        with open(self.filename, "a") as file:
            file.write(log_entry)

    def wipe_vault(self):
        """Purges the log file."""
        open(self.filename, 'w').close()

