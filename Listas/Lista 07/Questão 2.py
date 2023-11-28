#=======================================================================
# QUESTÃO 2

import os
os.system("cls")

endereco = open("questao2.txt","r")

for i in endereco:
    
  ip = i.replace("\n",'').split(".")
    
  if int(ip[0]) > 255 or int(ip[1]) > 255 or int(ip[2]) > 255 or int(ip[3]) > 255: 
    #percorre a lista e verifica se o valor é maior que 255
      
      print("IP inválido: ", ip)

  else:
        
        print("IP válido: ", ip)
    
endereco.close()