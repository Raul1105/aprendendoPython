soma = 0
for i in range (0, 6):
    n = int(input("Digite um numero:"))
    if n % 2 == 0:
        soma += n
print(f"A soma dos numeros pares digitados é de {soma}")