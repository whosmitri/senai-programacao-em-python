# 3
# valor oculos = R$200,00
# desconto = idade do user
# desconto>10% e desconto<80%
# qual sua idade? ----> valor final: xx e desconto de: yy%

print('Seja bem-vindo ao Desconto Glasses! Nossa página oficial para conferir o seu desconto (baseado na sua idade).', '\n')

idade = int(input('Digite aqui a sua idade: '))

if idade<=10:
    valor_desconto = 10/100
elif idade>=80:
    valor_desconto = 80/100
else:
    valor_desconto = idade/100

valor_final = 200.00-(200.00*valor_desconto)

print('Você terá que pagar: R$', valor_final)
print('Seu desconto foi de: ', valor_desconto,'%')
