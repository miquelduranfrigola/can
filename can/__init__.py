import os
import colorama
from colorama import Fore
import subprocess
from .script import Script

# Initialize colorama
colorama.init(autoreset=True)


def clear_screen():
    os.system("clear")


def set_terminal_style():
    style_code = """
    tell application "Terminal"
        set current settings of first window to settings set "Homebrew"
    end tell
    """
    subprocess.run(["osascript", "-e", style_code])


def main():
    set_terminal_style()
    clear_screen()
    script = Script()
    script.header()

    while True:
        user_input = input(Fore.LIGHTGREEN_EX)
        script.run(user_input)


if __name__ == "__main__":
    main()
