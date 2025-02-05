mi = 0
nmv = ""
imv = 0
mm = 0

for i in range (0,4):
    nome = str(input("Digite o nome:")).strip().capitalize()
    idade = int(input("Digite a idade:"))
    sexo = str(input("Digite o sexo:")).strip().lower()

    mi += idade
    if sexo == 'masculino' and idade > imv:
        nmv = nome
        imv = idade
    
    if sexo == 'feminino' and idade < 20:
        mm += 1

print(f"""A media de idade do grupo é {round(mi / 4)} anos
O nome do homem mais velho é {nmv} e tem {imv} anos
{mm} mulheres tem menos de 20 anos""")