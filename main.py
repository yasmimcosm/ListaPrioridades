import time
import sys
from fila import FilaComPrioridade

fila = FilaComPrioridade()
comPrioridade = []
semPrioridade = []

def animacao(mensagem="...", tempo_total=3, intervalo=0.5):
    """Animação simples de pontinhos"""
    tempoDecorrido = 0
    while tempoDecorrido < tempo_total:
        for i in range(1, 4):
            print("\r" + mensagem + "." * i + " " * (3 - i), end="")
            time.sleep(intervalo)
            tempoDecorrido += intervalo
            if tempoDecorrido >= tempo_total:
                break
    print("\r" + mensagem + "...", end="\n")



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
            animacao("Registrando")

            sn = input("A pessoa tem prioridade? [1-Sim / 2-Não]: ")
            nome = input("Qual é o nome da pessoa?: ")
            fila.adicionarPessoa(nome, prioridade=(sn == "1"))
            print(f"{nome} adicionado(a) à fila!")
            time.sleep(5)
            print("\n")

        case "2":
            animacao("Chamando")
            print(fila.atenderPessoa())
            time.sleep(5)

        case "3":
            animacao("Carregando")
            comPrioridade, semPrioridade = fila.listar_fila()
            print(f"Fila com prioridade no aguardo: {comPrioridade}")
            print(f"Fila sem prioridade no aguardo: {semPrioridade}")
            time.sleep(5)
            print("\n")

        case "0":
            if not fila.filaVazia():
                print("Ainda há pessoas na fila! Atenda todos antes de sair.")
            else:
                animacao("Finalizando")
                print("Até mais!")
                situacao = False
        
        case _:
            print("Opção inválida! Tente novamente.")
            print("\n")


    