# Como  forma  de  validar  um  protótipo,  foi  solicitado  que  você  crie  um  script simples,
# em  que  o  usuário  deve  informar  QUANTAS  TRANSAÇÕES financeiras realizou ao longo de um dia e,
# na sequência, deve informar o VALOR DE CADA UMA das transações que realizou

valorTransacoes: int = 0
qtdTransacoes = int(input("Informa a quantidade de transações que você realizou ao londgo do dia: "))

for i in range(1, qtdTransacoes + 1):
    transacoes: int = int(input(("Informe o valor da transação {} : ".format(i))))
    valorTransacoes += transacoes

print("Total de transações: {}".format(qtdTransacoes))
print("Valor total das transações: {}".format(valorTransacoes))

#deixar float ajusar dps
