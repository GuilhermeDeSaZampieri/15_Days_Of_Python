import random
random_int = random.randint(0, 1)

#função que retorna "Cara e Coroa"
def CaraOuCoroa(valor):
    #Uso do IF Ternario, que possibilita somente o resultado 1 ou 0
     return "Coroa " if valor == 1 else "Cara"

print(CaraOuCoroa(random_int))
