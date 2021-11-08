from django.urls import path
from apps.beneficary import views

urlpatterns = [
    path('<int:fff>', views.beneficiary, name='beneficiary'),
    path('-add/<int:id>', views.beneficiary_add, name='beneficiary-add'),
    path('-edit/<int:id>', views.beneficiary_edit, name='beneficiary-edit'),
]