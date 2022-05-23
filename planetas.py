m,n = input().split()
listaPlanos = []
listaPosicaoPlanetas = []
listaBinario = [0] * int(n)
matriz = []

#criar lista com a entrada dos planos
for x in range(int(m)):
    entradaPlanos = input().split()
    listaPlanos.append(entradaPlanos)
#criar lista com a posição dos planetas
for y in range(int(n)):
    entradaPosicao = input().split()
    listaPosicaoPlanetas.append(entradaPosicao)
#função que retorna o valor binario
def planetas_binario(listaPlanos, listaPosicaoPlanetas):
    for z in listaPlanos:
        a, b, c, d = z
        posicao = -1
        for w in listaPosicaoPlanetas:
            x,y,z = w
            posicao += 1
            calculo = (int(a)*int(x)) + (int(b)*int(y)) + (int(c)*int(z))
            if int(d) < calculo:
                listaBinario[posicao] = 1
        matriz.append(listaBinario)
    return matriz
matriz = planetas_binario(listaPlanos, listaPosicaoPlanetas)

for x in matriz:
    string = ''.join(map(str, x))

    print(int(string, base=2))