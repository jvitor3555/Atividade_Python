nome = str(input("Informe um nome, por favor: "))

for teste in range(len(nome) -1, -1, -1):
    novo_nome = nome[teste]
    print(novo_nome)