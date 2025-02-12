import random
import Stages
sta = Stages

frutas  = ["morango","melancia","uva","laranja","pera","banana","pessego"]

word = frutas[random.randint(0,2)]
print("O tema é frutas: ",frutas)

palavraDesc= ["_"]* len(word)
print("".join(palavraDesc))

dead = False
contDead = 6
contErro = 0
while dead == False:

    
    print(sta.corpo[contDead])
    if contDead == 0:
        print("Você faleceu")
        dead = True
        continue

    palaRep = []
    var = input("digite uma letra:\n").lower()
    for p in range(len(word)):

        if var == palavraDesc[p]:
            palaRep = [palavraDesc[p]]
        elif var == word[p]:
            palavraDesc[p]  = var
        else:
            contErro += 1
    if len(palaRep) > 0:
        print(f"A letra {palaRep} ja foi escrita")
    if ("".join(palavraDesc)) == word:
        print("Parabéns você venceuu!")
        dead = True

    if contErro == len(word):
        contDead -= 1

    contErro = 0
    print("".join(palavraDesc))