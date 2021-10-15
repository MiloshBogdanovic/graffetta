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
        form.base_fields["company_name"].label = "COMPANY NAME"
        return form


admin_site = MyAdminSite(name='admin')
admin_site.register(AdministrationLegal, admin_class=AdminAdministratorLegal)
admin_site.register(AdministrationIndividual)
admin_site.register(CondominiumData)
admin_site.register(CatastalData)
admin_site.register(FormFaccata)
admin_site.register(User)
admin_site.register(Group)


