# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps.app.admin import admin_site
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin_site.urls),          # Django admin route
    path("tables/", include("apps.tables.urls")),
    path("beneficiary/", include("apps.beneficary.urls")),
    path("prof/", include("apps.professionals.urls")),
    path("superbonus/", include("apps.superbonus.urls")),
    path("", include("apps.authentication.urls")),
    path("", include("apps.app.urls")), # UI Kits Html files

]
