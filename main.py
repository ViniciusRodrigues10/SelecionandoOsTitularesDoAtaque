def calcularIndice(notas):
    return notas[0] * 2 + notas[1] * 3.5 + notas[2] * 1.5 + notas[3] * 2


indices = []
for i in range(5):
    nomeJogadores = str(input())

    notas = []
    for j in range(4):
        notasJogadores = int(input())
        notas.append(notasJogadores)
    indices.append(calcularIndice(notas))

indices.sort(reverse=True)

for i in range(3):
    print(indices[i])
