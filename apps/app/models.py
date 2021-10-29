# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

#list_display = [field.name for field in OverallReport._meta.get_fields()]
# Create your models here.
from internationalflavor.vat_number import VATNumberField
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from apps.tables.models import TableContract
# from apps.tables.models import OverallReport, OverallExVat, OverallIncVat, OverallTaxable, CommonWorkReport, CommonWorkExVat, CommonWorkIncVat, CommonWorkTaxable, SubjectiveWorkReport, SubjectiveWorkExVat


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
    vat_number = VATNumberField(countries=['IT'])
    street = models.CharField(max_length=100)
    cap = models.CharField(max_length=20)
    municipal_reg_office = models.CharField(max_length=20)
    province_reg_office = models.CharField(max_length=20)
    legal_title_rep = models.CharField(null=True, max_length=10, choices=TITLE)
    leg_rep_name = models.CharField(max_length=100)
    leg_rep_tax_code = models.CharField(max_length=20)
    leg_rep_dob = models.DateField(auto_now=False, auto_now_add=False)
    municipal_of_birth_of_leg = models.CharField(max_length=30)
    province_of_birth_of_leg = models.CharField(max_length=30)
    legal_street = models.CharField(max_length=50)
    cap_legal = models.CharField(max_length=30)
    municipal_of_leg_residence = models.CharField(max_length=30)
    province_of_leg_residence = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = True



class AdministrationIndividual(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, choices=TITLE)
    name = models.CharField(max_length=120)
    fiscal_code = models.CharField(max_length=16)
    vat_number = VATNumberField(countries=['IT', 'NL'])
    dob = models.DateField(auto_now=False, auto_now_add=False)
    birthplace = models.CharField(max_length=30)
    birthplace_county = models.CharField(max_length=30)
    activity_street = models.CharField(max_length=50)
    activity_location_cap = models.IntegerField()
    activity_municipality = models.CharField(max_length=50)
    activity_province = models.CharField(max_length=50)
    residence_street = models.CharField(max_length=50)
    residence_cap = models.IntegerField(blank=False)
    residence_city = models.CharField(max_length=50)
    residence_province = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        managed = True


class CondominiumData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    fiscal_code = models.IntegerField(blank=False)
    street = models.CharField(max_length=50, blank=False)
    cap = models.IntegerField(blank=False)
    municipality = models.CharField(max_length=50, blank=False)
    province = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    pec_mail = models.EmailField(max_length=254, blank=False)
    select_administrator = models.CharField(null=True, max_length=10, choices=ADMIN_CHOICE)

    def __str__(self):
        return self.name

    class Meta:
        managed = True


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

    class Meta:
        managed = True

class DataInitial(models.Model):
    id = models.AutoField(primary_key=True)
    condominium = models.ForeignKey(CondominiumData, models.SET_NULL, blank=True, null=True)
    admin_legal = models.ForeignKey(AdministrationLegal, models.SET_NULL, blank=True, null=True)
    admin_individual = models.ForeignKey(AdministrationIndividual, models.SET_NULL, blank=True, null=True)
    catastal = models.ForeignKey(CatastalData, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = True


class FormFaccata(models.Model):
    id = models.AutoField(primary_key=True)
    datainit = models.ForeignKey(DataInitial, models.SET_NULL, blank=True, null=True)
    tables = models.ForeignKey(TableContract, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = True


class CondominiumForm(ModelForm):
    class Meta:
        model = CondominiumData
        exclude = ['id']
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
            'vat_number': TextInput(attrs={
                'class': 'form-control',
                'id': 'vat_number'
            }),
            'street': TextInput(attrs={
                'class': 'form-control',
                'id': 'street'
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
            'leg_rep_tax_code': TextInput(attrs={
                'class': 'form-control',
                'id': 'leg_rep_tax_code'
            }),
            'leg_rep_dob': DateInput(attrs={
                'class': 'form-control',
                'id': 'leg_rep_dob',
                'type': 'date'
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
            'title': Select(attrs={
                'class': 'form-control',
                'id': 'title'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'id': 'name'
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
                'id': 'dob',
                'type': 'date'
            }),
            'birthplace': TextInput(attrs={
                'class': 'form-control',
                'id': 'birthplace'
            }),
            'birthplace_county': TextInput(attrs={
                'class': 'form-control',
                'id': 'birthplace_county'
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
                'id': 'data_of_condominium_assembly',
                'type': 'date'
            }),
        }
