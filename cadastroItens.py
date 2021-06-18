print("---------------------")
print("/  Mercado do Cauê  /")
print("---------------------")

quantidadeItens = int(input("Insira a quantidade de itens: "))
nomeOperador = input("Insira o nome do operador de caixa: ")

print("Bem vindo "+nomeOperador)

i = 0
itens = []
while i < quantidadeItens:
    itens.append(input("insira um item: "))
    i+=1

print("--------------")
print("Itens que foram adicionados: ")
print("--------------")

for item in itens:
    print(item)