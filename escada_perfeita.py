lista=[5,4,5,4,2]
n = sum(lista)
print(n)
x = (((n*2)/5)+(5-1))/2
print(x)
a = 1+x-5
print(a)
'''
n = 0
soma = 0
a, b = 0, 0
pilha = []
moves=0
movimentos=0

n = int(input())
pilha=[int(x) for x in input().split(" ")]
for i in range(0, n, 1):
  soma+=pilha[i]



b = (((2*soma)/n)+(n-1))/2
a = 1+b-n


if (soma - ((n * n + n) / 2)) >= 0 and soma % n == 0:

    for i in range(0, n, 1):
        moves +=(pilha[i]-(i+a))
        if pilha[i] > i+a:
            movimentos += (pilha[i]-(i+a))
    print(movimentos)
else:
    print("-1")
'''