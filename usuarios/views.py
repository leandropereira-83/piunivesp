from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
import hashlib


def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/home')
    status = request.GET.get('status')
    print(status)

    return render (request, 'cadastro.html', {'status': status} )

def login(request):
    if request.session.get('usuario'):
        return redirect('/home')
    status = request.GET.get('status')
    return render (request, 'login.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario_existe = Usuario.objects.filter(email=email)
    if len(usuario_existe) > 0:
        #return HttpResponse ('Usuário já cadastrado')
        return redirect('/auth/cadastro?status=2')

    


    if len(senha)< 8 or len(senha)> 12:
        return redirect('/auth/cadastro?status=1')
        #return HttpResponse ('Sua senha deve ter entre 8 e 12 caracteres')

    if len(nome.strip()) == 0 or len (email.strip()) == 0:
        return redirect('/auth/cadastro?status=3')
        #return HttpResponse('Nome e e-mail não podem ser vazios')
    
    senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
    usuario = Usuario(nome=nome, senha=senha, email=email)

    try:

        usuario.save()
        #return HttpResponse(f'{nome} {email} {senha}')
        return redirect('/auth/cadastro?status=0')

    except:
        return HttpResponse ('Erro interno do sistema! Tente novamente em instantes.')

def valida_login(request):

    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    usuarios = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuarios) == 0:
        return redirect('/auth/login?status=1')
    elif len(usuarios) > 0:
        request.session['usuario'] = usuarios[0].id
        return HttpResponse ('x')

def sair(request):
  request.session.flush()
  return redirect('/auth/login')




    