frase = str(input("Digite uma frase para verificar se é um palindromo:")).upper()
fs = frase.replace(" ", "")[::-1]
fse = frase.replace(" ","")
print(f"{frase}{fs}{fse}")
if fse == fs:
    print(f"A frase é um palindromo")
else:
    print("A frase não é um palindromo")