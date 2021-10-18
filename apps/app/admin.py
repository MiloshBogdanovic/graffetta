# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite
from .models import AdministrationLegal,AdministrationIndividual, CondominiumData, CatastalData, FormFaccata
from django.contrib import admin

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'


class AdminAdministratorLegal(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["company_name"].label = "DENOMINAZIONE SOCIETA"
        form.base_fields["province"].label = 'PROVINCIA/E ISCRIZIONE REGISTRO IMPRESE'
        form.base_fields["company_reg_num"].label = 'N° ISCRIZIONE REGISTRO IMPRESE - PARTITA IVA - C.F.'
        form.base_fields["vat_number"].label = ''
        form.base_fields["street"].label = 'VIA E NUMERO SEDE LEGALE'
        form.base_fields["cap"].label = 'CAP SEDE LEGALE'
        form.base_fields["municipal_reg_office"].label = 'COMUNE SEDE LEGALE'
        form.base_fields["province_reg_office"].label = 'PROVINCIA SEDE LEGALE'
        form.base_fields["legal_title_rep"].label = 'TITOLO LEGALE RAPPRESENTATE'
        form.base_fields["leg_rep_name"].label = 'COGNOME E NOME LEGALE RAPPRESENTANTE'
        form.base_fields["leg_rep_tax_code"].label = 'CODICE FISCALE LEGALE RAPPRESENTATE'
        form.base_fields["leg_rep_dob"].label = 'DATA DI NASCITA LEGALE RAPPRESENTANTE'
        form.base_fields["municipal_of_birth_of_leg"].label = 'COMUNE DI NASCITA DEL LEGALE RAPPRESENTANTE'
        form.base_fields["province_of_birth_of_leg"].label = 'PROVINCIA DI NASCITA DEL LEGALE RAPPRESENTANTE'
        form.base_fields["legal_street"].label = 'VIA E NUMERO RESIDENZA LEGALE RAPPRESENTANTE'
        form.base_fields["legal_street_number"].label = 'NUMERO RESIDENZA LEGALE RAPPRESENTANTE'
        form.base_fields["cap_legal"].label = 'CAP RESIDENZA LEGALE RAPPRESENTANTE'
        form.base_fields["municipal_of_leg_residence"].label = 'COMUNE DI RESIDENZA LEGALE RAPPRESENTANTE'
        form.base_fields["province_of_leg_residence"].label = 'PROVINCIA DI RESIDENZA LEGALE RAPPRESENTANTE'
        return form

class AdminIndividualPanel(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = 'TITOLO AMMINISTRATORE'
        form.base_fields['name'].label = 'COGNOME e NOME'
        form.base_fields['fiscal_code'].label = 'CODICE FISCALE'
        form.base_fields['vat_number'].label = 'PARTITA IVA'
        form.base_fields['dob'].label = 'DATA DI NASCITA'
        form.base_fields['birthplace'].label = 'COMUNE DI NASCITA'
        form.base_fields['birthplace_county'].label = 'PROVINCIA DI NASCITA'
        form.base_fields['activity_street'].label = 'VIA E NUMERO/I SEDE ATTIVITA'
        form.base_fields['activity_location_cap'].label = 'CAP SEDE ATTIVITA'
        form.base_fields['activity_municipality'].label = 'COMUNE SEDE ATTIVITA'
        form.base_fields['activity_province'].label = 'PROVINCIA SEDE ATTIVITA'
        form.base_fields['residence_street'].label = 'VIA E NUMERO RESIDENZA'
        form.base_fields['residence_cap'].label = 'CAP RESIDENZA'
        form.base_fields['residence_city'].label = 'COMUNE DI RESIDENZA'
        form.base_fields['residence_province'].label = 'PROVINCIA DI RESIDENZA'
        return form

class AdminCondominiumPanel(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['name'] = "DENOMINAZIONE CONDOMINIO"
        form.base_fields['fiscal_code'] = "CODICE FISCALE CONDOMINIO"
        form.base_fields['street'] = "VIA E NUMERO/I UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['cap'] = "CAP UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['municipality'] = "COMUNE UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['province'] = "PROVINCIA UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['email'] = "INDIRIZZO MAIL DEL CONDOMINIO"
        form.base_fields['pec_mail'] = "INDIRIZZO PEC DEL CONDOMINIO"
        form.base_fields['select_administrator'] = "SELEZIONA AMMINISTRATORE"
        return form

class AdminCatastalDataPanel(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['n_catastal_cheet'] = "N° FOGLIO CATASTALE DI APPARTENENZA"
        form.base_fields['n_first_particle'] = "N° PRIMA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_first_belonging'] = "N° SUBALTERNI APPARTENTI ALLA PRIMA PARTICELLA"
        form.base_fields['n_second_particle'] = "N° SECONDA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_second_belonging'] = "N° SUBALTERNI APPARTENTI ALLA SECONDA PARTICELLA"
        form.base_fields['n_third_particle'] = "N° TERZA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_third_belonging'] = "N° SUBALTERNI APPARTENTI ALLA TERZA PARTICELLA"
        form.base_fields['n_fourth_particle'] = "N° QUARTA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_fourth_belonging'] = "N° SUBALTERNI APPARTENTI ALLA QUARTA PARTICELLA"
        form.base_fields['description_of_intervention'] = "DESCRIZIONE SINTETICA DELL'INTERVENTO"
        form.base_fields['data_of_condominium_assembly'] = "DATA ASSEMBLEA CONDOMINIALE IN CUI I CONDOMINI"
        return form
    
admin_site = MyAdminSite(name='admin')
admin_site.register(AdministrationLegal, admin_class=AdminAdministratorLegal)
admin_site.register(AdministrationIndividual, admin_class=AdminIndividualPanel)
admin_site.register(CondominiumData, admin_class=AdminCondominiumPanel)
admin_site.register(CatastalData)
admin_site.register(FormFaccata)
admin_site.register(User)
admin_site.register(Group)


