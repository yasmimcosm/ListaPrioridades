class FilaComPrioridade:
    def __init__(self):
        self.comPrioridade = []
        self.semPrioridade = []
        self.contador_sem_prioridade = 0

    def adicionarPessoa(self, nome, prioridade):
        if prioridade:
            self.comPrioridade.append(nome)
        else:
            self.semPrioridade.append(nome)

    def atenderPessoa(self):
        i = 0
        while i < 3:
            if self.comPrioridade:
                atendido = self.comPrioridade[0]
                print(f"Atendido(a): {atendido}, com prioridade")
                self.comPrioridade.remove(atendido)                    
                print("\n")
                
            elif self.semPrioridade:
                atendido = self.semPrioridade[0]
                print(f"Atendido(a): {atendido}, sem prioridade")
                self.semPrioridade.remove(atendido)
                print("\n")

            else:
                print("Não há mais pessoas para atender!")
                print("\n")
                break
            
            i += 1
            
    def listarFila(self):
        return (self.comPrioridade, self.semPrioridade)

    def filaVazia(self):
        return not self.comPrioridade and not self.semPrioridade