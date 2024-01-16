from openai import OpenAI


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
