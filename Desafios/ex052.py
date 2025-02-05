n = int(input("Digite um numero para verificar se é um numero primo:"))

if n % n == 0 and n % 1 == 0 and n % 2 != 0:
    print(f"O numero {n} é primo")
else:
    print(f"O numero {n} não é primo")