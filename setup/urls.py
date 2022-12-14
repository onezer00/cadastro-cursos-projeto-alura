"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from escola.views import (AlunosViewSet, CursosViewSet,
                          ListaAlunosMatriculados, ListaMatriculasAluno,
                          MatriculasViewSet)

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='alunos')
router.register('cursos', CursosViewSet, basename='cursos')
router.register('matriculas', MatriculasViewSet, basename='matriculas')

urlpatterns = [
    path('api_schema/', get_schema_view(
        title='DJANGO REST API - API Documentation',
        description = \
        """
        Esta API foi desenvolvida para o curso de Orientação a Objetos da Alura.
        Foram implementadas as seguintes funcionalidades:
        """
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('aluno/<int:pk>/matriculas', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas', ListaAlunosMatriculados.as_view()),
]
