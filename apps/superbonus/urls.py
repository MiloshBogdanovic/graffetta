from django.urls import path
from apps.superbonus import views



urlpatterns = [
    path('', views.app,  name='bonus-app-view'),
    path('add-condo', views.add_condo,  name='bonus-add-condo'),
    path('add-villa', views.add_villa,  name='bonus-add-villa'),
    path('interventions/<int:id>', views.interventions, name='bonus-add-intervention'),
    path('preview/<int:id>', views.preview, name='bonus-preview'),
    path('catastal/<int:id>', views.catastal, name='bonus-catastal'),
    path('beneficiary/<int:id>', views.beneficiary, name='bonus-beneficiary'),
    path('delete/<str:type>/<int:id>', views.delete_prop, name='bonus-delete'),
]
