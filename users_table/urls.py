from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('sobre/', views.sobre, name='sobre'),
]