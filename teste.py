lista_Final = []
Matriz = []
contador = 0
def criar_Matriz (linha,coluna):

    global Matriz
    for i in range(linha):
        l_linha = []
        coord = input()
        for j in range(coluna):
            l_linha.append(coord[j])
        Matriz.append(l_linha)
        
def qntd_Navios(i,j):
    #programação dinamica
    global Matriz
    global contador
    global l
    global c
    global lista_Final
    if Matriz[i][j] == "#":
        if i-1>=0:
            Matriz[i][j] = contador
            qntd_Navios(i-1,j)
        if j + 1 < c:
            Matriz[i][j] = contador
            qntd_Navios(i,j+1)
        if i+1 < l:
            Matriz[i][j] = contador
            qntd_Navios(i+1,j)
        if j-1>=0:
            Matriz[i][j] = contador
            qntd_Navios(i,j-1)
        lista_Final[contador] += 1
    else:
        return

l,c = [int(i) for i in input().split()]
criar_Matriz(l,c)
for i in range(l):
    for j in range(c):
        if Matriz[i][j] == "#":
            lista_Final.append(0)
            qntd_Navios(i,j)
            contador+=1

qntd_disparos = int(input())
for i in range(qntd_disparos):
    disparo = [int(i) for i in input().split()]
    if type(Matriz[disparo[0]-1][disparo[1]-1]) == int:
        lista_Final[Matriz[disparo[0]-1][disparo[1]-1]] -= 1
navios = 0
for i in lista_Final:
    if i == 0:
        navios+=1
print(navios)
