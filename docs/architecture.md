![agent Banner](https://github.com/user-attachments/assets/fd16ab2d-71bd-4300-b495-73d573044325)


# 📄 `architecture.md`


# Architecture de agentV1

## Modèle de base

- Type : Transformer Decoder
- Paramètres : ~3.8B
- Contexte : 4096 tokens
- Pré-entraînement : corpus multilingue
- Famille : Microsoft Phi-3 Mini

---

## Optimisations apportées

- Quantification FP16
- Accélération via `accelerate`
- Memory-efficient attention
- Tokenizer optimisé pour FR/EN
- Auto device mapping

---

## Composants internes

- Embeddings
- Multi-head Attention
- FFN optimisé
- Cache KV
- Générateur de tokens

---

## Pourquoi Phi-3 ?

- Excellent ratio performance / taille
- Très rapide sur GPU modestes
- Idéal pour agents, chatbots, assistants
📄 6. docs/examples.md
# Exemples pratiques

## Résumé de texte

```python
agent.ask("Résume ce texte : ...")
Génération d’histoires
agent.ask(
    "Écris une histoire sur un robot qui apprend l'humour",
    max_tokens=300,
    temperature=0.9
)
Aide à la programmation
agent.ask("Montre-moi comment utiliser les dictionnaires en Python.")
Analyse de texte
agent.ask("Donne-moi 3 points importants du texte suivant : ...")
