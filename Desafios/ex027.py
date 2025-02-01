nome = input("Digite seu nome:")
dividido = nome.split()
print(f"""Nome: {nome}
Primeiro nome: {dividido[0]}
Ultimo nome: {dividido[len(dividido) - 1]}""")