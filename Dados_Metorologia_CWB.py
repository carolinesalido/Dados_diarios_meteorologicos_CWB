import requests
import json
from datetime import datetime
import os

API_KEY = "f661a49e95ad27bcedd6de8cf923bba5"
URL = f"https://api.openweathermap.org/data/2.5/weather?q=Curitiba,BR&appid={API_KEY}&units=metric&lang=pt_br"
ARQUIVO_JSON = "dados_diarios.json"


def dados_curitiba():
    resposta = requests.get(URL)
    if resposta.status_code == 200:
        dados = resposta.json()
        clima = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperatura": dados["main"]["temp"],
            "sensacao_termica": dados["main"]["feels_like"],
            "umidade": dados["main"]["humidity"],
            "descricao": dados["weather"][0]["description"],
        }
        return clima
    else:
        print("Erro ao consultar API:", resposta.status_code)
        return None


def salvar_dados(dados_novos):
    if not dados_novos:
        return

    if not os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump([dados_novos], f, ensure_ascii=False, indent=4)
    else:
        # Lê o arquivo existente e adiciona o novo dado
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            dados_existentes = json.load(f)

        dados_existentes.append(dados_novos)

        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(dados_existentes, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    info = dados_curitiba()
    salvar_dados(info)
    print("Dados meteorológicos salvos com sucesso!")
