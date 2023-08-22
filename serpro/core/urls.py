from django.urls import path
from core import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('listar-alunos/', views.listar_alunos_view, name='listar_alunos_view'),
    path('editar-aluno/<int:pk>', views.EditarAlunoView.as_view(), name='editar_aluno_view'),
    path('criar-aluno/', views.CriarAlunoView.as_view(), name='criar_aluno_view'),
    path('relatorio-alunos-curso/', views.relatorio_alunos_curso_view, name='relatorio_alunos_curso_view'),
]
