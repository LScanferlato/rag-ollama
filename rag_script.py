from ollama import OllamaClient
from transformers import pipeline

# Inizializza il client Ollama
client = OllamaClient(api_url="http://localhost:11434")

# Carica un modello di recupero delle informazioni (RAG)
rag_pipeline = pipeline(
    "retrieval-question-answering",
    model="facebook/dpr-question_encoder-single-nq-base",
    retriever=pipeline(
        "neural-search",
        model="facebook/dpr-ctx_encoder-single-nq-base",
        index_name="my_index",
        use_gpu=False,
    ),
)

# Definisci la domanda da porre
question = "Qual è il capitale dell'Italia?"

# Ottieni la risposta utilizzando il modello RAG
result = rag_pipeline(question)

# Stampa la risposta
print(result['answer'])
