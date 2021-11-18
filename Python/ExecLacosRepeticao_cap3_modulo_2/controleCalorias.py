# Calcular o total de calorias digitadas

# Variavel para armazenar o total de calorias
# Conforme pesquisa, a unidade de medida "caloria" não possui numeros quebrados. Sendo somente inteiros.
qntdCalorias: int = 0
# Recebe o total de alimentos ingeridos
qntdAlimentos: int = int(input("Digite o total de alimentos ingeridos: "))
# Executa uma interação no total de alimentos ingeridos
for i in range(1, qntdAlimentos + 1):
    # Recebe a entrada de calorias para o item atual
    calorias: int = int(input(("Informe as calorias do alimento {}: ".format(i))))
    # Incrementa o total de calorias
    qntdCalorias += calorias

#Exibe as informações totais.
print("Total de alimentos: {}".format(qntdAlimentos))
print("Total de calorias: {}".format(qntdCalorias))