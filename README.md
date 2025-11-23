
<img width="1024" height="1024" alt="IMG_6931" src="https://github.com/user-attachments/assets/d381e360-9daa-4423-a5c4-e6906b7f4afe" />


# 🤖 agentV1 — Modèle d’Intelligence Artificielle Avancée

**agentV1** est un modèle d’intelligence artificielle avancé développé par **Mauricio Mangituka** pour **gopuAI**, basé sur **Microsoft Phi-3-mini-4k-instruct**. Conçu pour être léger, performant et simple à intégrer, il combine une excellente qualité de génération et une efficacité mémoire remarquable.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![HF Model](https://img.shields.io/badge/HuggingFace-gopu--poss%2FagentV1-yellow)
![GitHub](https://img.shields.io/badge/GitHub-gopu--inc%2FagentV1-black)

---

## 🚀 Caractéristiques Principales

* **🧠 Modèle de base** : Microsoft Phi-3-mini-4k-instruct
* **💾 Taille compacte** : ~2–3 Go
* **⚡ Performances élevées** : Bon raisonnement et génération fluide
* **🌍 Multilingue** : Français 🇫🇷 & Anglais 🇬🇧
* **🔧 Optimisé** : FP16, gestion mémoire améliorée, device_map automatique
* **📦 Facile à intégrer** : Compatible Hugging Face Transformers

---

## 📚 Table des Matières

* [Installation](#installation)
* [Utilisation Rapide](#utilisation-rapide)
* [Classe AgentV1 (API)](#classe-agentv1-api)
* [Exemples](#exemples)
* [Architecture](#architecture)
* [Déploiement](#déploiement)
* [Performances](#performances)
* [Contribution](#contribution)
* [License](#license)
* [Contact](#contact)

---

## 🛠 Installation

### ✔️ Prérequis

* Python **3.8+**
* PyTorch **2.0+**
* Transformers **4.25+**

### 📦 Installation des dépendances

```bash
pip install transformers torch accelerate
```

### 📥 Chargement du modèle

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agentV1")
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agentV1",
    torch_dtype="auto",
    device_map="auto"
)
```

---

## 🚀 Utilisation Rapide

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agentV1")
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agentV1",
    torch_dtype=torch.float16,
    device_map="auto"
)

prompt = "Explique-moi comment fonctionne l'IA générative."
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7,
        do_sample=True
    )

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 🔌 Classe AgentV1 (API)

```python
class AgentV1:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agentV1")
        self.model = AutoModelForCausalLM.from_pretrained(
            "gopu-poss/agentV1",
            torch_dtype=torch.float16,
            device_map="auto"
        )
    
    def ask(self, question, max_tokens=200, temperature=0.7):
        inputs = self.tokenizer(question, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def batch_ask(self, questions, max_tokens=200):
        return [self.ask(q, max_tokens) for q in questions]
```

---

## 💬 Exemples d’Utilisation

### Conversation simple

```python
agent = AgentV1()
print(agent.ask("Bonjour, qui es-tu ?"))
```

### Génération créative

```python
story = agent.ask(
    "Écris une courte histoire sur un robot qui découvre l'amitié.",
    max_tokens=300,
    temperature=0.8
)
```

### Aide à la programmation

```python
print(agent.ask("Explique-moi comment trier une liste en Python."))
```

### Analyse

```python
print(agent.ask("Résume les avantages de l'IA générative en 3 points."))
```

---

## 🏗 Architecture

### Modèle

* **Type** : Transformer
* **Paramètres** : ~3.8B
* **Context Window** : 4K tokens
* **Pré-entraînement** : Données multilingues

### Optimisations

* FP16
* Device map automatique (CPU/GPU)
* Mémoire optimisée (chargement adaptatif)

---

## 🌐 Déploiement

### Sur GPU

```python
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agentV1",
    torch_dtype=torch.float16,
    device_map="cuda:0"
)
```

### Sur CPU

```python
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agentV1",
    torch_dtype=torch.float32,
    device_map="cpu"
)
```

### Avec Docker

```dockerfile
FROM python:3.9-slim
RUN pip install transformers torch accelerate
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
```

---

## 📊 Performances

* **Vitesse** : 50–100 tokens/s sur GPU
* **RAM utilisée** : ~3–4 Go en FP16
* **Latence moyenne** : < 2s pour 150–200 tokens

### Cas d’usage recommandés

✔️ Chatbot / conversation
✔️ Génération de texte
✔️ Assistance programmation
✔️ Résumé / analyse
✔️ Q&A général

---

## 🤝 Contribution

1. Fork le projet
2. Crée ta branche : `git checkout -b feature/AmazingFeature`
3. Commit : `git commit -m "Add AmazingFeature"`
4. Push : `git push origin feature/AmazingFeature`
5. Ouvre une Pull Request

### Standards

* Formatage avec **Black**
* Docstrings complètes
* Tests pour les nouvelles features

---

## 📝 License

Projet sous licence **MIT**.
Voir le fichier `LICENSE`.

---

## 👤 Auteur

**Mauricio Mangituka**

* GitHub : [https://github.com/gopu-inc](https://github.com/gopu-inc)
* Hugging Face : [https://huggingface.co/gopu-poss](https://huggingface.co/gopu-poss)
* Email : [mauricio@example.com](mailto:mauricio@example.com)

---

## 🔗 Liens Utiles

* 🤗 Modèle HF : gopu-poss/agentV1
* 🐙 GitHub : gopu-inc/agentV1
* 🐛 Issues : via GitHub
* 📘 Documentation (à venir)

---

<div align="center">

⭐ **Si ce projet vous plaît, pensez à laisser une étoile !**
Développé avec ❤️ par *Mauricio Mangituka* pour **gopuAI**

</div>
