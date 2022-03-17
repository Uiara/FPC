lista_esquerdo = []
lista_direito = []
def numero_botas(M,L):
    '''Forma uma lista com o número do pé esquerdo ou direito'''
    lista_direito = []
    lista_esquerdo = []
    if L == "D":
        lista_direito.append(M)
    elif L == "E":
        lista_esquerdo.append(M)
    return(lista_direito,lista_esquerdo)

for x in lista_direito:
    if x in lista_esquerdo:
        numero_par += 1
        lista_esquerdo.remove(x)




