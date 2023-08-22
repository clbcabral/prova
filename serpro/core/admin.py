from django.contrib import admin
from core import models


# Register your models here.
admin.site.register(models.Pessoa)
admin.site.register(models.Professor)
admin.site.register(models.Disciplina)
admin.site.register(models.Ministrante)
admin.site.register(models.Curso)
admin.site.register(models.Aluno)
admin.site.register(models.Turma)
admin.site.register(models.Matricula)
admin.site.register(models.Grade)
