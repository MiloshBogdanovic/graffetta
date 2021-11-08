from django.urls import path
from apps.professionals import views

urlpatterns = [
    path('choose', views.choose_profession,  name='choose-profession'),
    path('ddi/', views.data_designer_individual, name='data-designer-individual'),
    path('ddl/', views.data_designer_legal, name='data-designer-legal')
]
