salario = float(input("Digite o salario do funcionario:R$"))

if salario > 1250:
    print(f"O salario de R${salario} com aumento de 10%(R${salario * 0.10:.2f}) fica:R${(salario * 0.10) + salario:.2f}!")
else:
    print(f"O salario de R${salario} com aumento de 15%(R${salario * 0.15:.2f} fica:R${(salario * 0.15) + salario:.2f})!")