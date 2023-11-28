vetorA = []
vetorB = []

for i in range(5):
    vetorA.append(int(input("Digite um número: ")))

for i in range(len(vetorA)):
    vetorB.append(vetorA[i] ** 2)

print(vetorA)
print(vetorB)