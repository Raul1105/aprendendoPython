n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))
n3 = int(input("Digite o terceiro valor:"))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print(f"Os valores {n1}, {n2} e {n3} podem formar um triangulo!")
    if n1 == n2 and n1 == n3 and n2 == n3:
        print(f"""Os valores formam um triangulo equilatero!""")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print(f"Os valores formam um triangulo isosceles!")
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print(f"Os valores formam um triangulo escaleno!")
else:
    print(f"Os valores não podem formar um triangulo!")