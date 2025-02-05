n = float(input("Digite seu peso:"))
maior = n
menor = n

for i in range (0, 4):
    n = float(input("Digite seu peso:"))
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
print(f"O maior peso foi {maior} e o menor peso foi {menor}")