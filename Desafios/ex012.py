preco = float(input("Digite o preço do produto:R$"))
desconto = preco * 0.05
print(f"Com 5% de desconto o desconto foi de R${desconto:.2f}\nNovo valor do produto:R${preco - desconto:.2f}")