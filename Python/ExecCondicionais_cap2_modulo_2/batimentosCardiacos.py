bpm = int(input("Informe o seu número de batimentos por minuto (BPM): "))
idade = int(input("Informe sua idade: "))

#Até 2 anos
if 120 <= bpm <= 140 and idade <= 2:
    print("O seu BPM está DENTRO da faixa adequada.")
elif bpm < 120 and idade <= 2:
    print("O seu BPM está ABAIXO da faixa adequada.")
elif bpm > 140 and idade <= 2:
    print("O seu BPM está ACIMA da faixa adequada.")

#De 8 anos até 17 anos
elif 80 <= bpm <= 100 and idade <= 8:
    print("O seu BPM está DENTRO da faixa adequada.")
elif 80 <= bpm <= 100 and idade <= 17:
    print("O seu BPM está DENTRO da faixa adequada.")
elif bpm < 80 and idade <= 8:
    print("O seu BPM está ABAIXO da faixa adequada.")
elif bpm < 80 and idade <= 17:
    print("O seu BPM está ABAIXO da faixa adequada.")
elif bpm > 100 and idade <= 8:
    print("O seu BPM está ACIMA da faixa adequada.")
elif bpm > 100 and idade <= 17:
    print("O seu BPM está ACIMA da faixa adequada.")

#Aulto Sedentario (18 a 65)
elif 70 <= bpm <= 80 and idade <= 18:
    print("O seu BPM está DENTRO da faixa adequada.")
elif 70 <= bpm <= 80 and idade <= 65:
    print("O seu BPM está DENTRO da faixa adequada.")
elif bpm < 70 and idade <= 18:
    print("O seu BPM está ABAIXO da faixa adequada.")
elif bpm < 80 and idade <= 65:
    print("O seu BPM está ABAIXO da faixa adequada.")
elif bpm > 70 and idade <= 18:
    print("O seu BPM está ACIMA da faixa adequada.")
elif bpm > 80 and idade <= 65:
    print("O seu BPM está ACIMA da faixa adequada.")

#Idosos (maior que 65 anos)
if 50 <= bpm <= 60 and idade > 65:
    print("O seu BPM está DENTRO da faixa adequada.")
elif bpm < 50 and idade > 65:
    print("O seu BPM está ABAIXO da faixa adequada.")
elif bpm > 60 and idade > 65:
    print("O seu BPM está ACIMA da faixa adequada.")