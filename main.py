import time
import sys

comPrioridade = []
semPrioridade = []

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
            tempo_total = 5
            intervalo = 0.5 
            tempo_decorrido = 0

            while tempo_decorrido < tempo_total:
                for i in range(1, 4):  
                    print("\r." + "." * i + " " * (3-i), end="")
                    time.sleep(intervalo)
                    tempo_decorrido += intervalo
                    if tempo_decorrido >= tempo_total:
                        break

            print("\r....", end="\n")
            sn = input("A pessoa tem prioridade? [1-Sim / 2-Não]: ")
            if (sn == "1"):
                nome = input("Qual é o nome da pessoa?: ")
                comPrioridade.append(nome)
                print(comPrioridade)
            else:
                nome = input("Qual é o nome da pessoa?: ")
                semPrioridade.append(nome)
                print(semPrioridade)

            time.sleep(5)
            print("\n")

        case "2":
            tempo_total = 5
            intervalo = 0.5 
            tempo_decorrido = 0

            while tempo_decorrido < tempo_total:
                for i in range(1, 4):  
                    print("\r." + "." * i + " " * (3-i), end="")
                    time.sleep(intervalo)
                    tempo_decorrido += intervalo
                    if tempo_decorrido >= tempo_total:
                        break

            print("\r....", end="\n")

            i = 0
            while i < 3:
                if comPrioridade:
                    atendido = comPrioridade[0]
                    print(f"Atendido(a): {atendido}, com prioridade")
                    comPrioridade.remove(atendido)
                    print("\n")
                
                elif semPrioridade:
                    atendido = semPrioridade[0]
                    print(f"Atendido(a): {atendido}, sem prioridade")
                    semPrioridade.remove(atendido)
                    print("\n")

                else:
                    print("Não há mais pessoas para atender!")
                    break
                    print("\n")
                

                i += 1
                time.sleep(3)

        case "3":
            tempo_total = 5
            intervalo = 0.5 
            tempo_decorrido = 0

            while tempo_decorrido < tempo_total:
                for i in range(1, 4):  
                    print("\r." + "." * i + " " * (3-i), end="")
                    time.sleep(intervalo)
                    tempo_decorrido += intervalo
                    if tempo_decorrido >= tempo_total:
                        break

            print("\r....", end="\n")

            print(f"Fila com prioridade no aguardo: {comPrioridade}")
            print(f"Fila sem prioridade no aguardo: {semPrioridade}")
            time.sleep(5)
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


    