---
language:
- fr
- en
license: mit
tags:
- text-generation
- conversational
- artificial-intelligence
- gopuAI
- agentV1
pipeline_tag: text-generation
widget:
- text: Bonjour, qui es-tu ?
  example_title: Présentation
- text: Explique-moi l'IA générative
  example_title: Explication IA
- text: Comment programmer en Python ?
  example_title: Aide programmation
datasets:
- unknown
metrics:
- accuracy
model-index:
- name: agentV1
  results:
  - task:
      name: Text Generation
      type: text-generation
    dataset:
      name: Custom Training Data
      type: unknown
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0
base_model:
- microsoft/Phi-3-mini-4k-instruct
new_version: Gopu-poss/gopu-agent-2k-fdf
library_name: transformers
---
# 🤖 agentV1 - Intelligence Artificielle Avancée

**agentV1** est un modèle d'intelligence artificielle de pointe développé par **Mauricio Mangituka** pour **gopuAI**. Basé sur Microsoft Phi-3-mini-4k-instruct, ce modèle combine performance optimale et efficacité mémoire.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-gopu--poss%2Fagent-yellow)
![GitHub](https://img.shields.io/badge/GitHub-gopu--inc%2FagentV1-black)

## 🚀 Caractéristiques

- **🧠 Modèle de base**: Microsoft Phi-3-mini-4k-instruct
- **💾 Taille compacte**: ~2-3 Go seulement
- **⚡ Performances**: Excellentes capacités de raisonnement
- **🌍 Multilingue**: Support du français et de l'anglais
- **🔧 Optimisé**: Quantification et optimisation mémoire

## 📋 Table des Matières

- [Installation](#installation)
- [Utilisation Rapide](#utilisation-rapide)
- [API Complète](#api-complète)
- [Exemples](#exemples)
- [Architecture](#architecture)
- [Déploiement](#déploiement)
- [Contribuer](#contribuer)
- [License](#license)
- [Contact](#contact)

## 🛠 Installation

### Prérequis
- Python 3.8+
- PyTorch 2.0+
- Transformers 4.25+

### Installation des dépendances

```bash
pip install transformers torch accelerate
```

Installation directe

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agent")
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agent",
    torch_dtype=torch.float16,
    device_map="auto"
)
```

🚀 Utilisation Rapide

Code minimal

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Chargement du modèle
tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agent")
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agent",
    torch_dtype=torch.float16,
    device_map="auto"
)

# Génération de texte
prompt = "Explique-moi comment fonctionne l'IA générative"
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7,
        do_sample=True
    )

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

🔌 API Complète

Classe AgentV1

```python
class AgentV1:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agent")
        self.model = AutoModelForCausalLM.from_pretrained(
            "gopu-poss/agent",
            torch_dtype=torch.float16,
            device_map="auto"
        )
    
    def ask(self, question, max_tokens=200, temperature=0.7):
        """Pose une question à l'agent"""
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
        """Pose plusieurs questions en lot"""
        responses = []
        for question in questions:
            responses.append(self.ask(question, max_tokens))
        return responses
```

📚 Exemples

Conversation basique

```python
agent = AgentV1()

# Question simple
response = agent.ask("Bonjour, qui es-tu ?")
print(response)
```

Génération créative

```python
story = agent.ask(
    "Écris une courte histoire sur un robot qui apprend l'émotion",
    max_tokens=300,
    temperature=0.8
)
```

Assistance technique

```python
code_help = agent.ask(
    "Explique-moi comment trier une liste en Python",
    max_tokens=150
)
```

Analyse de texte

```python
analysis = agent.ask(
    "Résume les avantages de l'IA générative en 3 points",
    max_tokens=100
)
```

🏗 Architecture

Modèle de Base

· Architecture: Transformer-based
· Paramètres: 3.8 milliards
· Context Window: 4K tokens
· Pré-entraînement: Texte multilingue

Optimisations

· Quantification: FP16 pour performance mémoire
· Device Mapping: Chargement automatique GPU/CPU
· Gestion mémoire: Optimisée pour usage efficace

🌐 Déploiement

Sur GPU local

```python
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agent",
    torch_dtype=torch.float16,
    device_map="cuda:0"
)
```

Sur CPU

```python
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agent",
    torch_dtype=torch.float32,
    device_map="cpu"
)
```

Avec Docker

```dockerfile
FROM python:3.9-slim
RUN pip install transformers torch accelerate
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
```

📊 Performances

Métriques

· Vitesse d'inférence: ~50-100 tokens/seconde sur GPU
· Utilisation mémoire: ~3-4 Go en FP16
· Latence: < 2 secondes pour 200 tokens

Cas d'Usage Recommandés

· ✅ Assistance conversationnelle
· ✅ Génération de contenu
· ✅ Réponse à questions
· ✅ Analyse de texte
· ✅ Aide à la programmation

🤝 Contribuer

Nous accueillons les contributions ! Voici comment participer :

1. Fork le projet
2. Clone votre fork
3. Créez une branche (git checkout -b feature/AmazingFeature)
4. Commit vos changements (git commit -m 'Add AmazingFeature')
5. Push (git push origin feature/AmazingFeature)
6. Ouvrez une Pull Request

Standards de Code

· Utilisez Black pour le formatage
· Écrivez des docstrings complètes
· Ajoutez des tests pour les nouvelles fonctionnalités

📝 License

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

👨‍💻 Créateur

Mauricio Mangituka

· GitHub: @gopu-inc
· Hugging Face: gopu-poss
· Email: mauricio@example.com

🏢 Société

gopuAI - Innovation en Intelligence Artificielle
Développement de solutions IA accessibles et performantes

🔗 Liens Importants

· 🤗 Hugging Face: gopu-poss/agent
· 🐙 GitHub: gopu-inc/agentV1
· 📚 Documentation: Lien vers documentation
· 🐛 Issues: GitHub Issues

📞 Support

· Questions techniques: Ouvrez une issue sur GitHub
· Collaborations: Contactez-nous par email
· Suggestions: Nous apprécions vos retours !

---

<div align="center">⭐ N'oubliez pas de donner une étoile au projet si vous l'aimez !

Développé avec ❤️ par Mauricio Mangituka pour gopuAI

</div>
```Fichier additionnel : requirements.txt

```txt
torch>=2.0.0
transformers>=4.25.0
accelerate>=0.20.0
numpy>=1.21.0
safetensors>=0.3.0
```

Fichier additionnel : setup.py

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentv1",
    version="1.0.0",
    author="Mauricio Mangituka",
    author_email="mauricio@example.com",
    description="AgentV1 - Modèle IA avancé par gopuAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gopu-inc/agentV1",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.25.0",
        "accelerate>=0.20.0",
    ],
)
```