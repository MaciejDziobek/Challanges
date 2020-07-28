lista=[10, 4, 9, 7, 1]

print(lista)

t=0
while (t != 5):
    x=0
    for i in (lista):
        if (x==4):
            break
        if (i<lista[x+1]):
            print
        else:
            lista.insert(x, lista[x+1])
            lista.pop(x+2)
        x=x+1
    t=t+1


print(lista)

