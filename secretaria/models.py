from django.db import models

# Create your models here.
class aluno(models.Model):
    nome= models.CharField('Nome',max_length=100)
    sobrenome=models.CharField('Sobrenome',max_length=100)
    matricula=models.IntegerField('Matricula',)
    
    def __str__(self):
     return f'{self.nome} / {self.sobrenome}'    

class disciplina(models.Model):
     nome= models.CharField('Nome da Disciplina',max_length=100)
     turma= models.CharField('Turma',max_length=100)

     def __str__(self):
      return f'{self.nome} / {self.turma}'
          