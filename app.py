from flask import Flask, render_template, request, jsonify
import random
import re
import time
from intencoes import intencoes
from busca_web import buscar_web
from utils import normalizar, resumir

app = Flask(__name__)


PALAVRAS_MATEMATICAS = [
    "quanto é", "calcule", "resultado de",
    "vezes", "x", "mais", "menos", "dividido por"
]

OPERADORES = ["+", "-", "*", "/"]


def extrair_conta(msg):
    msg = msg.lower()

    substituicoes = {
        "quanto é": "",
        "quanto e": "",
        "calcule": "",
        "resultado de": "",
        "vezes": "*",
        "x": "*",
        "mais": "+",
        "menos": "-",
        "dividido por": "/"
    }

    for k, v in substituicoes.items():
        msg = msg.replace(k, v)


    msg = re.sub(r'[^0-9\+\-\*\/\(\)\.\s]', '', msg)

    return msg.strip()



def calcular_matematica(expressao):
    try:
        if re.match(r'^[0-9\+\-\*\/\(\)\.\s]+$', expressao):
            resultado = eval(expressao)
            print("Conta:", expressao, "Resultado:", resultado)  # DEBUG
            return f"O resultado é {resultado}"
    except Exception as e:
        print("Erro:", e)

    return None



def contem_operador(msg):
    return any(op in msg for op in OPERADORES) or any(p in msg for p in PALAVRAS_MATEMATICAS)



def detectar_intencao(msg):
    melhor_intencao = None
    maior_score = 0

    for nome, dados in intencoes.items():
        score = 0

        for palavra in dados["palavras"]:
            if palavra in msg:
                if " " in palavra:
                    score += 2
                else:
                    score += 1

        if score > maior_score:
            maior_score = score
            melhor_intencao = nome

    if maior_score > 0:
        return melhor_intencao

    return None



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    msg_original = data.get("mensagem", "")
    msg = normalizar(msg_original)

    time.sleep(3.5)

    
    intencao = detectar_intencao(msg)
    if intencao:
        return jsonify({
            "resposta": random.choice(intencoes[intencao]["respostas"])
        })

    
    if contem_operador(msg):
        conta = extrair_conta(msg)
        resposta = calcular_matematica(conta)

        if resposta:
            return jsonify({"resposta": resposta})

   
    resposta_web = buscar_web(msg_original)
    if resposta_web:
        return jsonify({"resposta": resumir(resposta_web)})

    
    return jsonify({
        "resposta": "Não consegui encontrar uma resposta."
    })



if __name__ == "__main__":
    app.run(debug=True)