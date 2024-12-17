class Aluno:

    def __init__(self,nome='',idade=0,turma='',curso='',grade='',alt_dd='',a=0,b=''):
         self.nome = nome
         self.idade = idade
         self.turma = turma
         self.curso = curso
         self.grade = grade
         self.alt_dd = alt_dd
         self.a = a
         self.b = b

    def exibir_dd(self):
         print(f'''Dados do Aluno
               
Nome: {self.nome}
Idade: {self.idade}
Turma: {self.turma}
Curso: {self.curso}
Grade: {self.grade}
Matrícula: ''')

    def alterar_dd(self):
        self.a = int(input('''Qual dado você deseja mudar:
                           
[1]Nome
[2]Idade
[3]Curso
[4]Grade
[5]Matrícula
                           
Reposta: '''))
        self.b = input('Qual será o novo dado: ')
        if self.a == 1:
             self.nome = self.b 
        elif self.a == 2: 
             self.idade = self.b 
        elif self.a == 3: 
             self.curso = self.b 
        elif self.a == 4:
             self.grade = self.b 
        elif self.a == 5:
             pass
        
       
            
         

    def add_dd(self):
         
         self.nome = input('''\nNome: ''')
         self.idade = int(input('''\nIdade: '''))
         self.turma = input('\nTurma: ')
         self.curso = input('\nCurso: ')
         self.grade = input('\nGrade: ')