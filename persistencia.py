import json
import os

tarefas = []

def carregar_tarefas():

    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r", encoding="utf-8") as arquivo_aberto:
            tarefas_carregadas = json.load(arquivo_aberto)
    else:
        tarefas_carregadas = []

    return tarefas_carregadas


def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo_aberto:
       json.dump(tarefas, arquivo_aberto, ensure_ascii=False, indent=4) 
    