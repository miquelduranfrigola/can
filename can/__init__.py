import os
import subprocess
import colorama
import subprocess
from .script import Script

TYPEWRITER_SOUND = True

# Initialize colorama
colorama.init(autoreset=True)

root = os.path.dirname(os.path.abspath(__file__))


def clear_screen():
    os.system("clear")


def set_terminal_style():
    style_code = """
    tell application "Terminal"
        set current settings of first window to settings set "Homebrew"
    end tell
    """
    subprocess.run(["osascript", "-e", style_code])


def activate_loud_typing():
    apple_script = """
    tell application "Loud Typer"
        activate
    end tell
    """
    subprocess.run(["osascript", "-e", apple_script])


def main():
    if TYPEWRITER_SOUND:
        activate_loud_typing()
    set_terminal_style()
    clear_screen()
    script = Script()
    script.header()
    while True:
        user_input = input()
        script.run(user_input)


if __name__ == "__main__":
    main()
