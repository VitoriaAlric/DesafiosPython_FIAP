# Crie um algoritmo onde o usuário possa digitar o voto de cada um dos 5 membros da equipe e,
# ao final, exiba qual foi o console escolhido e com quantos votos.
# As opções são: PLAYSTATION, XBOX e NINTENDO.
votos_Playstation = int(input("Digite o total de votos para Playstation: "))
votos_XBOX = int(input("Digite o total de votos para Xbox: "))
votos_Nintendo = int(input("Digite o total de votos para Nintendo: "))

if votos_Playstation > votos_XBOX and votos_Nintendo:
    print("O Playstation foi o console escolhido com {:.2f} votos".format(votos_Playstation))
elif votos_XBOX > votos_Nintendo and votos_Playstation:
    print("O XBOX foi o console escolhido com {:.2f} votos".format(votos_XBOX))
elif votos_Nintendo > votos_Playstation and votos_XBOX:
    print("O Nintendo foi o console escolhido com {:.2f} votos".format(votos_Nintendo))
else:
    print("Empate!! Será necessário um desempate :)")