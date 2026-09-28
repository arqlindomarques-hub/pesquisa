import os
os.system ("cls" if os.name =="nt" else "clear")
#limpa o sistema
opiniao_1=0
opiniao_2=0
opiniao_3=0
#zera o contador de cada opiniao
for i in range (9):#range (49) contagem até 50 pessoas, no caso 10 pessoas, no teste 4.
    nome = input("digite seu nome:")#número de sequencia e entrada  de nome
    print(i + 1, "Seu nome é: ", nome)
    idade = input ("digite sua idade:")#entrada de idade
    print("Sua idade é: ", idade, "anos")
    opiniao = int(input("digite sua opinião sobre o atendimento: 1 = Excelente, 2 = Bom e 3 = Ruim: "))
    if opiniao == 1:
      opiniao_1 = opiniao_1 + 1#soma o número de vezes da ocorrencia da opinião 1
    elif opiniao == 2:
        opiniao_2 = opiniao_2 + 1
    elif opiniao == 3:
        opiniao_3 = opiniao_3 + 1
    else:
        print("Opinião inválida, digite novamente") #a ser ativado quando aprender comando de retorno
    #acaba looping de dados
print("Contagem de votos: Exelente = ", opiniao_1, ", Bom = ", opiniao_2, " e Ruim = ", opiniao_3)