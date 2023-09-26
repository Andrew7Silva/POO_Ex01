from alunoDeGraduacao import alunoDeGraduacao, alunoDePosGraduacao

grad_aluno = alunoDeGraduacao(nome= '', matricula= '')
grad_aluno.setNome('Andrew')
grad_aluno.setMatricula('1234')
print(grad_aluno)

gradPosAluno = alunoDePosGraduacao(nome='' , matricula='', orientador='')
gradPosAluno.setNome('Andrew Jr')
gradPosAluno.setMatricula('12345')
gradPosAluno.setOrientador('Fábio Bezerra')
print(gradPosAluno)

test = alunoDeGraduacao(nome='', matricula='')
test.setNome('Teste da Silva')
test.setMatricula('testando 123...')
print(test)