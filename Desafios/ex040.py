n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1 + n2) / 2

if media < 5:
    print(f"""A sua media foi de {media:.1f}!
Você esta reprovado!""")
elif media > 5 and media < 6.9:
    print(f"""A sua media foi de {media:.1f}
Você esta de recuperação!""")
else:
    print(f"""Sua media foi de {media}
Você esta aprovado!""")