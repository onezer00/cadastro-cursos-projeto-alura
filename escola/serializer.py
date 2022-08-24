"""
Modulo responsável por serializar os objetos
"""
from rest_framework import serializers

from .models import Aluno, Curso, Matricula


class AlunosSerializer(serializers.ModelSerializer):
    """
    Classe responsável pela serialização de alunos
    """
    class Meta:
        """
        Class Meta do AlunoSerializer
        """
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    """
    Classe responsável pela serialização dos cursos
    """
    class Meta:
        """
        Class Meta do CursoSerializer
        """
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    """
    Classe responsável pela serialização das matriculas
    """
    class Meta:
        """
        Class Meta da MatriculaSerializer
        """
        model = Matricula
        exclude = []


class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    """
    Classe responsável pela serialização as matriculas de um aluno
    """
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        """
        Class Meta do ListaMatriculaAlunoSerializer
        """
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        """
        Método responsável por retornar periodo da matricula
        """
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    """
    Classe responsável pela serialização dos alunos matriculados
    """
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        """
        Class Meta da ListaAlunosMatriculadosSerializer
        """
        model = Matricula
        fields = ['aluno_nome']
