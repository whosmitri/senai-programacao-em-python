# 17-01-2024
# EX. 2

print('Bem-vindo(a) à "Gratuidade na TransViagem!')
print('Informe sua idade e te informaremos se você tem gratuidade no transporte público.', '\n')

idade = int(input('Digite a sua idade aqui: '))

if idade>=65:
    print('Parabéns! Você tem passagem gratuita em qualquer transporte da nossa empresa (TransViagem)!')
elif idade<65 and idade>0:
    print('Parece que você ainda não tem acesso ao serviço de gratuidade, sinto muito.')
elif idade<=0:
      print('Esta não é sua verdadeira idade!')
