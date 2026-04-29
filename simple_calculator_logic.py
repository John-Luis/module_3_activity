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

    def save_to_vault(self, math_input, result):
        """This method will be inherited by the UI class."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] INPUT: {math_input} | RESULT: {result}\n"

        with open(self.filename, "a") as file:
            file.write(log_entry)
        print(f"📁 Logged to {self.filename}")


# Inherits from FileHandler to gain the save_to_vault capability.
class MaangasUI(FileHandler):
    def __init__(self):
        # Linking to the parent and setting the filename
        super().__init__(filename="LifeVault_History.txt")


        self.operations = {
            "+": add,
            "-": sub,
            "*": mult,
            "/": div
        }

    def start(self):
        print("=" * 40)
        print("🚀 ALPHA CALCULATOR v2.0 | ONLINE")
        print("Usage: [num] [op] [num] | Type 'OFF' to quit")
        print("=" * 40)