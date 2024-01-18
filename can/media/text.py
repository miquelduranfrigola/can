from openai import OpenAI
import os
import yaml


class ContextManager(object):
    def __init__(self):
        root = os.path.dirname(os.path.abspath(__file__))
        self.contexts_dir = os.path.abspath(
            os.path.join(root, "..", "..", "assets", "contexts")
        )
        self.contexts_file = os.path.join(self.contexts_dir, "text_contexts.yml")
        with open(self.contexts_file, "r") as file:
            data = yaml.safe_load(file)
        self.data = {}
        for r in data:
            self.data[r["name"]] = r["context"]

    def get(self, context_name):
        return self.data[context_name]


class TextManager(object):
    def __init__(self):
        root = os.path.dirname(os.path.abspath(__file__))
        self.texts_dir = os.path.abspath(
            os.path.join(root, "..", "..", "assets", "texts")
        )
        self.texts_file = os.path.join(self.texts_dir, "text_texts.yml")
        with open(self.texts_file, "r") as file:
            data = yaml.safe_load(file)
        self.data = {}
        for r in data:
            self.data[r["name"]] = r["text"]

    def get(self, text_name):
        return self.data[text_name]


class GPT(object):
    def __init__(self, context, model="gpt-3.5-turbo"):
        self.client = OpenAI()
        self.context = context
        self.model = model

    def post(self, query):
        messages = [
            {"role": "system", "content": self.context},
            {"role": "user", "content": query},
        ]
        completion = self.client.chat.completions.create(
            model=self.model, messages=messages
        )
        message = completion.choices[0].message
        return message.content
