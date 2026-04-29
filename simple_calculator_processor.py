# Importing functions and the parent class from processor.py
from simple_calculator_logic import FileHandler, add, sub, mult, div


# --- CHILD CLASS (Inheritance) ---
class MaangasUI(FileHandler):
    def __init__(self):
        # Setting up the parent class with a filename
        super().__init__(filename="LifeVault_History.txt")

        # Mapping symbols to the imported functions
        self.operations = {
            "+": add, "-": sub, "*": mult, "/": div
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