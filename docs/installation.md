![agent Banner](https://github.com/user-attachments/assets/fd16ab2d-71bd-4300-b495-73d573044325)

# Installation

## Prérequis

- Python 3.8+
- PyTorch 2.0+
- Transformers 4.25+
- accelerate (optionnel)

## Installation des dépendances

```bash
pip install torch transformers accelerate
```
## **Télécharger agentV1**
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agentV1")
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agentV1",
    device_map="auto",
    torch_dtype="auto"
)
Vérifier l’installation
print(model.config)

```
# *verification**
```python
print(model.config)

---
