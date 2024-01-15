import os
import colorama
from colorama import Fore
from .script import Script

# Initialize colorama
colorama.init(autoreset=True)

# Function to clear the screen
def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # MacOS and Linux
    else:
        os.system('clear')


def main():
    clear_screen()
    script = Script()
    script.header()
    
    while True:
        user_input = input(Fore.GREEN)
        script.run(user_input)


if __name__ == "__main__":
    main()