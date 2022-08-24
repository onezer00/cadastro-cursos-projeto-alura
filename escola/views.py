"""
Módulo responsável pelas views do aplicativo escola
"""
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from escola.models import Aluno, Curso, Matricula
from escola.serializer import (AlunosSerializer, CursoSerializer,
                               ListaAlunosMatriculadosSerializer,
                               ListaMatriculaAlunoSerializer,
                               MatriculaSerializer)


class AlunosViewSet(viewsets.ModelViewSet):
    """
    Classe responsável por exibir todos os alunos e alunas
    """

    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class CursosViewSet(viewsets.ModelViewSet):
    """
    Classe responsável por exibir todos os cursos e curso
    """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class MatriculasViewSet(viewsets.ModelViewSet):
    """
    Classe responsável por exibir todas as matrículas
    """

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class ListaMatriculasAluno(generics.ListAPIView):
    """
    Classe responsável por exibir todas as matrículas de um aluno
    """

    def get_queryset(self):
        """
        Método responsável pela queryset da lista de matrículas de um aluno
        """
        queryset = Matricula.objects.filter(aluno=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class ListaAlunosMatriculados(generics.ListAPIView):
    """
    Classe reponsável por listar alunos matriculados em curso
    """

    def get_queryset(self):
        """
        Método responsável pela queryset da lista de alunos matriculados em curso
        """
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
