# EX 5
# salario atual:
# porcentagem do reajuste:
# aumento em reais:
# salario final após reajuste

#   Salário Abaixo de R$1.500,00 = Aumento de 25%   V
#   Salário Entre de R$1.500,00 e R$1.999,99 = Aumento de 20%   V
#   Salário Entre de R$2.000,00 e R$2.999,99 = Aumento de 15%   V
#   Salário Entre de R$3.000,00 e R$4.999,99 = Aumento de 10%   V
#   Salário Acima de R$5.000,00 = Aumento de 5% A

print('Quer descobrir qual o valor do seu salário após o mais recente reajuste?','\n',
      'Você está no lugar certo!','\n')

sal_atual = float(input('Digite aqui o seu salário atual: '))

if sal_atual<1500.00:
    aumento = 25/100
elif sal_atual>=1500.00 and sal_atual<=1999.99:
    aumento = 20/100
elif sal_atual>=2000.00 and sal_atual<=2999.99:
    aumento = 15/100
elif sal_atual>=3000.00 and sal_atual<=4999.99:
    aumento = 10/100
elif sal_atual>=5000:
    aumento = 5/100

aumento_reais = sal_atual*aumento
sal_final = sal_atual + aumento_reais

print('Salário atual: R$', sal_atual,'\n',
      'Porcentagem do reajuste: ', aumento,'%','\n',
      'Aumento em reais: R$', aumento_reais,'\n',
      'Salário final (após reajuste): ', sal_final,'\n')
