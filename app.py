import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    # Verifica se la richiesta è in formato JSON
    if not request.is_json:
        return jsonify({"error": "Richiesta non valida. Invia un payload JSON."}), 400
    
    data = request.json
    prompt = data.get('prompt', '').strip()
    
    if not prompt:
        return jsonify({"error": "Il campo 'prompt' è obbligatorio e non può essere vuoto."}), 400

    try:
        # Invia il prompt a Ollama
        result = subprocess.run(
            ['ollama', 'run', 'llama2', '--verbose', '--interactive=false'],
            input=prompt,
            capture_output=True,
            text=True
        )
        
        # Log degli output di Ollama
        print("Output di Ollama:", result.stdout)
        print("Errori di Ollama:", result.stderr)

        # Restituisci l'output solo se non è vuoto
        if result.stdout.strip():
            return jsonify({'response': result.stdout.strip()})
        else:
            return jsonify({"error": "Ollama non ha restituito alcuna risposta."}), 500

    except Exception as e:
        return jsonify({"error": f"Errore durante l'esecuzione di Ollama: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
