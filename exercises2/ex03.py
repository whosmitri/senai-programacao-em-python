# EX. 3
# DUAS NOTAS (prova + trabalho), ENTÃO CALCULAR MÉDIA.
# final>7 = APROVADO / final<5 = REPROVADO / 5>final<7 = RECUPERAÇÃO

print('Bem-vindo(a), professor(a), preencha os campos abaixos com as notas correspondentes para saber a média final do seu aluno.', '\n')

nome = str(input('Digite aqui o nome do(a) aluno(a): '))
nota1 = float(input('Insira aqui a nota de prova do(a) aluno(a): '))
nota2 = float(input('Insira aqui a nota de trabalho do(a) aluno(a): '))

nota_prova = round(nota1)
nota_trabalho = round(nota2)

media = (nota_prova + nota_trabalho)/2

if media>7:
    print('Seu(sua) aluno(a), ',nome,', tirou ', media,' e está aprovado(a)!')
elif media<5:
    print('Seu(sua) aluno(a), ',nome,', tirou ',media,' e está reprovado(a), ele(a) deve estudar mais.')
elif media<=7 and media>=5:
    print('Seu(sua) aluno(a)' ,nome,', tirou ',media,' e está de recuperação, ainda não acabou!')
