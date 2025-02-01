nome = input("Digite seu nome completo:")
dividido = nome.split()

print(f"""Seu nome com todas as letras maiusculas:{nome.upper()}
Seu nome com todas minusculas:{nome.lower()}
Quantas letras possui:{len(nome.replace(" ", ""))}
Quantas letra tem no primeiro nome:{len(dividido[0])}""")