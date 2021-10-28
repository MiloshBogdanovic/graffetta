from django.urls import path
from apps.tables import views

urlpatterns = [

    path('', views.tables, name='tables'),
    path('common-works', views.tables, name='common'),
    path('subjective-works', views.tables, name='subjective'),

]
