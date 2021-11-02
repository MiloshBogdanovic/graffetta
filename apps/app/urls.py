# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('cond/<int:id>', views.condt, name='condtable'),
    path('individ/<int:id>', views.individt, name='individtable'),
    path('flegal/<int:id>', views.flegalt, name='legaltable'),
    path('catast/<int:id>', views.catastt, name='catasttable'),
    # Matches any html file
    path('bonus-faccata/', views.bonus, name='bonus'),
    path('bonus-faccata/<int:form>', views.bonus, name='bonus'),
    path('bonus-faccata/legal<int:form>', views.legal, name='legal'),
    path('bonus-faccata/individual<int:form>', views.individual, name='individual'),
    path('bonus-faccata/catastal<int:form>', views.catastal, name='catastal'),
    path('search', views.search, name='search_results'),
    re_path(r'^.*\.*', views.pages, name='pages'),


]


