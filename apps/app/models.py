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
from apps.professionals.models import Prof_table

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
    vat_number = VATNumberField(countries=['IT'])
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
    email = models.EmailField(max_length=254, blank=False, verbose_name='Email')
    pec_mail = models.EmailField(max_length=254, blank=False,verbose_name='PEC')
    select_administrator = models.CharField(null=True, max_length=10, choices=ADMIN_CHOICE)

    class Meta:
        managed = True


class CatastalData(models.Model):
    id = models.AutoField(primary_key=True)
    n_catastal_cheet = models.IntegerField(blank=False)
    n_first_particle = models.IntegerField(blank=False)
    n_subscribers_to_first_belonging = models.CharField(max_length=20, blank=False)
    n_second_particle = models.IntegerField(blank=True, null=True)
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
    condominium = models.ForeignKey(CondominiumData, on_delete=models.SET_NULL, blank=True, null=True)
    admin_legal = models.ForeignKey(AdministrationLegal, on_delete=models.SET_NULL, blank=True, null=True)
    admin_individual = models.ForeignKey(AdministrationIndividual, on_delete=models.SET_NULL, blank=True, null=True)
    catastal = models.ForeignKey(CatastalData, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = True


class FormFaccata(models.Model):
    id = models.AutoField(primary_key=True)
    datainit = models.ForeignKey(DataInitial, models.SET_NULL, blank=True, null=True)
    tables = models.ForeignKey(TableContract, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    professionals = models.ForeignKey(Prof_table, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'FORM ID-{self.id}'

    class Meta:
        managed = True


class CondominiumForm(ModelForm):
    class Meta:
        model = CondominiumData
        exclude = ['id']
        labels = {
            'name': 'DENOMINAZIONE CONDOMINIO',
            'fiscal_code': 'CODICE FISCALE',
            'street': 'VIA',
            'cap':'CAP',
            'municipality': 'COMUNE',
            'province': 'PROVINCIA',
            'email':'E-MAIL',
            'pec_mail':'PEC E-MAIL',
            'select_administrator':'TIPO DI AMMINISTRATORE'
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'id': 'cond_name',
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
                'id': "pec_mail",
                'verbose_name': 'PEC'
            }),
            'select_administrator': Select(attrs={
                'class': 'custom-select',
                'id': "select_administrator"
            })
        }
        error_messages = {
            'pec_mail': {
                'invalid': ("Inserisci una email valida per PEC"),

            },
            'email': {
                'invalid': ("Inserisci una email valida"),
            },
        }


class AdministrationLegalForm(ModelForm):
    class Meta:
        model = AdministrationLegal
        exclude = ['id']
        labels = {
            'company_name':'DENOMINAZIONE SOCIETA',
            'province':'PROVINCIA/E ISCRIZIONE REGISTRO IMPRESE',
            'vat_number':'N° ISCRIZIONE REGISTRO IMPRESE - PARTITA IVA - C.F.',
            'street':'VIA E NUMERO SEDE LEGALE',
            'cap':'CAP',
            'municipal_reg_office':'COMUNE SEDE LEGALE',
            'province_reg_office':'PROVINCIA SEDE LEGALE',
            'legal_title_rep':'TITOLO ',
            'leg_rep_name':'COGNOME E NOME LEGALE RAPPRESENTANTE',
            'leg_rep_tax_code':'CODICE FISCALE LEGALE RAPPRESENTATE',
            'leg_rep_dob':'DATA DI NASCITA LEGALE RAPPRESENTANTE',
            'municipal_of_birth_of_leg':'COMUNE DI NASCITA DEL LEGALE RAPPRESENTANTE',
            'province_of_birth_of_leg':'PROVINCIA DI NASCITA DEL LEGALE RAPPRESENTANTE',
            'legal_street':'VIA E NUMERO RESIDENZA LEGALE RAPPRESENTANTE',
            'cap_legal':'CAP RESIDENZA LEGALE RAPPRESENTANTE ',
            'municipal_of_leg_residence':'COMUNE DI RESIDENZA LEGALE RAPPRESENTANTE',
            'province_of_birth_of_leg':'PROVINCIA DI RESIDENZA LEGALE RAPPRESENTANTE'
        }
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
        error_messages = {
            'vat_number': {
                'invalid': ("Il numero di partita IVA dovrebbe iniziare con IT seguito da undici cifre"),
            },

        }


class AdministrationIndividualForm(ModelForm):
    class Meta:
        model = AdministrationIndividual
        exclude = ['id']
        labels = {
            'title':'TITOLO AMMINISTRATORE',
            'name':'NOME E COGNOME',
            'fiscal_code':'CODICE FISCALE',
            'vat_number':'PARTITA IVA',
            'dob':'DATA DI NASCITA',
            'birthplace':'LUOGO DI NASCITA',
            'birthplace_county':'PROVINCIA DI NASCITA',
            'activity_street':'VIA E NUMERO/I SEDE ATTIVITA',
            'activity_location_cap':'CAP SEDE ATTIVITA',
            'activity_municipality':'COMUNE SEDE ATTIVITA',
            'activity_province':'PROVINCIA SEDE ATTIVITA',
            'residence_street':'VIA E NUMERO RESIDENZA',
            'residence_cap':'CAP RESIDENZA',
            'residence_city':'LUOGO DI RESIDENZA',
            'residence_province':'PROVINCIA DI RESIDENZA'
        }
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
        error_messages = {
            'vat_number': {
                'invalid': ("Il numero di partita IVA dovrebbe iniziare con IT seguito da undici cifre"),
            },

        }


class CatastalDataForm(ModelForm):
    class Meta:
        model = CatastalData
        exclude = ['id']
        labels = {
            'n_catastal_cheet':'N° FOGLIO CATASTALE DI APPARTENENZA',
            'n_first_particle':'N° PRIMA PARTICELLA COSTITUENTE IL CONDOMINIO',
            'n_subscribers_to_first_belonging': 'N° SUBALTERNI APPARTENTI ALLA PRIMA PARTICELLA',
            'n_second_particle':'SECONDA PARTICELLA COSTITUENTE IL CONDOMINIO',
            'n_subscribers_to_second_belonging':'N° SUBALTERNI APPARTENTI ALLA SECONDA PARTICELLA',
            'n_third_particle':'N° TERZA PARTICELLA COSTITUENTE IL CONDOMINIO',
            'n_subscribers_to_third_belonging':'N° SUBALTERNI APPARTENTI ALLA TERZA PARTICELLA',
            'n_fourth_particle':'N° QUARTA PARTICELLA COSTITUENTE IL CONDOMINIO',
            'n_subscribers_to_fourth_belonging':'N° SUBALTERNI APPARTENTI ALLA QUARTA PARTICELLA',
            'description_of_intervention':"DESCRIZIONE SINTETICA DELL'INTERVENTO",
            'data_of_condominium_assembly':'DATA ASSEMBLEA CONDOMINIALE IN CUI I CONDOMINI HANNO IRREVOCABILMENTE OPTATO PER LO SCONTO IN FATTURA'
        }
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
