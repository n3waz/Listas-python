valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite a quantidade de anos: "))

prestacao = valor_casa / (anos * 12)

if prestacao > (salario * 0.3):
    print("Empréstimo não aprovado")
else:
    print(f"Valor da prestação: {prestacao}")