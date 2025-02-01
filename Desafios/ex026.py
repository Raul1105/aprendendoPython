frase = input("Digite uma frase: ")
print(f"""A letra 'A' aparece {frase.upper().count("A")}
Aparece a primeira vez na posição:{frase.upper().find("A")}
Aparece pela ultima vez na posicão:{frase.upper().rfind("A")}""")