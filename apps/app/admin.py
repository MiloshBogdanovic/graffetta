# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite
from .models import AdministrationLegal, AdministrationIndividual, CondominiumData, CatastalData, FormFaccata, DataInitial
from django.contrib import admin
from apps.beneficary.models import Beneficiary
from apps.tables.models import *
from apps.professionals.models import *


# Register your models here.
class MyAdminSite(AdminSite):
    site_header = 'Auri-Soft Admin Page'


class AdminAdministratorLegal(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["company_name"].label = "DENOMINAZIONE SOCIETA"
        form.base_fields["province"].label = 'PROVINCIA/E ISCRIZIONE REGISTRO IMPRESE'
        form.base_fields["vat_number"].label = 'N° ISCRIZIONE REGISTRO IMPRESE - PARTITA IVA - C.F.'
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
        form.base_fields['name'].label  = "DENOMINAZIONE CONDOMINIO"
        form.base_fields['fiscal_code'].label  = "CODICE FISCALE CONDOMINIO"
        form.base_fields['street'].label  = "VIA E NUMERO/I UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['cap'].label  = "CAP UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['municipality'].label  = "COMUNE UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['province'].label  = "PROVINCIA UBICAZIONE CONDOMINIO - IMMOBILE"
        form.base_fields['email'].label  = "INDIRIZZO MAIL DEL CONDOMINIO"
        form.base_fields['pec_mail'].label  = "INDIRIZZO PEC DEL CONDOMINIO"
        form.base_fields['select_administrator'].label  = "SELEZIONA AMMINISTRATORE"
        return form


class AdminCatastalDataPanel(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['n_catastal_cheet'].label  = "N° FOGLIO CATASTALE DI APPARTENENZA"
        form.base_fields['n_first_particle'].label  = "N° PRIMA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_first_belonging'].label  = "N° SUBALTERNI APPARTENTI ALLA PRIMA PARTICELLA"
        form.base_fields['n_second_particle'].label  = "N° SECONDA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_second_belonging'].label  = "N° SUBALTERNI APPARTENTI ALLA SECONDA PARTICELLA"
        form.base_fields['n_third_particle'].label  = "N° TERZA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_third_belonging'].label  = "N° SUBALTERNI APPARTENTI ALLA TERZA PARTICELLA"
        form.base_fields['n_fourth_particle'].label  = "N° QUARTA PARTICELLA COSTITUENTE IL CONDOMINIO"
        form.base_fields['n_subscribers_to_fourth_belonging'].label  = "N° SUBALTERNI APPARTENTI ALLA QUARTA PARTICELLA"
        form.base_fields['description_of_intervention'].label  = "DESCRIZIONE SINTETICA DELL'INTERVENTO"
        form.base_fields['data_of_condominium_assembly'].label  = "DATA ASSEMBLEA CONDOMINIALE IN CUI I CONDOMINI"
        return form


admin_site = MyAdminSite(name='admin')
admin_site.register(AdministrationLegal, admin_class=AdminAdministratorLegal)
admin_site.register(AdministrationIndividual, admin_class=AdminIndividualPanel)
admin_site.register(CondominiumData, admin_class=AdminCondominiumPanel)
admin_site.register(CatastalData, admin_class=AdminCatastalDataPanel)
admin_site.register(FormFaccata)
admin_site.register(DataInitial)

admin_site.register(Beneficiary)

admin_site.register(OverallReport)
admin_site.register(OverallExVat)
admin_site.register(OverallIncVat)
admin_site.register(OverallTaxable)
admin_site.register(CommonWorkReport)
admin_site.register(CommonWorkExVat)
admin_site.register(CommonWorkIncVat)
admin_site.register(CommonWorkTaxable)
admin_site.register(SubjectiveWorkReport)
admin_site.register(SubjectiveWorkExVat)
admin_site.register(SubjectiveWorkIncVat)
admin_site.register(SubjectiveWorkTaxable)
admin_site.register(DataDesignerIndividual)
admin_site.register(DataDesignerLegal)
admin_site.register(DataSecurityCoordinatorIndividual)
admin_site.register(DataSecurityCoordinatorLegal)
admin_site.register(DataSecurityCoordinatorExecutionIndividual)
admin_site.register(DataSecurityCoordinatorExecutionLegal)
admin_site.register(DataDirectorWorksIndividual)
admin_site.register(DataDirectorWorksLegal)
admin_site.register(DataThermoTechnicalIndividual)
admin_site.register(DataThermoTechnicalLegal)
admin_site.register(DataEnergyExpertIndividual)
admin_site.register(DataEnergyExpertLegal)
admin_site.register(DataResponsibleForWorksIndividual)
admin_site.register(DataResponsibleForWorksLegal)
admin_site.register(Prof_table)
admin_site.register(User)
admin_site.register(Group)


