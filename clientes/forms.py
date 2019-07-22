from django.forms import ModelForm
from .models import Person


class Personform(ModelForm):
    class Meta:
        model = Person
        fields = ['Nome', 'Sobrenome', 'Idade', 'Salário', 'Descrição', 'Foto']



