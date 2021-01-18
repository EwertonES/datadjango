from django import forms
from .models import AUser

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = AUser
        fields = ['f_name', 'l_name', 'age', 'b_date', 'email', 'nickname', 'observation']
        labels = {
            'f_name': 'Nome',
            'l_name': 'Sobrenome',
            'age': 'Idade',
            'b_date': 'Data de Nascimento',
            'email': 'Email',
            'nickname': 'Apelido',
            'observation': 'Observacao',
        }