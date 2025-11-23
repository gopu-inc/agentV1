## troubleshooting
# Dépannage

## Problème : CUDA non détecté
```python
torch.cuda.is_available()
```
→ Installer drivers + CUDA Toolkit

---

## Problème : Out of Memory
```yml
Solutions :
- Baisser max_new_tokens
- Passer torch_dtype en float16
- Utiliser CPU offload
```
---

## Problème : Lenteur CPU

Le modèle a 3.8B paramètres → CPU lent.  
Utilisez un GPU.
