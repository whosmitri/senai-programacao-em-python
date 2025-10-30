# EX 6 - CAIXA ELETRÔNICO

#   R$ 200,00
#   R$ 100,00
#   R$ 50,00
#   R$ 20,00
#   R$ 10,00
#   R$ 5,00
#   R$ 2,00

# valor total da compra:
# menor quantidade de cédulas

print('='*35)
print('Bem-vindo à sua caixa eletrônica ')
print('='*35)
print('Aviso 1: nosso programa ainda está em fase beta, então podem haver limitações.','\n',
      'Aviso 2: Se atente a não sacar notas menores que dois ou iguais a três!.')

valor_sacar = int(input('Digite aqui o valor a ser sacado: '))

if valor_sacar < 2 or valor_sacar == 3:
    print('Valor Inválido! Leia o "Aviso 2"!!')

else:
    duzentos = int(valor_sacar/200)
    valor_sacar = valor_sacar - (duzentos*200)

    cem = int(valor_sacar/100)
    valor_sacar = valor_sacar - (cem*100)

    cinquenta = int(valor_sacar/50)
    valor_sacar = valor_sacar - (cinquenta*50)

    vinte = int(valor_sacar/20)
    valor_sacar = valor_sacar - (vinte*20)

    dez = int(valor_sacar/10)
    valor_sacar = valor_sacar - (dez*10)

    cinco = int(valor_sacar/5)
    valor_sacar = valor_sacar - (cinco*5)

    dois = int(valor_sacar/2)
    valor_sacar = valor_sacar - (dois*2)

    resto = valor_sacar

    print('Notas R$200: ', duzentos)
    print('Notas R$100: ', cem)
    print('Notas R$50: ', cinquenta)
    print('Notas R$20: ', vinte)
    print('Notas R$10: ', dez)
    print('Notas R$5: ', cinco)
    print('Notas R$2: ', dois)

    if valor_sacar == 0:
        print('Obrigado por usar nossos serviços!','\n',
              'Saque no valor de --> R$',valor_sacar)
    elif valor_sacar>=1:
        print('Operação cancelada!','\n',
              'As cédulas nesta caixa não permitem continuar com a transação.','\n',
              'Por favor, escolha outro valor!')
