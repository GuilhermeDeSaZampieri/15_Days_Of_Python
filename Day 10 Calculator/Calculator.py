print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def vezes(a, b):
    return a * b

def divi(a, b):
    return a / b

continuar = True
result = 0

while continuar:
    escolher = input("""
     +
     -
     *
     /
     Escolha sua operação: """)
    if escolher not in ["+", "-", "*", "/"]:
        print("Operação não reconhecida")
        continue

    try:
        if result == 0:
            a = float(input("Digite um número: "))
            b = float(input("Digite outro número: "))
        else:
            a = result
            b = float(input("Digite um número: "))


    except ValueError:
        print("Por favor, digite apenas números.")
        continue

    if escolher == "+":
        result = soma(a, b)
    elif escolher == "-":
        result = sub(a, b)
    elif escolher == "*":
        result = vezes(a, b)
    elif escolher == "/":
        result = divi(a, b)
    print(f"O resultado foi {result:.2f}")
    escolher2 = input("Você deseja continuar com o mesmo resultado 's' ou quer ultilizar um novo 'n'? Para sair digite: 'sair' ").lower()
    if escolher2 == "n":
        result = 0
    elif escolher2 == "sair":
        print("Volte sempre!")
        continuar = False
