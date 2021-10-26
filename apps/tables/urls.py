from django.urls import path
from apps.tables import views

urlpatterns = [

    path('', views.tables, name='tables'),

]
