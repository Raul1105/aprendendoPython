idade = int(input("Digite a sua idade:"))

if idade < 18:
    print(f"Você ainda devera se alistar daqui a {18 - idade} anos!")
elif idade == 18:
    print(f"Ja esta na hora de se alistar!")
else:
    print(f"Você ja deveria ter se alistado ha {idade - 18} anos!")