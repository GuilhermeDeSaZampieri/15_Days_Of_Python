print("Bem vindo a caça ao tesouro!\nVocê está em um labirinto, por onde você deseja ir? 'Direita' 'Esquerda' ")
direcao = input().upper()

if direcao == "DIREITA":
    print("Game over")
elif direcao == "ESQUERDA":
    direcao = input(
        "\nParabéns, você passou da 1º fase!\nAgora por qual direção você deseja ir? 'Direita' 'Esquerda'\n").upper()
    if direcao == "DIREITA":
        print("Game over")
    elif direcao == "ESQUERDA":
        direcao = input(
            "\nParabéns, você passou da 2º fase!\nAgora por qual porta você deseja ir? 'Direita' 'Esquerda' 'Meio'\n").upper()
        if direcao == "DIREITA":
            print("Game over")
        elif direcao == "ESQUERDA":
            print("Game over")
        elif direcao == "MEIO":
            print("\nVocê venceu!! Parabéns!!")
            print('''                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.   hjw''')
