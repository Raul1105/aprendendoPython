dc = 60
km = 0.15
dias = int(input("Quantos dias alugados:"))
kmr = float(input("Quantos Km rodados:"))
print(f"O total a pagar é:R${dias*dc + kmr * km:.2f}")