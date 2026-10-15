from persistencia import salvar_tarefas, carregar_tarefas

tarefas_teste = [
    {
        "id": 1,
        "desc": "Estudar Python",
        "concluido": False
    }
]

salvar_tarefas(tarefas_teste)

tarefas_carregadas = carregar_tarefas()

assert tarefas_carregadas == tarefas_teste

print("Todos os testes passaram!")