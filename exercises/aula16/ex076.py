listaPreco = ('Lápis',1.75,'Borracha',2.00,'Estojo',25.00,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

str = 'LISTAGEM DE PREÇOS'

print("--"*20)
print(str.center(40))
print("--"*20)

for i in range(1,len(listaPreco)+1):
    if i % 2 == 0:
        #Printa Produto
        print(f'{listaPreco[i-1]}')
    else:
        #Printa Preço
        print(f'{listaPreco[i-1]}')

print("--"*20)


itens = [
    {"item": "Lapis", "preco": "R$"},
    {"item": "borracha", "preco": "R$"},
    {"item": "Carro", "preco": "R$"}
]

max_len = max(len(item['preco']) for item in itens)

for item in itens:
    print(f"{item['item']:<15}{item['preco'].ljust(max_len)}")
