entrada = input().split()
n,m,s = entrada
while n != '0' and m != '0' and s != '0':
    matriz = []
    listaInicial = []
    figurinhaCopa = 0
    listaFigurinha = []
    for x in range(int(n)):
        entradaMatriz = input()
        matriz.append(list(entradaMatriz))
    instrucoesRobo = list(input())
    
    linha = -1
    linhaAtual = 0
    coluna = 0
    for y in matriz: #para encontrar o elemento
        linha += 1
        if linhaAtual < linha:
            linhaAtual = linha
            coluna = -1
        for w in y:
            coluna += 1
            if w == 'N' or w == 'S' or w == 'L' or w == 'O':
                direcaoAnterior = w
                break
        if w == 'N' or w == 'S' or w == 'L' or w == 'O':
            break

    #ele gira mas não anda
    def direcao_funcao(direcao,coluna,linha): #direcao que ira andar
        if direcao == 'N':
            coluna += 1
        elif direcao == 'S':
            coluna -= 1
        elif direcao == 'L' or direcao == 'D':
            linha += 1
        elif direcao == 'O' or direcao == 'E':
            linha -= 1       
        return direcaoAnterior, coluna, linha

    direcaoRecebida =''
    for x in (instrucoesRobo):
        direcaoRecebida = ''+x
        if direcaoRecebida != 'F':
            if direcaoAnterior != 'N' or direcaoAnterior != 'S' or direcaoAnterior != 'L' or direcaoAnterior != 'O':
                direcaoAnterior = direcaoRecebida
        elif direcaoRecebida == 'F':
            direcaoAnterior, linha, coluna = (direcao_funcao(direcaoAnterior,linha,coluna))
            caracter = matriz[linha][coluna]
            if caracter == '*':
                figurinhaCopa += 1
                matriz[linha][coluna] = '.'

    listaFigurinha.append(figurinhaCopa)

for x in range(listaFigurinha):
    print(x)

                




