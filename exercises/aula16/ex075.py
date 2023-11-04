
# num1 = int(input('Digite um número:'))
# num2 = int(input('Digite um número:'))
# num3 = int(input('Digite um número:'))
# num4 = int(input('Digite um número:'))

# arrayNumber = (num1,num2,num3,num4)



arrayNumber = (2,3,4,9)
print(f'(A) O número 9 apareceu {arrayNumber.count(9)} vezes!')

if 3 in arrayNumber:
    print(f'(B)A primeira posição que aparece o valor "3" é na posição: {arrayNumber.index(3)+1}!')
else:
    print('(B)O valor 3 não foi digitado!')

print("Os valores pares foram:")
for i in range(1,len(arrayNumber)):
    if arrayNumber[i-1] % 2 == 0:
        print(arrayNumber[i-1])
# print(f'(B) O valor 3')  