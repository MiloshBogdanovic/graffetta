from django.urls import path
from apps.professionals import views

urlpatterns = [
    path('ddi/', views.data_designer_individual, name='data-designer-individual'),
]
