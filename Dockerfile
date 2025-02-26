# Fase 1: Costruzione dell'ambiente base
FROM ubuntu:22.04 AS base

# Impostazioni per evitare errori relativi a `debconf`
ENV DEBIAN_FRONTEND=noninteractive

# Aggiornamento del sistema e installazione delle dipendenze
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    wget \
    git \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Installazione di Ollama
RUN curl https://ollama.ai/install.sh | sh

# Creazione di una directory per l'applicazione
WORKDIR /app

# Copia del file requirements.txt (se necessario)
COPY requirements.txt .

# Installazione delle dipendenze Python
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Fase 2: Copia del codice sorgente
COPY . .

# Impostazione della variabile d'ambiente per attivare il virtualenv
ENV PATH="/app/venv/bin:$PATH"

# Comando di avvio
CMD ["python", "app.py"]

# Puoi testare l'API inviando una richiesta POST a http://localhost:5000/query con un payload JSON contenente il campo prompt.
