from flask import Flask, render_template, jsonify
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

ARQUIVO_JSON = "consultas.json"
API_KEY = "f661a49e95ad27bcedd6de8cf923bba5"
LAT, LON = -25.4284, -49.2733

def consultar_dados():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    dados = resposta.json()
    return {
        "cidade": dados["name"],
        "temperatura": dados["main"]["temp"],
        "condicao": dados["weather"][0]["description"],
        "icone": dados["weather"][0]["icon"],
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

def salvar_consulta(dados):
    if not os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "w") as f:
            json.dump([], f)
    with open(ARQUIVO_JSON, "r") as f:
        historico = json.load(f)
    historico.append(dados)
    with open(ARQUIVO_JSON, "w") as f:
        json.dump(historico, f, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dados")
def dados():
    info = consultar_dados()
    salvar_consulta(info)
    with open(ARQUIVO_JSON, "r") as f:
        historico = json.load(f)
    return jsonify({
        "dados": info,
        "consultas": len(historico)
    })

if __name__ == "__main__":
    app.run(debug=True)
