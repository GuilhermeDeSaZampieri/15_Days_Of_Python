print("Bem vindo a pizzaria python!")
size = input("Qual tamanhao você quer? G, M ou P: ").upper()
pepperoni = input("Você quer peperoni na sua pizza? S ou N: ").upper()
extra_cheese = input("Você quer queijo extra? S ou N: ").upper()

bill = 0
if size == "G":
    bill += 25
    if pepperoni == "S":
        bill += 3
elif size == "M":
    bill += 20
    if pepperoni == "S":
        bill += 3
elif size == "P":
    bill += 15
    if pepperoni == "S":
        bill += 2

if extra_cheese == "S":
    bill += 1

print(f"O valor da pizza foi de:  R${bill:.2f}")