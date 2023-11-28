import os
os.system('cls')

def imposto(num1):

    if num1 <= 2000.00: # se o número for menor ou igual a 2000

        return("Isento") # retorna o resultado
    
    elif num1 >= 2000.01 and num1 <= 3000.00: # 8% de 1000

        num1 = (num1 - 2000)*0.08 # 8% de 1000
        return ("R$ {:.2f}".format(num1)) # retorna o resultado
    
    elif num1 >= 3000.01 and num1 <= 4500.00: # 18% de 1500

        num1 = (num1 - 3000)*0.18 + 1000*0.08 # 18% de 1500 + 8% de 1000
        return ("R$ {:.2f}".format(num1)) # retorna o resultado
    
    else: # 28% de 3500
        
        num1 = (num1 - 4500)*0.28 + 1500*0.18 + 1000*0.08 # 28% de 3500 + 18% de 1500 + 8% de 1000
        return ("R$ {:.2f}".format(num1)) # retorna o resultado
    
salario = (float(input())) # o número que entra na funcão como paramêtro
print(imposto(salario))