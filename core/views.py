from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all() #pegar todas as pessoas que estão no bdd
    return render(request, "index.html", {"pessoas": pessoas}) #retorna um template, envia as pessoas p o template

def salvar(request):
    nome = request.POST.get("nome")
    Pessoa.objects.create(nome=nome) #cria o novo dado no banco
    pessoas = Pessoa.objects.all() 
    return render(request, "index.html", {"pessoas": pessoas}) #envia lista atualizada de pessoas p o index

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id) #recupera a pessoa do banco
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)