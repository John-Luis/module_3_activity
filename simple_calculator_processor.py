import sys
import time
from simple_calculator_logic import CalculatorLogic
import os
import platform

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def typewriter(text, speed=0.02):
    """Creates the high-tech terminal typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


class MaangasUI(CalculatorLogic):
    def __init__(self):
        # Inherits both math and logging through CalculatorLogic
        super().__init__()

        # Mapping symbols to inherited methods
        self.operations = {
            "+": self.add, "-": self.sub, "*": self.mult,
            "/": self.div, "**": self.power, "%": self.mod
        }

    def get_sys_info(self):
        """Displays hardware stats for that Computer Engineering vibe."""
        typewriter(f"{CYAN}--- HARDWARE MANIFEST ---{RESET}")
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Architecture: {platform.machine()}")
        print(f"User: John Luis")

    def start(self):
        # Clear terminal for that fresh "System Boot" feel
        os.system('cls' if os.name == 'nt' else 'clear')

        # --- STARTUP HEADER ---
        typewriter(f"{GREEN}🚀 ALPHA CALCULATOR v3.0 | SYSTEM ONLINE{RESET}")
        print(f"{CYAN}Developed by: John Luis | Computer Engineering{RESET}")
        print("-" * 50)

        # --- FUNCTIONALITY OVERVIEW ---
        print(f"{YELLOW}CORE CAPABILITIES:{RESET}")
        print(f"  [+] Addition        [-] Subtraction")
        print(f"  [*] Multiplication  [/] Division")
        print(f"  [**] Power/Exp      [%] Modulo")
        print(f"\n{YELLOW}SYSTEM COMMANDS:{RESET}")
        print(f"  'SYS'   -> View hardware manifest")
        print(f"  'WIPE'  -> Purge all calculation logs")
        print(f"  'OFF'   -> Terminate session safely")

        # --- USAGE EXAMPLES ---
        print(f"\n{GREEN}HOW TO USE:{RESET}")
        print(f"  Format: [number] [operator] [number]")
        print(f"  Example: {CYAN}10 + 5{RESET}  or  {CYAN}2 ** 3{RESET}")
        print("-" * 50)
        typewriter(f"{YELLOW}Ready for input...{RESET}")

        while True:
            try:
                user_input = input(f"\n{CYAN}λ >> {RESET}").strip()
                cmd = user_input.upper()

                if cmd == "OFF":
                    typewriter(f"{GREEN}Saving logs... Shutting down. Stay epic, John Luis!{RESET}")
                    break
                elif cmd == "WIPE":
                    self.wipe_vault()
                    typewriter(f"{YELLOW}🧹 Vault wiped successfully.{RESET}")
                    continue
                elif cmd == "SYS":
                    self.get_sys_info()
                    continue

                parts = user_input.split()
                if len(parts) != 3:
                    print(f"{RED}⚠️ Invalid Format. Example: 5 + 5{RESET}")
                    continue

                num1, op, num2 = float(parts[0]), parts[1], float(parts[2])

                if op in self.operations:
                    result = self.operations[op](num1, num2)
                    print(f"{GREEN}✨ CALCULATION: {num1} {op} {num2} = {result}{RESET}")
                    # Inherited from CalculatorLogic/FileHandler
                    self.save_to_vault(user_input, result)
                else:
                    print(f"{RED}❌ Error: '{op}' is not a recognized operator.{RESET}")

            except Exception as e:
                print(f"{RED}⚠️ Error: {e}{RESET}")


app = MaangasUI()
app.start()