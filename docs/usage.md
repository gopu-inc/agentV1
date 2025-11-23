

# 📄 3. `docs/usage.md`

# Utilisation Rapide

## Génération simple

```python
prompt = "Explique-moi l'IA générative"

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.7
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
Mode conversation
history = []
question = "Bonjour, qui es-tu ?"

response = agent.ask(question)
Paramètres importants
Paramètre	Description
max_new_tokens	Nombre de tokens générés
temperature	Créativité
top_p	Filtrage nucleus
do_sample	Génération aléatoire
Conseils d’optimisation
Utiliser torch.float16 sur GPU
Limiter max_new_tokens sur CPU
Préférer do_sample=True pour la créativité
```
# *Mode conversation*
```
history = []
question = "Bonjour, qui es-tu ?"

response = agent.ask(question)
Paramètres importants
Paramètre	Description
max_new_tokens	Nombre de tokens générés
temperature	Créativité
top_p	Filtrage nucleus
do_sample	Génération aléatoire
Conseils d’optimisation
Utiliser torch.float16 sur GPU
Limiter max_new_tokens sur CPU
Préférer do_sample=True pour la créativité
```
___
