# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.forms import ModelForm
from django.forms.widgets import EmailInput, PasswordInput, CheckboxInput, TextInput, Select, Textarea


OPTIONS_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]


class FormOne(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    check_me_out = models.BooleanField(default=False)
    text = models.TextField(max_length=54)
    example_select = models.IntegerField(choices=OPTIONS_CHOICES)
    text_area = models.TextField(max_length=254)


class FormForFormOne(ModelForm):
    class Meta:
        model = FormOne
        fields = ('email', 'password', 'check_me_out', 'text', 'example_select', 'text_area')
        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter email",
                'id': "exampleInputEmail1"
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Password",
                'id': "exampleInputPassword1"
            }),
            'check_me_out': CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': "exampleCheck1"

            }),
            'text': TextInput(attrs={
                'class': 'form-control'
            }),
            'example_select': Select(attrs={
                'class': 'form-control',
                'id': "exampleFormControlSelect1"
            }),
            'text_area': Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'id': "exampleFormControlTextarea1"
            })

        }
