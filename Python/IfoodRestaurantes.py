#A avaliação é o determinante para o ranking, ou seja, a maior avaliação ficará
# no topo da lista o desempate ocorrerá pela distância.

#Criação da lista com o nome dos restaurantes + avaliações + distância;
restaurantes = [["Lamen Kazu", 4.8, 0.7],
                ["Mr.Pretzels", 4.8, 0.5],
                ["Brigaderia", 4.8, 1.2],
                ["We Coffe", 4.9, 1.6],
                ["Amor aos Pedaços", 4.8, 1.2],
                ["O Mineiro", 4.2, 1.7]]

notas_restaurantes = []

#permite que a nota seja inserida no final da nossa lista
for notas in restaurantes:
    notas_restaurantes.append(notas[1])

#ordena a lista em ordem crescente
notas_restaurantes.sort()
#inverte a ordem dos elementos da lista
notas_restaurantes.reverse()

ordem_restaurantes = []

# Ordena os restaurantes por nota em ordem decrescente
while len(notas_restaurantes) > 0:
    for restaurante in restaurantes:
        if restaurante[1] == notas_restaurantes[0]:
            ordem_restaurantes.append(restaurante)
            notas_restaurantes.pop(0)

# Trabalhando com a distância
for x in range(1, len(ordem_restaurantes)):
    if ordem_restaurantes[x][1] == ordem_restaurantes[x - 1][1]:
        if ordem_restaurantes[x][2] < ordem_restaurantes[x - 1][2]:
            restaurante_maior_distancia = ordem_restaurantes[x - 1]
            ordem_restaurantes[x - 1] = ordem_restaurantes[x]
            ordem_restaurantes[x] = restaurante_maior_distancia

#Exibir o resultado
print(
    "\nO ranking dos restaurantes com os critérios de notas e distância foi:\n")
for x in range(len(ordem_restaurantes)):
    print("{}° {} | Nota: {} | Distância:  {} Km".format(x + 1, ordem_restaurantes[x][0],
                                                         ordem_restaurantes[x][1],
                                                         ordem_restaurantes[x][2]))