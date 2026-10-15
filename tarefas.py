from persistencia import carregar_tarefas, salvar_tarefas

tarefas = carregar_tarefas()

def add_tarefas():
    status = False
    proximo_id = verificar_lista()

    while not status:
        print("Gerenciador de tarefas")
        
        
        tarefa = input("Digite a descrição da tarefa: ").strip()

        if not tarefa:
            print("A descrição da tarefa não pode estar vazia!")
            continue

        item = {
            "id": proximo_id,
            "desc": tarefa,
            "concluido": False
        }

        proximo_id = proximo_id + 1

        tarefas.append(item)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada!")

        status2 = False
        while not status2:
            questao = input("Deseja adicionar mais itens? (sim/não): ").lower().strip()
 
                       
            if questao in ("sim", "s"):
                status = False
                status2 = True
            elif questao in ("não", "nao", "n"):
                status = True
                status2 = True
            else:
                print("Digite sim ou não!")
            
    print("Lista de tarefas:", tarefas)


def listar_tarefas():

    quant_lista = len(tarefas)
    if quant_lista == 0:
        print("lista vazia")
    else:
        for i in range(len(tarefas)):
            print(tarefas[i])
        print("lista finalizada")



def concluir_tarefa():

    if not tarefas:
        print("Não existem tarefas cadastradas!")
        return

    verificar = False
    while not verificar:
        try:
            id_tarefa_con = int(input("Digite o ID da tarefa que deseja concluir: "))
            if id_tarefa_con <= 0:
                print("Digite um valor numerico positivo!")
                continue

            verificar = True
            
        except ValueError:
            print("Digite um ID numerico valido!")
        

    encontrou = False

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa_con:
            encontrou = True

            if not tarefa["concluido"] :
                tarefa["concluido"] = True
                salvar_tarefas(tarefas)
                print("Tarefa concluída!")
            else:
                print("Essa tarefa já está concluída!")

            break

    if encontrou == False:
        print("Tarefa não encontrada!")



def remover_tarefa():

    if not tarefas:
        print("Não existem tarefas cadastradas!")
        return

    verificar = False
    while not verificar:
        try:
            id_tarefa_rem = int(input("Digite o ID da tarefa que deseja remover: "))
            if id_tarefa_rem <= 0:
                print("Digite um valor numerico positivo!")
                continue

            verificar = True   

        except ValueError:
            print("Digite um ID numerico valido!")

    encontrou = False
    
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa_rem:
            encontrou = True
            tarefas.remove(tarefa)
            salvar_tarefas(tarefas)
            print("Tarefa removida com sucesso")
            break

    if encontrou == False:
       print("tarefa não encotrada")

def verificar_lista():

    if not tarefas:
        proximo_id = 1
    else:
        maior_id = 0
        for tarefa in tarefas:
            if tarefa["id"] > maior_id:
                maior_id = tarefa["id"]
        
        proximo_id = maior_id + 1

    return proximo_id

