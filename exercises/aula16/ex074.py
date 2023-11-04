from random import randint

num1 = randint(0,100)
num2 = randint(0,100)
num3 = randint(0,100)
num4 = randint(0,100)
num5 = randint(0,100)

menor = num1
maior = num1

arrayNum = (num1,num2,num3,num4,num5)

for i in range(1, len(arrayNum)):
    if menor > arrayNum[i]:
        menor = arrayNum[i]
    elif maior < arrayNum[i]:
        maior = arrayNum[i]

print(f"O computador gerou 5 números aleatórios, eles são: \n {arrayNum}")
print(f'O maior valor gerado foi {maior} e o menor foi {menor}!')
