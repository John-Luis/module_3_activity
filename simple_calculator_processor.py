import sys
import time
from simple_calculator_logic import CalculatorLogic

# Aesthetic tools for the "Maangas" vibe
CYAN, GREEN, RED, YELLOW, RESET = "\033[96m", "\033[92m", "\033[91m", "\033[93m", "\033[0m"

def typewriter(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

class MaangasUI(CalculatorLogic):
    def __init__(self):
        # Inherits both math and logging from CalculatorLogic
        super().__init__()
        self.operations = {
            "+": self.add, "-": self.sub, "*": self.mult,
            "/": self.div, "**": self.power, "%": self.mod
        }

    def start(self):
        print("=" * 40)
        print("🚀 ALPHA CALCULATOR v2.0 | ONLINE")
        print("Usage: [num] [op] [num] | Type 'OFF' to quit")
        print("=" * 40)

        while True:
            try:
                user_input = input("\nλ >> ").strip()
                if user_input.upper() == "OFF":
                    print("System shutting down. Stay epic, John Luis!")
                    break

                parts = user_input.split()
                if len(parts) != 3:
                    raise IndexError("Format: [num] [op] [num]")

                num1, op, num2 = float(parts[0]), parts[1], float(parts[2])

                if op in self.operations:
                    result = self.operations[op](num1, num2)
                    print(f"✨ RESULT: {result}")

                    # Using the inherited method from FileHandler
                    self.save_to_vault(user_input, result)
                else:
                    print("❌ Error: Invalid operator.")

            except ValueError:
                print("⚠️ Error: Please enter valid numbers.")
            except (IndexError, ZeroDivisionError) as e:
                print(f"⚠️ {e}")
            except Exception as e:
                print(f"⚠️ Unexpected Error: {e}")



app = MaangasUI()
app.start()