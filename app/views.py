# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render, render_to_response

from .forms import PetForm
from .models import Pet

# Create your views here.

def cargar_foto(request):

    if request.method == 'POST':

        petForm = PetForm(request.POST, request.FILES)

        if petForm.is_valid():
            pet = petForm.save(commit=False)
            pet.save()
            return render(request, 'preview.html')


    petForm = PetForm()
    return render(request, 'load.html', { "petForm": petForm })

def home(request):
    pets = Pet.objects.all()
    return render(request, 'index.html', { 'pets': pets})
