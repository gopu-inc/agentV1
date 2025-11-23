import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Chargement du modèle
print("Chargement agentV1...")
tokenizer = AutoTokenizer.from_pretrained("gopu-poss/agent")
model = AutoModelForCausalLM.from_pretrained(
    "gopu-poss/agent",
    torch_dtype=torch.float16,
    device_map="auto"
)
print("✅ Prêt!")

print("\n🤖 agentV1 - Tapez 'quit' pour quitter\n")

while True:
    user_input = input("👤 Vous: ")
    
    if user_input.lower() in ['quit', 'exit']:
        break
        
    inputs = tokenizer(user_input, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            do_sample=True
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"🤖 agentV1: {response}\n")
