class FilaComPrioridade:
    def __init__(self):
        self.comPrioridade = []
        self.semPrioridade = []
        self.totalAtendidos = 0
        self.atendidosComPrioridade = 0
        self.atendidosSemPrioridade = 0


    def adicionarPessoa(self, nome, prioridade):
        if prioridade == 1:
            self.comPrioridade.append(nome)
    
        elif prioridade == 2:
            self.semPrioridade.append(nome)
        
        else:
            return False
        
        return True

    def atenderPessoa(self):     
            i = 0
            while i < 3:
                if self.comPrioridade:
                    atendido = self.comPrioridade[0]
                    print(f"Atendido(a): {atendido}, com prioridade")
                    self.comPrioridade.remove(atendido)                    
                    self.atendidosComPrioridade += 1
                    self.totalAtendidos += 1

                    j = 0  
                    while j < 2 and self.semPrioridade:
                        atendido = self.semPrioridade[0]
                        print(f"Atendido(a): {atendido}, sem prioridade")
                        self.semPrioridade.remove(atendido)
                        self.atendidosSemPrioridade += 1
                        self.totalAtendidos += 1
                        j +=1

                    print("\n")
                    break 

                elif self.semPrioridade:
                    atendido = self.semPrioridade[0]
                    print(f"Atendido(a): {atendido}, sem prioridade")
                    self.semPrioridade.remove(atendido)
                    self.atendidosSemPrioridade += 1
                    self.totalAtendidos += 1
                    print("\n")

                else:
                    print("Não há mais pessoas para atender!")
                    print("\n")
                    break

                i += 1
        

    def validarNome(self):
        while True:
            nome = input("Qual é o nome da pessoa?: ").strip().title()
        
            if not nome:
                print("Nome inválido! Digite novamente.")
                continue

            if not all(c.isalpha() or c.isspace() for c in nome):
                print("Nome inválido! Use apenas letras.")
                continue
            
            return nome
        

    def listarFila(self):
        return (self.comPrioridade, self.semPrioridade)

    def filaVazia(self):
        return not self.comPrioridade and not self.semPrioridade
    
    def dadosPessoa(self):
        print("=== Estatísticas de atendimento ===")
        print(f"Total de pessoas atendidas: {self.totalAtendidos}")
        if self.totalAtendidos > 0:
            print(f"Com prioridade: {self.atendidosComPrioridade / self.totalAtendidos * 100:.1f}%")
            print(f"Sem prioridade: {self.atendidosSemPrioridade / self.totalAtendidos * 100:.1f}%")