while True:
    solucao = int(input("Digite o PH da solução: "))
    
    if solucao < 7 and solucao != -1:
        print("Ácida")
    elif solucao > 7:
        print("Básica")
    elif solucao == 7:
        print("Neutra")

    elif solucao == -1:
        break