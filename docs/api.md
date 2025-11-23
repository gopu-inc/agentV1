# `docs/api.md`


# API de agentV1

## Classe principale : AgentV1

### Initialisation

```python

agent = AgentV1()
Méthode : ask()
Pose une question à l’agent.
agent.ask(
    question="Explique-moi Python.",
    max_tokens=200,
    temperature=0.7
)
Méthode : batch_ask()
agent.batch_ask([
    "Bonjour",
    "Explique-moi les listes en Python"
])
Paramètres avancés
generate()
model.generate(
    input_ids,
    max_new_tokens=200,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
    do_sample=True
)
Gestion GPU / CPU
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agentV1",
    device_map="cuda"  # ou "cpu"
)
