
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('uc/<int:id>', views.uc, name='uc'),
    path('atividades/<int:id>', views.atividades, name='atividades')
]

