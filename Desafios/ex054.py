maior = 0
menor = 0

for i in range (0, 7):
    idade = int(input("Digite o ano de nascimento:"))
    if 2025 - idade < 18:
        menor += 1
    else:
        maior += 1
print(f"""{maior} pessoas são maior de idade e {menor} são menores de idade""")