def balanco(): # Função principal

    while True: # Loop infinito

        try: # Tenta executar o código

            expressao = input().strip() # Recebe a expressão e remove os espaços em branco
    
            correct = True # Variável que indica se a expressão está correta ou não

            parenteses = 0 # Variável que conta o número de parenteses abertos

            for letra in expressao: # Percorre a expressão

                if(letra == '('): # Se a letra for um parenteses aberto

                    parenteses += 1 # Incrementa o número de parenteses abertos

                elif(letra == ')'): # Se a letra for um parenteses fechado

                    if(parenteses > 0): # Se houver parenteses abertos

                        parenteses -= 1 # Decrementa o número de parenteses abertos

                    else: # Se não houver parenteses abertos 

                        correct = False # A expressão está incorreta

                        break # Sai do loop
            
            correct = correct and (parenteses == 0) # A expressão está correta se não houver parenteses abertos e se a variável correct for True
            
            print("correct" if correct else "incorrect") # Imprime correct se a expressão estiver correta, caso contrário imprime incorrect
            
        except EOFError: # Se o usuário pressionar Ctrl+D

            break # Sai do loop

balanco()