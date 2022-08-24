"""
Responsável por administrar o site escola
"""
from django.contrib import admin

from .models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    """
    Classe responsável por administrar alunos
    """

    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    """
    Classe responsável por administrar cursos
    """

    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)
    list_per_page = 20


admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    """
    Classe responsável por administrar matriculas
    """

    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)


admin.site.register(Matricula, Matriculas)
