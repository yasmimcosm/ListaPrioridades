import time
from fila import FilaComPrioridade

fila = FilaComPrioridade()

def animacao(mensagem="...", tempo_total=3, intervalo=0.5):
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

    opcao = input("Escolha uma das opções acima para realizar: ")

    match opcao:
        case "1":
            animacao("Registrando")
            nome = fila.validarNome()

            while True:
                sn = input("A pessoa tem prioridade? [1-Sim / 2-Não]: ")
                if sn in ["1", "2"]:  
                    sn = int(sn)       
                    break              
                print("Opção inválida! Digite 1 para Sim ou 2 para Não.")

            if fila.adicionarPessoa(nome, sn):
                print(f"{nome} adicionado(a) à fila!")
            else:
                print("Opção Inválida, tente novamente")

            time.sleep(4)
            print("\n")

        case "2":
            if fila.filaVazia():
                print("Não há pessoas para atender!\n")
            else:
                animacao("Chamando")
                fila.atenderPessoa()
                time.sleep(2)


        case "3":
            animacao("Carregando")
            print(f"Fila com prioridade no aguardo: {fila.comPrioridade}")
            print(f"Fila sem prioridade no aguardo: {fila.semPrioridade}")

            time.sleep(4)
            print("\n")

        case "0":
            if not fila.filaVazia():
                print("Ainda há pessoas na fila! Atenda todos antes de sair.")
                time.sleep(4)

            else:
                animacao("Finalizando")
                fila.dadosPessoa()
                print("Até mais!")
                situacao = False
        
        case _:
            print("Opção inválida! Tente novamente.")
            print("\n")


    