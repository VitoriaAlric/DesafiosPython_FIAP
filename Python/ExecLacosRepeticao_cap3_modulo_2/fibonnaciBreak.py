#O  usuário  deve  digitar um  valor  numérico  inteiro  e  o algoritmo deverá verificar se esse valor encontra-se na sequência de Fibonnaci.
# Caso o  número  esteja  na  sequência,  o  algoritmo  deve  exibir  a  mensagem  “Ação  bem sucedida!” e, caso não esteja,
# deve exibir a mensagem “A ação falhou...”.A  sequência  de  Fibonacci  é  muito  simples  e  possui  uma  lógica  de  fácil
# compreensão: ela se inicia em 1 e cada novo elemento da sequência é a soma entre os dois elementos anteriores.
# Portanto: 1, 1, 2, 3, 5, 8, 13, 21, e assim por diante.Logo, se o usuário digitar o número 55 o programa deveráinformar que a
# ação foi bem sucedida, afinal 55 está entre os números da sequência.Mas  se  o  usuário  digitar  o  número  6,  por  exemplo,
# a  ação  não  será  bem sucedida, pois o número 6 não está na sequência

#entrada
numUsuario = int(input('Digite um número: '))

#definicao das variaveis
anterior = 1
proximo = 1
soma = 2

#condicao loop
while True:

    anterior = proximo
    proximo = soma
    soma = anterior + proximo

    if numUsuario == 1:
        print("Ação bem sucedida!")
        break
    elif numUsuario == 2:
        print("Ação bem sucedida!")
        break
    elif soma == numUsuario:
        print("Ação bem sucedida!")
        break
    elif soma > numUsuario:
        print("A ação falhou...")
        break

