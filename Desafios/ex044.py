valor = float(input("Informe o valor do produto:R$"))
pagamento = str(input("Informe a forma de pagamento:")).strip().lower()
parcelas = 0

if pagamento == 'dinheiro' or pagamento == 'cheque':
    print(f"""Seu pagamento tera 10% de desconto!
O valor de R${valor:.2f} com 10%({valor * 0.10}) de desconto fica R${valor - (valor * 0.10):.2f}""")
elif pagamento == "cartao":
    pagamento = str(input("Ira parcelar?")).strip().lower()
    if pagamento == 'nao':
        print(f"""Seu pagamento tera 5% de desconto!
O valor de R${valor:.2f} com 5%({valor * 0.05}) de desconto fica R${valor - (valor *0.05):.2f}""")
    if pagamento == 'sim':
        parcelas = int(input("Quantas parcelas:"))
        if parcelas <= 2:
            print(f"""Seu pagamento não tera desconto!
Valor da compra de R${valor:.2f}""")
        elif parcelas >= 3:
            print(f"""Seu pagamento tera um juros de 20%!
O valor de R${valor:.2f} com juros de 20%({valor * 0.20}) fica R${valor + (valor * 0.20):.2f}""")