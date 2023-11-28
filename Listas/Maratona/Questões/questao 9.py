senha = input("Digite a senha: ")

cont = 0

for i in senha:
    if type(i) == int:
        cont+=1
    if i == "*" or "$" or "%" or"|" or "&":
        cont+=1
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        cont+=1
    if i in "abcdefghijklmnopqrstuvwxyz":
        cont+=1

if cont >= 4:
    print("Senha válida")
else:
    print("Senha inválida")