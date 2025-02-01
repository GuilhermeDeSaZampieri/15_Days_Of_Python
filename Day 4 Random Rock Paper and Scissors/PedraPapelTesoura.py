rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Vs = '''
 █████   █████  █████████ 
░░███   ░░███  ███░░░░░███
 ░███    ░███ ░███    ░░░ 
 ░███    ░███ ░░█████████ 
 ░░███   ███   ░░░░░░░░███
  ░░░█████░    ███    ░███
    ░░███     ░░█████████ 
     ░░░       ░░░░░░░░░  '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
r = random
#Lista que armazena cada uma das imagens
Decisao = [rock, paper, scissors]

print("Bem vindo ao Jogo de Pedra, Papel e Tesoura")
escolha = int(input("0 - Pedra | 1 - Papel | 2 - Tesoura\n"))
EscolhaDoPC = r.randint(0,2)

print(f"{Decisao[escolha]}\n {Vs}\n {Decisao[EscolhaDoPC]} ")

if escolha == 0 and EscolhaDoPC == 0 or escolha == 1 and EscolhaDoPC == 1 or escolha == 2 and EscolhaDoPC == 2:
    print("Resultado =  Empate")
elif escolha == 0 and EscolhaDoPC == 1 or escolha == 1 and EscolhaDoPC == 2 or escolha == 2 and EscolhaDoPC == 0:
    print("Resultado = Você Perdeu")
elif escolha == 0 and EscolhaDoPC == 2 or escolha == 1 and EscolhaDoPC == 0 or escolha == 2 and EscolhaDoPC == 1:
    print("Resultado =  Você Ganhou")

