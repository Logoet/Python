lista = []
for i in range(0,5):
    num = int(input("Digite um valor:")) #9
    if not lista: 
        lista.append(num)
        print(f'O número {num} foi adicionado na posição de número 0.')
    elif num <= lista[0]:
        lista.insert(0,num)
        print(f'O número {num} foi adicionado na posição de número 0.')
    elif num >= lista[-1]:
        lista.append(num)
        print(f'O número {num} foi adicionado na posição de número {len(lista)}.')
    else:
        for j in enumerate(lista):
            
            print(f'O valor de j={j}')
            if num > lista[-j]:
                lista.insert(j+1,num)
                print(f'O número {num} foi adicionado na posição de número {j}.')
                break
print(f'A lista digitada foi:{lista}')
