lista = [[],[]]
for i in range(0,7):
    num = int(input(f"Digite o {i}º número:"))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(lista)
