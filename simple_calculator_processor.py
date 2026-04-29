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