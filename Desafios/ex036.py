valorCasa = float(input("Digite o valor da casa:R$"))
salario = float(input("Qual seu salario:R$"))
anos = int(input("Em quantos anos ira pagar:"))
meses = anos * 12
prestacao = valorCasa / meses
print(meses)
print(prestacao)

if prestacao > salario * 0.30:
    print(f"""Emprestimo negado!
O valor da prestação de R${prestacao:.2f} excede 30% do salario de R${salario:.2f}
O limite da parcela seria de {salario * 0.30:.2f}""")
else:
    print(f"""Emprestimo aprovado!
A casa no valor de R${valorCasa:.2f} sera paga em {meses:.2f}x de R${prestacao:.2f}!""")