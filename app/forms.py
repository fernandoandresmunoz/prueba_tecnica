from django.forms import ModelForm
from .models import Pet


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['photo', 'nombre_de_la_mascota', 'nickname']