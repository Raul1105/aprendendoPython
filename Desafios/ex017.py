import math

catetoOposto = float(input("Digite o cateto oposto:"))
catetoAdjacente = float(input("Digite o cateto adjacente:"))
print(f"Cateto oposto:{catetoOposto}, cateto adjacente:{catetoAdjacente} \nO comprimento da hipotenusa é {math.hypot(catetoOposto, catetoAdjacente):.2f}")