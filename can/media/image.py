import os
import time
import re
import uuid
import requests
from openai import OpenAI


class ImageFile(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def display_fullscreen(self, display_time=5):
        os.system(f"open -a Preview {self.file_path}")
        time.sleep(display_time)
        os.system("""osascript -e 'tell application "Preview" to close every window'""")
        os.system("""osascript -e 'tell application "Terminal" to activate'""")


class ImageDalle(object):
    def __init__(self, context):
        self.client = OpenAI()
        self.context = context

    def get_file_path(self, file_name):
        root = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(root, "..", "..", "assets", "dalle", file_name)

    def download(self, url, filename):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, "wb") as file:
                    file.write(response.content)
            else:
                print(
                    f"Failed to download image. HTTP status code: {response.status_code}"
                )
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_image(self, text):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=self.context + " " + text,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        file_name = (
            re.sub(r"[^a-zA-Z0-9]", "-", text[:100]) + "-" + str(uuid.uuid4()) + ".png"
        )
        file_path = self.get_file_path(file_name)
        self.download(image_url, file_path)
        return file_path

    def display_fullscreen(self, text, display_time=5):
        file_path = self.get_image(text)
        ImageFile(file_path=file_path).display_fullscreen(display_time=display_time)
