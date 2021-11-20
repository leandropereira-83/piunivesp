from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    if request.session.get('usuario'):
        pass
        pass
        return HttpResponse('Estou na Home')
    else:
        return redirect ('/auth/login?status=2')   

# Create your views here.
