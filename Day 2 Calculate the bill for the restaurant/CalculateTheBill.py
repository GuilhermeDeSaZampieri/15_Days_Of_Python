conta = float(input("Boa noite, qual o valor da conta do restaurante? R$"))
gorjeta = int(input("Qual a % de gorjeta que vocês desejam oferecer ao garçom? "))
quantidadePessoas = int(input("Qual a quantidade de pessoas que vão dividir a conta? "))
resultadoConta = (conta + (conta * (gorjeta*0.01))) / quantidadePessoas

print(f"\nA conta no valor de R$ {conta:.2f}," 
      f" divido entre {quantidadePessoas} pessoas,"
      f" com uma gorjeta de {gorjeta}% para o garçom."
      f"\nFoi de R$ {resultadoConta:.2f} para cada pessoa")



