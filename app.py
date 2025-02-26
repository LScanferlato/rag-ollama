import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    prompt = data.get('prompt', '')
    
    # Invio del prompt a Ollama
    result = subprocess.run(
        ['ollama', 'run', 'llama2', '--verbose', '--interactive=false', prompt],
        capture_output=True,
        text=True
    )
    
    return jsonify({'response': result.stdout})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)