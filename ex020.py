from random import shuffle

aluno1 = input('1 - ')
aluno2 = input('2 - ')
aluno3 = input('3 - ')
aluno4 = input('4 - ')

listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(listaDeAlunos)

print(f'A ordem de apresentação será:\n1 - {listaDeAlunos[0]}\n2 - {listaDeAlunos[1]}\n3 - {listaDeAlunos[2]}\n4 - {listaDeAlunos[3]}')
