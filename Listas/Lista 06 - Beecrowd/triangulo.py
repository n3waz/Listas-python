import os 
os.system('cls')

def triangulo(a, b, c):

    if (a >= (b + c)):
        print("NAO FORMA TRIANGULO")
    else:

        if (a*a < (b*b + c*c)): #se a² < b² + c²
            print("TRIANGULO ACUTANGULO") #acutangulo 

        elif (a*a == (b*b + c*c)): #se a² = b² + c²
            print("TRIANGULO RETANGULO") #retangulo

        elif (a*a > (b*b + c*c)): #se a² > b² + c²
            print("TRIANGULO OBTUSANGULO") #obtusangulo
             
def lados(a, b, c): 
    if (a==b==c): #se a=b=c
        print("TRIANGULO EQUILATERO") #equilatero
    
    elif (a==b or a==c or b==c): #se a=b ou a=c ou b=c
        print("TRIANGULO ISOSCELES") #isosceles
    
lista = input().split()

for i in range(len(lista)):
    lista[i] = float(lista[i])

lista.sort(reverse=True)

triangulo(lista[0], lista[1], lista[2])
lados(lista[0], lista[1], lista[2])