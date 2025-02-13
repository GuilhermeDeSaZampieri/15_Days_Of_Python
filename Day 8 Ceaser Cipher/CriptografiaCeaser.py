alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

def decodificar_codificar(var, escolher, distancia):
    if escolher == "descodificar":
        distancia *= -1
    for a in var:
        if a in alfabeto:
            index = alfabeto.index(a)
            novoIndex = (index + distancia) % 26
            palavraCodificadaDecodificada.append(alfabeto[novoIndex])
        else:
            palavraCodificadaDecodificada.append(a)

    return palavraCodificadaDecodificada


continuar = True

while continuar:
    escolha = input("Para escolher uma das opções: 'codificar' ou 'descodificar', digite conforme é solicitado\n ").lower()
    if escolha not in ["codificar", "descodificar"]:
        print("Opção invàlida")
        continue

    novaPalavra = []
    palavra = input("informe uma palavra\n").lower()
    numShift = int(input("informe um numero\n"))

    for a in range(len(palavra)):
        novaPalavra += palavra[a]

    palavraCodificadaDecodificada = []

    print("Palavra de Caeser Cipher: " + ("".join(decodificar_codificar(novaPalavra, escolha, numShift))))

    querContinuar = input("Digite: 'sim' se você deseja continuar, caso contrário digite: 'nao'\n ").lower()
    if querContinuar == "sim":
        continuar = True
    elif querContinuar == "nao":
        print("Volte sempre!")
        continuar = False


