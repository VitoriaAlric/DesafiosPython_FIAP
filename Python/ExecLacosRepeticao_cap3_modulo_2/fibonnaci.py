#Inicializando váriaveis
n1, n2 = 1, 1
soma = 2
numUsuario = int(input('Digite um valor número inteiro: '))
#looping para o cálculo do Fibannoci
while soma < numUsuario:
       n1 = n2
       n2 = soma
       soma = n1 + n2
#excessões
if numUsuario <= 0:
    print("Entre com um numero inteiro")
elif numUsuario == 1:
    print("O número que você digitou encontra-se na sequência Fibonnaci. Ação bem sucedida!")
elif numUsuario == 2:
    print("O número que você digitou encontra-se na sequência Fibonnaci. Ação bem sucedida!")
elif soma == numUsuario :
    print("O número que você digitou encontra-se na sequência Fibonnaci. Ação bem sucedida!")
elif soma > numUsuario :
    print("O número que você digitou não faz parte da encontra-se na sequência Fibonnaci. A ação falhou...")

