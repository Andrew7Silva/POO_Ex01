class alunoDeGraduacao:
    __nome = ''
    __matricula = ''

    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        print('\nCriando aluno de graduação')

    def getNome(self,):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula
    
    def __str__(self):
        return "Nome: " + self.__nome + "\nMatrícula: " + self.__matricula


class alunoDePosGraduacao(alunoDeGraduacao):
    __orientador = ''

    def __init__(self, nome, matricula, orientador):
        super().__init__(nome, matricula)
        self.__orientador = orientador
        print('\nCriando aluno de pós graduação')

    def getOrientador(self):
        return self.__orientador

    def setOrientador(self, orientador):
        self.__orientador = orientador

    def __str__(self):
        return super().__str__() + "\nOrientador: " + self.__orientador