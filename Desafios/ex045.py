import random

pc = ["pedra", "papel", "tesoura"]
usuario = str(input("Digite sua escolha(pedra, papel ou tesoura):")).strip().lower()
escolha = random.choice(pc)

if escolha == usuario:
    print(f"Empate! Os dois escolheram {escolha}")
elif escolha == 'pedra' and usuario == 'tesoura':
    print(f"O PC venceu! {escolha} vence {usuario}")
elif escolha == 'pedra' and usuario == 'papel':
    print(f"O usuario venceu! {usuario} vence {escolha}")
elif escolha == 'papel' and usuario == 'tesoura':
    print(f"O usuario venceu! {usuario} vence {escolha}")
elif escolha == 'papel' and usuario == 'pedra':
    print(f"O PC venceu! {escolha} vence {usuario}")
elif escolha == 'tesoura' and usuario == 'pedra':
    print(f"O usuario venceu! {usuario} vence {escolha}")
elif escolha == 'tesoura' and usuario == 'papel':
    print(f"O PC venceu! {escolha} vence {usuario}")
else:
    print(f"Erro! {escolha} não é uma opção!")