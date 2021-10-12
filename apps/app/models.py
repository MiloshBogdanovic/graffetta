# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from internationalflavor.vat_number import VATNumberField
from django.db import models
from django.db.models import ForeignKey
from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput, Select,  NumberInput, DateInput

ADMIN_CHOICE = [
    ('Legal', 'Legal'),
    ('Individual', 'Individual')
]

TITLE = [
    ('SIG.RA', 'SIG.RA'),
    ('GEOM.', 'GEOM.'),
    ('RAG.', 'RAG.'),
    ('ING.', 'ING.'),
    ('ARCH', 'ARCH'),
    ('ALTRO', 'ALTRO')
         ]


class AdministrationLegal(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    company_reg_num = models.IntegerField(unique=True)
    vat_number = VATNumberField(countries=['IT'])
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=5)
    cap = models.CharField(max_length=20)
    municipal_reg_office = models.CharField(max_length=20)
    province_reg_office = models.CharField(max_length=20)
    legal_title_rep = models.CharField(null=True, max_length=10, choices=TITLE)
    leg_rep_name = models.CharField(max_length=50)
    leg_rep_surname = models.CharField(max_length=50)
    leg_rep_tax_code = models.CharField(max_length=20)
    leg_rep_dob = models.DateField(auto_now=False, auto_now_add=False)
    municipal_of_birth_of_leg = models.CharField(max_length=30)
    province_of_birth_of_leg = models.CharField(max_length=30)
    legal_street = models.CharField(max_length=50)
    legal_street_number = models.CharField(max_length=5)
    cap_legal = models.CharField(max_length=30)
    municipal_of_leg_residence = models.CharField(max_length=30)
    province_of_leg_residence = models.CharField(max_length=30)


class AdministrationIndividual(models.Model):
    id = models.AutoField(primary_key=True)
    title_of_admin = models.CharField(max_length=50)


class CondominiumData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    fiscal_code = models.IntegerField(blank=False)
    street = models.CharField(max_length=50, blank=False)
    street_number = models.CharField(max_length=5)
    municipality = models.CharField(max_length=50, blank=False)
    province = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    pec_mail = models.EmailField(max_length=254, blank=False)
    select_administrator = models.CharField(null=True, max_length=10, choices=ADMIN_CHOICE)
    admn_legal_id = models.ForeignKey(AdministrationLegal, on_delete=models.CASCADE, null=True)
    admn_individual_id = models.ForeignKey(AdministrationIndividual, on_delete=models.CASCADE, null=True)


class CondominiumForm(ModelForm):
    class Meta:
        model = CondominiumData
        fields = ('name', 'fiscal_code', 'street', 'street_number', 'municipality', 'province', 'email',
                  'pec_mail', 'select_administrator')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'id': 'cond_name'
            }),
            'fiscal_code': NumberInput(attrs={
                'class': 'form-control',
                'id': 'fiscal_code'
            }),
            'street': TextInput(attrs={
                'class': 'form-control',
                'id': 'street'
            }),
            'street_number': NumberInput(attrs={
                'class': 'form-control',
                'id': 'street_number'
            }),
            'municipality': TextInput(attrs={
                'class': 'form-control',
                'id': 'municipality'
            }),
            'province': TextInput(attrs={
                'class': 'form-control',
                'id': 'province'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter email",
                'id': "email"
            }),
            'pec_mail': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter email",
                'id': "pec_mail"
            }),
            'select_administrator': Select(attrs={
                'class': 'custom-select',
                'id': "select_administrator"
            })
        }


class AdministrationLegalForm(ModelForm):
    class Meta:
        model = AdministrationLegal
        exclude = ['id']
        widgets = {
            'company_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'company_name',
            }),
            'province': TextInput(attrs={
                'class': 'form-control',
                'id': 'province'
            }),
            'company_reg_num': NumberInput(attrs={
                'class': 'form-control',
                'id': 'company_reg_num'
            }),
            'vat_number': TextInput(attrs={
                'class': 'form-control',
                'id': 'vat_number'
            }),
            'street': TextInput(attrs={
                'class': 'form-control',
                'id': 'street'
            }),
            'street_number': NumberInput(attrs={
                'class': 'form-control',
                'id': 'street_number '
            }),
            'cap': TextInput(attrs={
                'class': 'form-control',
                'id': 'cap '
            }),
            'municipal_reg_office': TextInput(attrs={
                'class': 'form-control',
                'id': 'municipal_reg_office'
            }),
            'province_reg_office': TextInput(attrs={
                'class': 'form-control',
                'id': 'province_reg_office'
            }),
            'legal_title_rep': TextInput(attrs={
                'class': 'form-control',
                'id': 'legal_title_rep'
            }),
            'leg_rep_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'leg_rep_name'
            }),
            'leg_rep_surname': TextInput(attrs={
                'class': 'form-control',
                'id': 'leg_rep_surname'
            }),
            'leg_rep_tax_code': TextInput(attrs={
                'class': 'form-control',
                'id': 'leg_rep_tax_code'
            }),
            'leg_rep_dob': DateInput(attrs={
                'class': 'form-control',
                'id': 'leg_rep_dob'
            }),
            'municipal_of_birth_of_leg': TextInput(attrs={
                'class': 'form-control',
                'id': 'municipal_of_birth_of_leg'
            }),
            'province_of_birth_of_leg': TextInput(attrs={
                'class': 'form-control',
                'id': 'province_of_birth_of_leg'
            }),
            'legal_street': TextInput(attrs={
                'class': 'form-control',
                'id': 'legal_street'
            }),
            'legal_street_number': NumberInput(attrs={
                'class': 'form-control',
                'id': 'legal_street'
            }),
            'cap_legal': TextInput(attrs={
                'class': 'form-control',
                'id': 'cap_legal'
            }),
            'municipal_of_leg_residence': TextInput(attrs={
                'class': 'form-control',
                'id': 'municipal_of_leg_residence'
            }),
            'province_of_leg_residence': TextInput(attrs={
                'class': 'form-control',
                'id': 'province_of_leg_residence'
            }),

        }


class AdministrationIndividualForm(ModelForm):
    class Meta:
        model = AdministrationIndividual
        exclude = ['id']
