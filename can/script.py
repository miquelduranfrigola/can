import time
from colorama import Fore
from .image import display_fullscreen_image


class Script(object):
    def __init__(self):
        pass

    def _print(self, text, color="blue", delay=0.05):
        if color == "blue":
            color = Fore.BLUE
        if color == "red":
            color = Fore.RED
        if color == "green":
            color = Fore.GREEN
        if color == "yellow":
            color = Fore.YELLOW
        for character in text:
            print(color + character, end="", flush=True)
            time.sleep(delay)
        print()

    def _voice(self, text):
        pass

    def _display_fullscreen_image(self, image_path, display_time=3):
        display_fullscreen_image(image_path=image_path, display_time=display_time)

    def header(self):
        self._print("Benvinguda a Ca'n", "yellow")

    def run(self, input_line):
        if input_line == "Quan veurem el resultat?":
            return self._print("Aviat esperem :)")

        if input_line == "Hola!":
            return self._print("Estem en procés de creació a l'Ateneu de 9Barris!")
        
        if input_line == "Fins quan?":
            return self._print("Tenim la Residència de Taula fins el 26 de gener.")

        if input_line == "imatge":
            self._display_fullscreen_image("fageda.jpeg")
