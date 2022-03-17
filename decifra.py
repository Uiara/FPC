vocabulario_atual = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decifra (novo_vocabulario, cifra):
    '''Função para decifrar, baseado na entrada de uma cifra'''
    lista = []
    soma = 0
    lista_nova = []
    for x in cifra:
        for y in novo_vocabulario:
            soma += 1
            if x == y:
                lista.append(soma-1)
                soma = 0
                break
                
    for x in lista:
        lista_nova.append(vocabulario_atual[x])

    resultado = "".join(lista_nova)
    print(resultado)

novo_vocabulario = input()
cifra = input()

decifra(novo_vocabulario,cifra)