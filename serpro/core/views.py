from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django import forms
from core.models import Aluno, Curso

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def listar_alunos_view(request):
    alunos = Aluno.objects.filter()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

class CriarAlunoView(CreateView):
    model = Aluno
    template_name = 'criar_aluno.html'
    fields = ('nome', 'cpf', 'data_nascimento', 
              'endereco', 'telefone', 'numero_matricula',
              'data_matricula', 'aluno_especial')
    success_url = reverse_lazy('criar_aluno_view')
    
class EditarAlunoView(UpdateView):
    model = Aluno
    template_name = 'editar_aluno.html'
    fields = ('nome', 'cpf', 'data_nascimento', 
              'endereco', 'telefone', 'numero_matricula',
              'data_matricula', 'aluno_especial')
    success_url = reverse_lazy('listar_alunos_view')

class RelatorioAlunosCursoForm(forms.Form):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), label='Curso')

def relatorio_alunos_curso_view(request):
    alunos = []
    if request.method == 'POST':
        form = RelatorioAlunosCursoForm(request.POST)
        if form.is_valid():
          curso = form.cleaned_data['curso']
          alunos = Aluno.objects.filter(matricula__turma__curso=curso)
    else:
        form = RelatorioAlunosCursoForm()
    return render(request, 'relatorio_alunos_curso.html', context={
        'form': form,
        'alunos': alunos
    })
