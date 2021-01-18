from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import AUser
import requests


# Create your views here.
def home(request):
    context = {
        'users': AUser.objects.all().order_by('f_name', 'l_name')
    }
    return render(request, 'users_table/home.html', context)


def cadastrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            f_name = form.cleaned_data.get('f_name')
            l_name = form.cleaned_data.get('l_name')
            messages.success(request, f'Usuário {f_name} {l_name} criado com sucesso!')
            return redirect('home')
    else:
        name1, name2, name3 = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio').json()
        form = UserRegisterForm(initial={
            'f_name': name1,
            'l_name': f'{name2} {name3}',
        })
    return render(request, 'users_table/cadastrar.html', {'form': form})


def sobre(request):
    return render(request, 'users_table/sobre.html')