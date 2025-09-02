# Sistema de Atendimento com Fila de Prioridade

![Python](https://img.shields.io/badge/Python-blue)
![GitHub](https://img.shields.io/badge/GitHub-ControleEstoque-green)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)

---

## 📌 Descrição do Projeto
Este projeto implementa um **Tipo Abstrato de Dados (TAD) Fila com Prioridades** para controlar o atendimento de pessoas em uma empresa, seguindo a política **1 pessoa com prioridade e 2 pessoas sem prioridade**.  

O sistema permite:
- Registrar a chegada de pessoas;
- Realizar atendimentos obedecendo a política definida;
- Listar a fila atual;
- Apresentar estatísticas ao final do atendimento.

---

## ⚙️ Funcionalidades
- **Chegada de pessoa**: Adiciona uma pessoa à fila, informando se possui prioridade ou não.  
- **Atendimento**: Realiza atendimentos seguindo a política **1com2sem**, considerando a disponibilidade de cada tipo de fila.  
- **Listar fila**: Exibe todas as pessoas na fila, indicando se são com ou sem prioridade.  
- **Controle de saída**: Impede que o programa seja finalizado enquanto houver pessoas na fila.  
- **Estatísticas finais**:
  - Total de pessoas atendidas;  
  - Percentual de atendimentos com prioridade;  
  - Percentual de atendimentos sem prioridade.  

---

## 🛠️ Tecnologias
- Linguagem: **Python** (ou outra escolhida pelo grupo)  
- Estrutura de dados: **Array com redimensionamento** ou **Lista Encadeada Simples** (definida por sorteio)

---

## 📁 Estrutura do Projeto

```
projeto-fila-prioridade/
│
├── main.py # Programa principal com menu e controle da fila
├── fila.py # Implementação do ADT Fila com Prioridade
├── pessoa.py # Classe Pessoa com atributos: nome e prioridade
├── README.md # Este arquivo
└── relatorio.pdf # Relatório técnico do projeto
```


---
# Colaboração em Grupo

O projeto foi dividido para facilitar a colaboração entre duas pessoas:

## Pessoa 1
1. Implementação do ADT Fila com Prioridade (fila.py).
2. Métodos:
   - adicionar_pessoa(pessoa).
   - atender_pessoa().
   - listar_fila().
   - Estatísticas de atendimentos.
5. Estrutura interna da fila (array ou lista encadeada).
6. Controle da política 1com2sem.

## Pessoa 2

1. Implementação da interface cliente (main.py).
   - Menu interativo
   - Entrada de dados (nome e prioridade)
   - Chamadas para os métodos do ADT
   - Validação de entrada
6. Listagem da fila e exibição de estatísticas finais
7. Garantir que o programa não saia com pessoas na fila

## Entregáveis
- Código-fonte completo
- Relatório técnico (máx. 3 páginas)
- Descrever decisões de projeto
- Explicar a escolha entre array ou lista encadeada
- Vídeo de apresentação (máx. 3 minutos)
- Demonstrar funcionamento do sistema
- Mostrar política de atendimento e estatísticas finais
