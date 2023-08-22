from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=15)

class Professor(Pessoa):
    numero_funcionario = models.CharField(max_length=9)
    data_contratacao = models.DateField()
    dedicacao_exclusiva = models.BooleanField()

class Disciplina(models.Model):
    nome = models.CharField(max_length=120)
    ementa = models.TextField()
    carga_horaria = models.DecimalField(decimal_places=2, max_digits=6)
    porcentagem_teoria = models.DecimalField(decimal_places=2, max_digits=5)
    porcentagem_pratica = models.DecimalField(decimal_places=2, max_digits=5)
    ativo = models.BooleanField()

class Ministrante(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)

class Curso(models.Model):
    class Categoria(models.TextChoices):
        APERFEICOAMENTO = 'AP', 'Aperfeiçoamento'
        CAPACITACAO = 'CP', 'Capacitação'
        OFICINA = 'OF', 'Oficina'
        TREINAMENTO = 'TR', 'Treinamento'
    nome = models.CharField(max_length=150)
    categoria = models.CharField(choices=Categoria.choices, max_length=2)
    data_criacao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField()
    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    numero_matricula = models.CharField(max_length=9)
    data_matricula = models.DateField()
    aluno_especial = models.BooleanField(default=False)

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    horario = models.CharField(max_length=50)
    local = models.CharField(max_length=100)
    ativo = models.BooleanField()

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)

class Grade(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    ministrante = models.ForeignKey(Ministrante, on_delete=models.PROTECT)