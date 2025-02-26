import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    # Verifica se il campo 'prompt' è presente nella richiesta
    if not request.is_json:
        return jsonify({"error": "Richiesta non valida. Invia un payload JSON."}), 400
    
    data = request.json
    prompt = data.get('prompt', '')
    
    if not prompt.strip():
        return jsonify({"error": "Il campo 'prompt' è obbligatorio."}), 400
    
    # Invio del prompt a Ollama
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama2', '--verbose', '--interactive=false', prompt],
            capture_output=True,
            text=True
        )
        return jsonify({'response': result.stdout})
    except Exception as e:
        return jsonify({"error": f"Errore durante l'esecuzione di Ollama: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
