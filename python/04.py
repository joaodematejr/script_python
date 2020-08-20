print('Digite um valor para troco')
valor = int(input())

print('Digite o preço do produto')
preco = int(input())


#Adição de desconto
desconto = int (input("Digite o valor do desconto: "))
precototal = preco - desconto
print ("O preço com desconto é R$", preco)

calcular = valor - precototal

print("O valor do troco será de R$", calcular)
