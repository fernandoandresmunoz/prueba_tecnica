# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pet(models.Model):
    photo = models.ImageField(upload_to='images')
    nombre_de_la_mascota = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)

    class Meta:
        pass
