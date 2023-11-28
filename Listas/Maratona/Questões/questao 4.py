num = int(input("Digite um número de funcionários: "))

conta_total = float(input("Digite o número da conta total: "))
nomes = []
contribuicoes = []

valores = 0
cont = 0
maior_i = 0

for i in range(num):
    nome = input("Digite o nome do funcionário: ")
    nomes.append(nome)

    contribuicao = float(input("Digite a contribuição do funcionário: "))
    contribuicoes.append(contribuicao)
    valores += contribuicao
    cont = cont + 1

excedente = valores - conta_total


for i in range(len(contribuicoes)):
    max = []

    
    # if i == contribuicoes[i] > contribuicoes[i-1]:
    #     maior_i=i
    #     print(f"O funcionário que mais contribuiu foi: {nomes[i]} com o valor de: {maior_i}")
    print(contribuicoes[i])




print(f"O valor total arrecadado foi: {valores}")
print("A media de contribuição foi: ", valores / cont)

#erro no print da contribuição