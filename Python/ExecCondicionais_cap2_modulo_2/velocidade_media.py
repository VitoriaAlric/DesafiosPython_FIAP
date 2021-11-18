#Esse programa recebe a diantancia do tempo e calcula a velocidade média
#Primeiro vamos pedir a distancia e o tempo
print("Esse é o calculador de velocidade média")
distancia = input ("Digite a distancia percorrida:")
tempo = input ("Digite o tempo percorrido:")
#realizando o calculo e exibindo a mensagem
velocidade_media = float(distancia) / float(tempo)
print("A velocidade média calcula foi:de {:.2f} km/h ".format(velocidade_media))