peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f}, você esta abaixo do peso!")
elif imc >= 18.5 and imc <= 25:
    print(f"Seu IMC é de {imc:.2f} você esta no peso ideal!")
elif imc > 25 and imc <= 30:
    print(f"Seu IMC é de {imc:.2f} você esta com sobrepeso!")
elif imc > 30 and imc <= 40:
    print(f"Seu IMC é de {imc:.2f} você esta com obesidade!")
elif imc > 40:
    print(f"Seu IMC é de {imc:.2f} você esta obesidade morbida!")