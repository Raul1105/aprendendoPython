print("Viagens ate 200km é cobrado R$0,50 por Km e acima de 200km é cobrado R$0,45.")
km = float(input("Digite a distancia da viagem em Km:"))

if km <= 200:
    print(f"A sua viagem com {km}km ficara no valor de R${km * 0.50:.2f}")
else:
    print(f"A sua viagem com{km}km ficara no valor de R${km * 0.45:.2f}")