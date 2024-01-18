import os
import time
from colorama import Fore
from datetime import datetime
from .media.image import ImageFile, ImageDalle, ImageContextManager
from .media.sound import SoundFile, TextToSpeech
from can.media.text import ContextManager, TextManager, GPT


class Script(object):
    def __init__(self):
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.cm = ContextManager()
        self.tm = TextManager()

    def _assets_file(self, file_name):
        return os.path.abspath(os.path.join(self.root, "..", "assets", file_name))

    def _print(self, text, color="white", delay=0.05):
        if color == "white":
            color = Fore.WHITE
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

    def _display_fullscreen_image_from_text(self, context, text, display_time=3):
        ImageDalle(context=context).display_fullscreen(text, display_time=display_time)

    def header(self):
        current_datetime = datetime.now()
        dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        self._print(dt, "yellow")

    def run(self, input_line):
        if input_line == "Hola":
            return self._print("Hola 🙂")

        if input_line == "imatge":
            return self._display_fullscreen_image_from_file(
                self._assets_file("fageda.jpeg")
            )

        if input_line == "so":
            return self._play_sound_from_file(self._assets_file("ubuntu_brothers.mp3"))

        # La llico mes important, Marti Sales

        if input_line.startswith("La ciència"):
            return

        if input_line.startswith("Les coses"):
            return

        if input_line.startswith("El llenguatge"):
            return

        if input_line.startswith("El poema"):
            return

        if input_line == "Què fa el poema?":
            context = self.cm.get("que-fa-el-poema")
            text = self.tm.get("la-llico-mes-important-0")
            output = GPT(context=context).post(text)
            image_context = ImageContextManager().get("pintor-impressionista")
            self._display_fullscreen_image_from_text(image_context, output)
            self._play_sound_from_text(output)
            return self._print(output)

        if input_line == "Què fa el llenguatge?":
            context = self.cm.get("que-fa-el-llenguatge")
            text = self.tm.get("la-llico-mes-important-1")
            return self._print(GPT(context=context).post(text))

        if input_line == "Què fan les coses?":
            context = self.cm.get("que-fan-les-coses")
            text = self.tm.get("la-llico-mes-important-2")
            return self._print(GPT(context=context).post(text))

        if input_line == "Què fa la ciència?":
            context = self.cm.get("que-fa-la-ciencia")
            text = self.tm.get("la-llico-mes-important-3")
            return self._print(GPT(context=context).post(text))

        self._print("No t'entenc", "red")
