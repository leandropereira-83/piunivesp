from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import UC, AtividadeUC

def home(request):

    if request.session.get('usuario'):
        uc = UC.objects.all()
        request_usuario = request.session.get('usuario')
        return render(request, 'home.html', {'uc': uc, 'request_usuario':request_usuario})
    else:
        return redirect('/auth/login/?status=2')
        '''  if request.session.get('usuario'):
        pass
        pass
        return HttpResponse('Estou na Home')
        else:
        return redirect ('/auth/login?status=2') '''  

def uc(request, id):
    v_uc=UC.objects.get(id = id)
    atividades = AtividadeUC.objects.filter(uc = v_uc )
    return render(request, 'uc.html',{'atividades':atividades})


def atividades(request, id):
    if request.session.get('usuario'):
        atividades = AtividadeUC.objects.get(id = id)
        return render(request, 'atividade.html', {'atividades': atividades})
    else:
        return redirect('auth/login/status=2')
# Create your views here.
