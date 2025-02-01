numero = input("Digite um numero entre 0 e 9999:")
numero = numero.zfill(4)

print(f"""Unidade:{numero[3]}
Dezena:{numero[2]}
Centena:{numero[1]}
Milhar:{numero[0]}""")