from can.media.text import ContextManager, TextManager, GPT

cm = ContextManager()
context = cm.get("convertir-en-un-tweet")

tm = TextManager()
text = tm.get("la-vida-mateixa-circ")

gpt = GPT(context)
output = gpt.post(text)

print(output)
