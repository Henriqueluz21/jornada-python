
from tarefas import add_tarefas, listar_tarefas, concluir_tarefa, remover_tarefa

def menu():
    
   sair = False
   while sair == False:
       print("opção 1: add tarefa")
       print("opção 2: Listar tarefas")
       print("opção 3: concluir tarefa")
       print("opção 4: remover tarefa")
       print("opção 0: sair")
       opcao = input("digite a opção que deseja:")
   
       match opcao:
            case "1":
                add_tarefas()
            case "2":
                listar_tarefas()
            case "3":
                concluir_tarefa()
            case "4":
                remover_tarefa()
            case "0":
                op = input("deseja realmente sair? (sim/não): ")
                if op.lower() == "sim":
                    sair = True
            case _:
                print("opção invalida")

if __name__ == "__main__":
    menu()                
