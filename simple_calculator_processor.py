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
        # Clear terminal for the "Alpha" experience
        os.system('cls' if os.name == 'nt' else 'clear')

        typewriter(f"{GREEN}🚀 ALPHA CALCULATOR v3.0 | SYSTEM STABLE{RESET}")
        print(f"{YELLOW}Commands: 'SYS' for hardware, 'WIPE' to clear logs, 'OFF' to exit{RESET}")

        while True:
            try:
                # Colored input prompt
                user_input = input(f"\n{CYAN}λ >> {RESET}").strip()
                cmd = user_input.upper()

                if cmd == "OFF":
                    typewriter(f"{GREEN}Terminating session. Stay epic, John Luis!{RESET}")
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
                    raise IndexError("Usage: [num] [op] [num]")

                num1, op, num2 = float(parts[0]), parts[1], float(parts[2])

                if op in self.operations:
                    result = self.operations[op](num1, num2)
                    print(f"{GREEN}✨ RESULT: {result}{RESET}")
                    # Method inherited through logic class
                    self.save_to_vault(user_input, result)
                else:
                    print(f"{RED}❌ Error: Unauthorized operator.{RESET}")

            except Exception as e:
                print(f"{RED}⚠️ Error: {e}{RESET}")


app = MaangasUI()
app.start()