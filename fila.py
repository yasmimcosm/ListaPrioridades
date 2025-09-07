class FilaComPrioridade:
    def __init__(self):
        self.comPrioridade = []
        self.semPrioridade = []
        self.contador_sem_prioridade = 0


    def adicionarPessoa(self, nome, prioridade):
        if prioridade == 1:
            self.comPrioridade.append(nome)
            return True
    
        elif prioridade == 2:
            self.semPrioridade.append(nome)
            return True
        
        else:
            return False


    def atenderPessoa(self):     
            i = 0
            while i < 3:
                if self.comPrioridade:
                    atendido = self.comPrioridade[0]
                    print(f"Atendido(a): {atendido}, com prioridade")
                    self.comPrioridade.remove(atendido)                    
                    
                    j = 0  
                    while j < 2 and self.semPrioridade:
                        atendido = self.semPrioridade[0]
                        print(f"Atendido(a): {atendido}, sem prioridade")
                        self.semPrioridade.remove(atendido)
                        j +=1

                    print("\n")
                    break 

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
        

    def validarNome(self):
        while True:
            nome = input("Qual é o nome da pessoa?: ").strip() 
        
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