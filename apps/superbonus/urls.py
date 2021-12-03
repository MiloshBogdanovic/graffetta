from django.urls import path
from apps.superbonus import views



urlpatterns = [
    path('', views.app,  name='bonus-app-view'),
    path('add-condo', views.add_condo,  name='bonus-add-condo'),
    path('add-villa', views.add_villa,  name='bonus-add-villa'),
    path('interventions', views.interventions, name='bonus-add-intervention'),
]
