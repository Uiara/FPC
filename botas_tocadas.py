while True:
    try:
        N = int(input())
        lista_direito = []
        lista_esquerdo = []
        numero_par = 0
        while N % 2 != 0:
            if 2 >= N or N <= 10**4:
                N = int(input()) 

        for x in range(N):
            entrada  = input().split(" ")
            M , L = entrada[0],entrada[1]
            if L == "D":
                lista_direito.append(M)
            elif L == "E":
                lista_esquerdo.append(M)
        for x in lista_direito:
            if x in lista_esquerdo:
                numero_par += 1
                lista_esquerdo.remove(x)

        print(numero_par)
    except EOFError:
        break

