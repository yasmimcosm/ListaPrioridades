import time
import sys

print("=====================================")
print("SISTEMA DE ATENDIMENTO - EMPRESA")
print("=====================================")
situacao = True

while (situacao == True):
    print("[1] Chegada de pessoa para atendimento")
    print("[2] Atender próxima pessoa")
    print("[3] Listar pessoas na fila")
    print("[0] Sair do programa")
    print("\n")

    opcao = input("Escolha uma das opções acima para realizar: ")

    match opcao:
        case "1":
            print("1")
            print("\n")

        case "2":
            print("2")
            print("\n")

        case "3":
            print("3")
            print("\n")

        case "0":
            print("Finalizando...", end="")
            tempo_total = 5
            intervalo = 0.5 
            tempo_decorrido = 0

            while tempo_decorrido < tempo_total:
                for i in range(1, 4):  
                    print("\rFinalizando" + "." * i + " " * (3-i), end="")
                    time.sleep(intervalo)
                    tempo_decorrido += intervalo
                    if tempo_decorrido >= tempo_total:
                        break
            print("Até mais!")
            situacao = False


    