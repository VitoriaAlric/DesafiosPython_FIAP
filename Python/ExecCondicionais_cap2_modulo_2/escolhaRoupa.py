# A loja virtual “FIAP Wear”, que vende roupas personalizadas da instituição, disponibilizou
# no  mês  do  seu  aniversário  o  cupom  NIVER10  que  concede  10%  de desconto no valor total
# de uma compra feita no site.Caso o cliente digite o cupom corretamente, deverá ser informado do
# valor final da compra já com o desconto aplicado. Caso digite qualquer cupom incorreto, deverá
# ser informado do valor da compra sem o desconto.Esse  problema  claramente  pedeo  uso  de  um
# if  composto!  Afinal  de  contas temos uma única condição (o cupom digitado ser igual a “NIVER10”)
# e duas ações, sendo uma para cada resultado da condição.

#solicitando os dados do cliente
valor_compra = input("Informe o valor da compra realizada ")
cupom = input("Digite o cupom de desconto ")
#realizando o teste lógico com o cupom em maiúsculas
if cupom.upper() == "NIVER10":
    #cálculo de 10% de desconto
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
#exibindo o valor final da compra
print("O valor final da compra é {}".format(valor_final))