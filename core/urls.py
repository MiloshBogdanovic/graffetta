# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.app.admin import admin_site
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", include("apps.authentication.urls")),
    path('admin/', admin_site.urls),
    path("tables/", include("apps.tables.urls")),
    path("beneficiary/", include("apps.beneficary.urls")),
    path("prof/", include("apps.professionals.urls")),
    path("superbonus/", include("apps.superbonus.urls")),
    path("", include("apps.app.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]





#