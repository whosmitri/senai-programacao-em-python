# 17-01-2024
# EX. 1

print('Quer descobrir se um número é impar ou par? Eu faço isso para você!')
print('Digite o número inteiro de sua preferência no campo abaixo.')
print('')

num = float(input('Digite aqui: '))

if num.is_integer():
    if num % 2 == 0:
        print('Esse número é par!')
    else:
        print('Esse número não é par.')
else:
    print('O número não é inteiro, portanto não posso classificá-lo como par ou impar, sinto muito!')
