"""
Classe responsável por administrar alunos
"""
from django.apps import AppConfig


class EscolaConfig(AppConfig):
    """
    Configuração inicial do aplicativo escola
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'escola'
