assinatura = str(input("Digite a LETRA INICIAL do seu plano : P-Platinum, G-Gold, S-Silver ou B-Basic: "))
faturamentoAnual = float(input("Qual seu faturamento anual? "))

# if bonus.upper()
if assinatura.upper() == "P":
    #cáculo de 5%
    bonus = float(faturamentoAnual) * (5/100)
elif assinatura.upper() == "G":
    #cáculo de 10%
    bonus = float(faturamentoAnual) * (10/100)
elif assinatura.upper() == "S":
    #cáculo de 20%
    bonus = float(faturamentoAnual) * (20/100)
elif assinatura.upper() == "B":
    bonus = float(faturamentoAnual) * (30/100)

else:
    bonus = float(faturamentoAnual)
print("O valor do bônus é: {:.2f}".format(bonus))