import os
import time
from colorama import Fore
from .media.image import ImageFile, ImageDalle
from .media.sound import SoundFile, TextToSpeech
from .media.text import GPT


class Script(object):
    def __init__(self):
        self.root = os.path.dirname(os.path.abspath(__file__))

    def _assets_file(self, file_name):
        return os.path.abspath(os.path.join(self.root, "..", "assets", file_name))

    def _print(self, text, color="blue", delay=0.05):
        if color == "blue":
            color = Fore.LIGHTBLUE_EX
        if color == "red":
            color = Fore.LIGHTRED_EX
        if color == "green":
            color = Fore.LIGHTGREEN_EX
        if color == "yellow":
            color = Fore.LIGHTYELLOW_EX
        for character in text:
            print(color + character, end="", flush=True)
            time.sleep(delay)
        print()

    def _play_sound_from_file(self, file_path, timeout=None):
        SoundFile(file_path=file_path).play(timeout=timeout)

    def _play_sound_from_text(self, text):
        TextToSpeech().play(text)

    def _display_fullscreen_image_from_file(self, file_path, display_time=3):
        ImageFile(file_path=file_path).display_fullscreen(display_time=display_time)

    def _display_fullscreen_image_from_text(self, text, display_time=3):
        ImageDalle(context="I want a photorealistic figure ").display_fullscreen(
            text, display_time=display_time
        )

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
            return self._display_fullscreen_image_from_file(
                self._assets_file("fageda.jpeg")
            )

        if input_line == "so":
            return self._play_sound_from_file(self._assets_file("ubuntu_brothers.mp3"))

        if input_line == "gpt prova":
            text = GPT("Dona'm un text poètic").post(
                "Una artista de circ que es diu Gemma"
            )
            return self._print(text)

        if input_line == "dalle prova":
            self._display_fullscreen_image_from_text("The city of Ersilia")
            return

        if input_line == "tts prova":
            self._play_sound_from_text("Hola Gemma com estas?")
            return

        self._print("No t'entenc", "red")
