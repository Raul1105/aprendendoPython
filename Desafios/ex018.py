import math

angulo = int(input("Digite o angulo:"))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"O angulo dado foi:{angulo}\nSeu seno é:{seno:.2f}, cosseno:{cosseno:.2f} e a tangente:{tangente:.2f}")