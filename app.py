from flask import Flask, render_template, request, jsonify
import json
import os
import random
import unicodedata
import difflib

arquivo = "memoria.json"
app = Flask(__name__)

# -------------------------
# FUNÇÕES
# -------------------------

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto.strip()

def carregar_memoria():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_memoria(memoria):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=4)

def encontrar_resposta(msg, memoria):
    chaves = memoria.keys()
    parecido = difflib.get_close_matches(msg, chaves, n=1, cutoff=0.6)
    if parecido:
        return parecido[0], random.choice(memoria[parecido[0]])
    return None, None

# -------------------------
# ROTAS FLASK
# -------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg_original = data.get("mensagem", "")
    msg = normalizar(msg_original)
    
    memoria = carregar_memoria()
    respostas_padrao = ["Não entendi muito bem 🤔", "Pode explicar melhor?", "Ainda estou aprendendo 😅"]
    
    chave, resposta = encontrar_resposta(msg, memoria)
    
    if resposta:
        return jsonify({"resposta": resposta})
    else:
        return jsonify({"resposta": random.choice(respostas_padrao)})

@app.route("/ensinar", methods=["POST"])
def ensinar():
    data = request.get_json()
    msg_original = data.get("mensagem", "")
    resposta_nova = data.get("resposta", "")
    
    msg = normalizar(msg_original)
    memoria = carregar_memoria()
    
    if msg in memoria:
        memoria[msg].append(resposta_nova)
    else:
        memoria[msg] = [resposta_nova]
    
    salvar_memoria(memoria)
    return jsonify({"resposta": "Agora aprendi! 🤖"})

# -------------------------
# RODAR APP
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)