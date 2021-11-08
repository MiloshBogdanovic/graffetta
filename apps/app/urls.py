# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.app import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # Matches any html file
    path('bonus-faccata/', views.bonus, name='bonus'),
    path('bonus-faccata/<int:form>', views.bonus, name='condominio'),
    path('bonus-faccata/legal<int:form>/<int:fff>', views.legal, name='legal'),
    path('bonus-faccata/individual<int:form>', views.individual, name='individual'),
    path('bonus-faccata/catastal<int:form>', views.catastal, name='catastal'),
    path('search', views.search, name='search_results'),
    # Api views for editing tables
    path('edit-table-data', views.save_table_data, name='edit-table-data'),
    path('condominium', views.condo_list, name="condominium"),
    path('catastal', views.catastal_list, name="catastal"),
    path('admin-legal', views.admin_legal_list, name="admin-legal"),
    path('admin-individual', views.admin_individual_list, name="admin-individual"),
    path('edit-form/<str:table>/<int:id>', views.edit_form, name="edit-form"),
    re_path(r'^.*\.*', views.pages, name='pages')
]


