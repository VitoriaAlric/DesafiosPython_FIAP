# 1 – O projeto HealthTrack é o máximo e tem grande possibilidade de impactar positivamente a vida das pessoas.
# Mesmo que a solução final não utilize uma implementação em Python, podemos aproveitar a oportunidade para desenvolver
# o algoritmo que resolva um problema simples: o cálculo do IMC sem distinção de sexo biológico.
# Por isso, você deve desenvolver um script que solicite o PESO e a ALTURA de uma pessoa.
# A partir disso, o script deva calcular o IMC (PESO dividido pelo quadrado da ALTURA)
# e informar em quais das faixas a pessoa se encontra,

altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))
imc = 0

imc = peso / (altura*altura)

if imc < 16:
    print("Baixo peso Grau III")
elif imc < 16.99:
    print("Baixo peso Grau II")
elif imc < 18.49:
    print("Baixo peso Grau I")
elif imc < 24.99:
    print("Peso ideal")
elif imc < 29.99:
    print("Sobrepeso")
elif imc < 34.99:
    print("Obesidade Grau I")
elif imc < 39.99:
    print("Obesidade Grau II")
elif imc > 40.00:
    print("Obesidade Grau III")

print ("O cálculo do seu IMC atual é: {:.2f}".format(imc))