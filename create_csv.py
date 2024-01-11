import csv

# Dados fictícios
dados = [
    ["nome", "e-mail", "data_nascimento", "celular"],
    ["João Silva", "joao.silva@email.com", "01/05/1980", "(11) 98765-4321"],
    ["Maria Oliveira", "maria.oliveira@email.com", "15/08/1992", "(21) 97654-3210"],
    ["Lucas Santos", "lucas.santos@email.com", "10/11/1985", "(31) 96543-2109"],
    ["Ana Pereira", "ana.pereira@email.com", "05/03/1998", "(41) 95432-1098"],
    ["Pedro Costa", "pedro.costa@email.com", "20/07/1982", "(51) 94321-0987"],
    ["Laura Lima", "laura.lima@email.com", "12/09/1990", "(61) 93210-9876"],
    ["Carlos Oliveira", "carlos.oliveira@email.com", "28/04/1975", "(71) 92109-8765"],
    ["Mariana Souza", "mariana.souza@email.com", "02/12/1988", "(81) 91087-6543"],
    ["Roberto Martins", "roberto.martins@email.com", "18/06/1995", "(91) 90987-6543"],
    ["Juliana Silva", "juliana.silva@email.com", "25/01/1984", "(01) 90098-7654"],
]


# Nome do arquivo CSV
nome_arquivo = "dados.csv"

# Criar e escrever no arquivo CSV
with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)

print(f"Arquivo CSV '{nome_arquivo}' criado com sucesso.")
