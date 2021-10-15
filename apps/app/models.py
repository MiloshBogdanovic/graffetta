# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


# Create your models here.
from internationalflavor.vat_number import VATNumberField
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput, Select, NumberInput, DateInput, Textarea

ADMIN_CHOICE = [
    ('Legal', 'Legale'),
    ('Individual', 'Individuale')
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
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    fiscal_code = models.CharField(max_length=16)
    vat_number = VATNumberField(countries=['IT', 'NL'])
    dob = models.DateField(auto_now=False, auto_now_add=False)
    birthplace = models.CharField(max_length=30)
    birthplace_county = models.CharField(max_length=30)
    activity_street_number = models.CharField(max_length=5)
    activity_street = models.CharField(max_length=50)
    activity_location_cap = models.IntegerField()
    activity_municipality = models.CharField(max_length=50)
    activity_province = models.CharField(max_length=50)
    residence_street_number = models.CharField(max_length=5)
    residence_street = models.CharField(max_length=50)
    residence_cap = models.IntegerField(blank=False)
    residence_city = models.CharField(max_length=50)
    residence_province = models.CharField(max_length=50)


class CondominiumData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    fiscal_code = models.IntegerField(blank=False)
    street = models.CharField(max_length=50, blank=False)
    street_number = models.CharField(max_length=5)
    cap = models.IntegerField(blank=False)
    municipality = models.CharField(max_length=50, blank=False)
    province = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    pec_mail = models.EmailField(max_length=254, blank=False)
    select_administrator = models.CharField(null=True, max_length=10, choices=ADMIN_CHOICE)


class CatastalData(models.Model):
    id = models.AutoField(primary_key=True)
    n_catastal_cheet = models.IntegerField(blank=False)
    n_first_particle = models.IntegerField(blank=False)
    n_subscribers_to_first_belonging = models.CharField(max_length=20, blank=False)
    n_second_particle = models.IntegerField(blank=False, null=True)
    n_subscribers_to_second_belonging = models.CharField(max_length=20, blank=True, null=True)
    n_third_particle = models.IntegerField(blank=True, null=True)
    n_subscribers_to_third_belonging = models.CharField(max_length=20, blank=True, null=True)
    n_fourth_particle = models.IntegerField(blank=True, null=True)
    n_subscribers_to_fourth_belonging = models.CharField(max_length=20, blank=True, null=True)
    description_of_intervention = models.CharField(max_length=500)
    data_of_condominium_assembly = models.DateField(auto_now=False, auto_now_add=False)


class FormFaccata(models.Model):
    id = models.AutoField(primary_key=True)
    condominium = models.ForeignKey(CondominiumData, models.SET_NULL, blank=True, null=True)
    admin_legal = models.ForeignKey(AdministrationLegal, models.SET_NULL, blank=True, null=True)
    admin_individual = models.ForeignKey(AdministrationIndividual, models.SET_NULL, blank=True, null=True)
    catastal = models.ForeignKey(CatastalData, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)


class CondominiumForm(ModelForm):
    class Meta:
        model = CondominiumData
        fields = ('name', 'fiscal_code', 'street', 'street_number', 'municipality', 'province', 'email',
                  'pec_mail', 'select_administrator','cap')
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
            'cap':NumberInput(attrs={
                'class':'form-control',
                'id':'cap'
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
            'cap': NumberInput(attrs={
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
            'legal_title_rep': Select(attrs={
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
        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'id':'title'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'first_name'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name'
            }),
            'fiscal_code': TextInput(attrs={
                'class': 'form-control',
                'id': 'fiscal_code'
            }),
            'vat_number': TextInput(attrs={
                'class': 'form-control',
                'id': 'vat_number'
            }),
            'dob': DateInput(attrs={
                'class': 'form-control',
                'id': 'dob'
            }),
            'birthplace': TextInput(attrs={
                'class': 'form-control',
                'id': 'birthplace'
            }),
            'birthplace_county': TextInput(attrs={
                'class': 'form-control',
                'id': 'birthplace_county'
            }),
            'activity_street_number': TextInput(attrs={
                'class': 'form-control',
                'id': 'activity_street_number'
            }),
            'activity_street': TextInput(attrs={
                'class': 'form-control',
                'id': 'activity_street'
            }),
            'activity_location_cap': NumberInput(attrs={
                'class': 'form-control',
                'id': 'birthplace_county'
            }),
            'activity_municipality': TextInput(attrs={
                'class': 'form-control',
                'id': 'activity_municipality'
            }),
            'activity_province': TextInput(attrs={
                'class': 'form-control',
                'id': 'activity_province'
            }),
            'residence_street_number': TextInput(attrs={
                'class': 'form-control',
                'id': 'residence_street_number'
            }),
            'residence_street': TextInput(attrs={
                'class': 'form-control',
                'id': 'residence_street'
            }),
            'residence_cap': NumberInput(attrs={
                'class': 'form-control',
                'id': 'residence_cap'
            }),
            'residence_city': TextInput(attrs={
                'class': 'form-control',
                'id': 'residence_city'
            }),
            'residence_province': TextInput(attrs={
                'class': 'form-control',
                'id': 'residence_province'
            }),
        }


class CatastalDataForm(ModelForm):
    class Meta:
        model = CatastalData
        exclude = ['id']
        widgets = {
            'n_catastal_cheet': NumberInput(attrs={
                'class': 'form-control',
                'id': 'n_catastal_cheet'
            }),
            'n_first_particle': NumberInput(attrs={
                'class': 'form-control',
                'id': 'n_first_particle'
            }),
            'n_subscribers_to_first_belonging': TextInput(attrs={
                'class': 'form-control',
                'id': 'n_subscribers_to_first_belonging'
            }),
            'n_second_particle': NumberInput(attrs={
                'class': 'form-control',
                'id': 'n_second_particle'
            }),
            'n_subscribers_to_second_belonging': TextInput(attrs={
                'class': 'form-control',
                'id': 'n_subscribers_to_second_belonging'
            }),
            'n_third_particle': NumberInput(attrs={
                'class': 'form-control',
                'id': 'n_third_particle'
            }),
            'n_subscribers_to_third_belonging': TextInput(attrs={
                'class': 'form-control',
                'id': 'n_subscribers_to_third_belonging'
            }),
            'n_fourth_particle': NumberInput(attrs={
                'class': 'form-control',
                'id': 'n_fourth_particle'
            }),
            'n_subscribers_to_fourth_belonging': TextInput(attrs={
                'class': 'form-control',
                'id': 'n_subscribers_to_fourth_belonging'
            }),
            'description_of_intervention': Textarea(attrs={
                'class': 'form-control',
                'id': 'description_of_intervention'
            }),
            'data_of_condominium_assembly': DateInput(attrs={
                'class': 'form-control',
                'id': 'data_of_condominium_assembly'
            }),
        }
