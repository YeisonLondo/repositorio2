def programa(lista):
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
                intercambio = True
        if not intercambio:
            break
            


lista=[8,4,5,2,8,3,10]
programa(lista)
print(lista)
        