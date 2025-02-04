numero = int(input("Digite um numero:"))
conversao = str(input("Para qual base voce quer converter?(binario, octal ou hexadecimal)")).strip().upper()

if conversao == 'BINARIO':
    print(f"""A conversão de {numero} para binario fica {bin(numero)[2:]}""")
elif conversao == 'OCTAL':
    print(f"""A conversão de {numero} para octal fica {oct(numero)[2:]}""")
elif conversao == 'HEXADECIMAL':
    print(f"""A conversão de {numero} para hexadecimal fica {hex(numero)[2:]}""")
else:
    print(f"""Erro!
A conversão {conversao} não existe!""")