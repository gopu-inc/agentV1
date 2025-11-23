import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from flask import Flask, request, jsonify
import threading
import time

# Configuration
MODEL_NAME = "gopu-poss/agent"
PORT = 4299

# Chargement du modèle
print("🔧 Chargement du modèle agentV1...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("✅ Modèle agentV1 chargé!")

app = Flask(__name__)

def generate_response(prompt, max_tokens=150, temperature=0.7):
    """Génère une réponse avec le modèle"""
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=True,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Nettoyer la réponse
    if prompt in response:
        response = response.replace(prompt, "").strip()
    return response

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint pour discuter avec le modèle"""
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'Aucun message fourni'}), 400
    
    try:
        response = generate_response(message)
        return jsonify({
            'response': response,
            'model': 'agentV1',
            'developer': 'Mauricio Mangituka'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de santé"""
    return jsonify({'status': 'active', 'model': 'agentV1', 'port': PORT})

def terminal_chat():
    """Mode conversation terminal"""
    print("\n" + "="*50)
    print("🤖 agentV1 - Mode Terminal")
    print("Développé par Mauricio Mangituka")
    print("Tapez 'quit' pour quitter")
    print("="*50)
    
    while True:
        try:
            user_input = input("\n👤 Vous: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Au revoir!")
                break
            
            if not user_input:
                continue
                
            print("🤖 agentV1: ", end="", flush=True)
            response = generate_response(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n👋 Arrêt du programme...")
            break
        except Exception as e:
            print(f"\n❌ Erreur: {e}")

def start_flask_server():
    """Démarre le serveur Flask"""
    print(f"🌐 Démarrage du serveur sur le port {PORT}...")
    app.run(host='0.0.0.0', port=PORT, debug=False)

if __name__ == "__main__":
    print("🚀 agentV1 - Service de Chat IA")
    print("Options:")
    print("1. Mode Terminal (tapez 'terminal')")
    print("2. Mode API (tapez 'api')")
    print("3. Les deux (tapez 'both')")
    
    choice = input("\nChoisissez le mode: ").strip().lower()
    
    if choice == 'terminal':
        terminal_chat()
    elif choice == 'api':
        start_flask_server()
    elif choice == 'both':
        # Démarrer le serveur dans un thread séparé
        server_thread = threading.Thread(target=start_flask_server, daemon=True)
        server_thread.start()
        print(f"✅ Serveur API démarré sur http://localhost:{PORT}")
        time.sleep(2)
        terminal_chat()
    else:
        print("❌ Choix invalide. Utilisation du mode terminal par défaut.")
        terminal_chat()
