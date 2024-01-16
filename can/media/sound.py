import os
import subprocess
import time
import re
import uuid
from openai import OpenAI


class SoundFile(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def play(self, timeout):
        open_script = f"""
        tell application "QuickTime Player"
            open POSIX file "{self.file_path}"
            play the front document
            set doc to the front document
            repeat while (playing of doc is true)
                delay 1
            end repeat
            close doc
            quit
        end tell
        tell application "Terminal"
            activate
        end tell
        """
        # Run the AppleScript in the background
        subprocess.Popen(["osascript", "-e", open_script])

        # Wait for the specified duration
        if timeout is not None:
            time.sleep(timeout)
            self.close()

    def close(self):
        # AppleScript to close QuickTime Player
        close_script = """
        tell application "QuickTime Player"
            close every document where playing is true
            quit
        end tell
        """
        subprocess.run(["osascript", "-e", close_script])


class TextToSpeech(object):
    def __init__(self, voice="onyx"):
        self.voice = voice
        self.client = OpenAI()

    def available_voices(self):
        return ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

    def get_file_path(self, file_name):
        root = os.path.dirname(os.path.abspath(__file__))
        return os.path.abspath(
            os.path.join(root, "..", "..", "assets", "tts", file_name)
        )

    def get_sound(self, text):
        file_name = (
            re.sub(r"[^a-zA-Z0-9]", "-", text[:100]) + "-" + str(uuid.uuid4()) + ".mp3"
        )
        file_path = self.get_file_path(file_name)
        response = self.client.audio.speech.create(
            model="tts-1", voice=self.voice, input=text
        )
        response.stream_to_file(file_path)
        return file_path

    def play(self, text):
        file_path = self.get_sound(text)
        SoundFile(file_path=file_path).play(timeout=None)
