print("Digite 3 comprimentos para verificar se elas podem formar um triangulo")
a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))

if a + b > c and a + c > b and b + c > a:
    print(f"Os valores {a}, {b} e {c} podem formar um triangulo!")
else:
    print(f"Os valores {a}, {b} e {c} não podem formar um triangulo!")