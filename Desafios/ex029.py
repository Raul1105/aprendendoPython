velocidade = int(input("Digite a velocidade:"))

if velocidade > 80:
    velocidade = velocidade - 80
    print(f"""Você foi multado!
Valor da multa:R${velocidade * 7}""")
else:
    print("Você esta dentro do limite da via")