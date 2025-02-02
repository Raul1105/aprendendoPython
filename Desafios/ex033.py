n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))

if n1 > n2 and n1 > n3:
    print(f"O maior numero é o {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior numero é o {n2}")
elif n3 > n1 and n3 > n2:
    print(f"O maior numero é o {n3}")

if n1 < n2 and n1 < n3:
    print(f"O menor numero é o {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor numero é o {n2}")
elif n3 < n1 and n3 < n2:
    print(f"O menor numero é o {n3}")