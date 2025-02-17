import os
pessoas = []

escolher = ""
continuar = True
maior = 0
contador = 0
print("bem vindo ao leilão online!")

while continuar:

    nome = input("Digite seu nome:\n")
    oferta = float(input("Digite a sua oferta\n"))
    pessoas.append({"nome": nome, "oferta": oferta})

    if oferta > maior:
        maior = oferta
        contador = len(pessoas) -1

    escolher = input("Mais alguém vai ofertar? 'sim' 'nao'").lower()
    if escolher == "sim":
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

    if escolher == "nao":
        print("Volte sempre")
        continuar = False

print(f'Parabéns {pessoas[contador]["nome"]} o valor da sua oferta foi o maior R${pessoas[contador]["oferta"]:.2f} ')


