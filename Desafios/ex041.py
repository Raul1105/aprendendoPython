anoNascimento = int(input("Digite o ano do seu nascimento:"))
idade = 2025 - anoNascimento

if idade <= 9:
    print(f"Você esta na categoria mirim por ter {idade} anos!")
elif idade > 9 and idade <= 14:
    print(f"Você esta na categoria infantil por ter {idade} anos!")
elif idade > 14 and idade <= 19:
    print(f"Você esta na categoria junior por ter {idade} anos!")
elif idade == 20:
    print(f"Você esta na categoria senior por ter {idade} anos!")
else:
    print(f"Você esta na categoria master por ter {idade} anos!")