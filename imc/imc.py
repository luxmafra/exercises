peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO NORMAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
