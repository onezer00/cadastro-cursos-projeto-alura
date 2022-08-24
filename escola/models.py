"""
Criação de modelos para o aplicativo escola
"""
from django.db import models


class Aluno(models.Model):
    """
    Criação de modelos para o Aluno
    """
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return str(self.nome)


class Curso(models.Model):
    """
    Criação de modelos para o Curso
    """
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(
        max_length=1, choices=NIVEL, blank=False, null=False, default='B'
    )

    def __str__(self):
        return str(self.descricao)


class Matricula(models.Model):
    """
    Criação de modelos para a Matricula
    """
    PERIODO = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(
        max_length=1, choices=PERIODO, blank=False, null=False, default='M'
    )
