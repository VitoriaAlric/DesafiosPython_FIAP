valorBruto=float(input("Digite o Valor Bruto do Pacote: "))
categoria=str(input("Digite as duas LETRA inicias da categoria que você pertence. EX: EC-Economica EX-Executiva PC-Primeira Classe: "))
qtdViajantes=int(input("Digite a quantidade de viajantes: "))
valorLiq = float

#Categoria Economica
if categoria.upper() == "EC" and qtdViajantes == 2:
    desconto = float(valorBruto) * 0.03
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 3% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
elif categoria.upper() == "EC" and qtdViajantes == 3:
    desconto = float(valorBruto) * 0.04
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 4% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
elif categoria.upper() == "EC" and qtdViajantes == 4:
    desconto = float(valorBruto) * 0.05
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 5% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
#Categoria Executiva
elif categoria.upper() == "EX" and qtdViajantes == 2:
    desconto = float(valorBruto) * 0.05
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 5% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
elif categoria.upper() == "EX" and qtdViajantes == 3:
    desconto = float(valorBruto) * 0.07
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 7% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
elif categoria.upper() == "EX" and qtdViajantes == 4:
    desconto = float(valorBruto) * 0.08
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 8% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
#Categoria Primeira Classe
elif categoria.upper() == "PC" and qtdViajantes == 2:
    desconto = float(valorBruto) * 0.10
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 10% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
elif categoria.upper() == "PC" and qtdViajantes == 3:
    desconto = float(valorBruto) * 0.15
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 15% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))
elif categoria.upper() == "PC" and qtdViajantes == 4:
    desconto = float(valorBruto) * 0.20
    valorLiq = valorBruto - desconto
    print("Vocês tem direito a 20% de desconto, o valor atual é {:.2f} e com desconto será de: {:.2f} e o Valor Liquido será de: {:.2f}".format(valorBruto,
                                                                                                             desconto, valorLiq))