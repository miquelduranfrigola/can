from can.media.text import ContextManager, TextManager, GPT

cm = ContextManager()
# context = cm.get("convertir-en-un-tweet")
context = """
Completa el següent poema amb una sola frase, d'entre 15 i 25 paraules. Que la frase comenci amb la paraula "Ser".
La frase no pot contenir el mot "poema".
Un exemple seria: Ser l’únic refugi infal·lible contra la supremacia del visible.
No vull que copïis l'exemple. Sigues original.
Aquest és el text:
"""


tm = TextManager()
text = tm.get("la-llico-mes-important")

gpt = GPT(context)
output = gpt.post(text)

print(output)
