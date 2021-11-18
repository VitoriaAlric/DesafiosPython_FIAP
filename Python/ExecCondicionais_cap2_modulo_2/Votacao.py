seg = int(input("Quantidade de votos para a Live na SEG: "))
ter = int(input("Quantidade de votos para a Live na TER: "))
qua = int(input("Quantidade de votos para a Live na QUA: "))
qui = int(input("Quantidade de votos para a Live na QUI: "))
sex = int(input("Quantidade de votos para a Live na SEX: "))


if seg > ter and seg > qua and seg > qui and seg > sex:
    print("Segunda-feira recebeu mais votos, será o dia da LIVE o/")

elif ter > seg and ter > qua and ter > qui and ter > sex:
    print("Terça-feira recebeu mais votos, será o dia da LIVE o/")

elif qua > seg and qua > ter and qua > qui and qua > sex:
    print("Quarta-feira recebeu mais votos, será o dia da LIVE o/")

elif qui > seg and qui > ter and qui > qua and qui > sex:
    print("Quinta-feira recebeu mais votos, será o dia da LIVE o/")

elif sex > seg and sex > ter and sex > qua and sex > qui:
    print("Sexta-feira recebeu mais votos, será o dia da LIVE o/")

else:
    print("Empate galera, o professor irá desempatar hahaha")