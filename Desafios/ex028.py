import random

n = random.randint(0,5)
print(n)
numero = int(input("Tente adivinhar o valor entre 0 e 5:"))

if numero == n:
    print(f"""Você acertou!
numero:{n}""")
else:
    print(f"""Você errou!
Você digitou {numero} e o numero era {n}""")