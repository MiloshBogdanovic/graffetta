from django.urls import path
from apps.superbonus import views
from django.urls import include, re_path


urlpatterns = [
    path('', views.app,  name='bonus-app-view'),
    path('add-condo', views.add_condo,  name='bonus-add-condo'),
    path('add-villa', views.add_villa,  name='bonus-add-villa'),
    path('interventions/<int:id>', views.interventions, name='bonus-add-intervention'),
    path('preview/<int:id>', views.preview, name='bonus-preview'),
    path('catastal/<int:id>', views.catastal, name='bonus-catastal'),
    path('beneficiary/<int:id>', views.beneficiary, name='bonus-beneficiary'),
    path('beneficiary/<int:id>/<int:ben_id>', views.edit_beneficiary, name='bonus-edit-beneficiary'),
    path('interventions-costs/<int:id>/<str:type>', views.intervention_costs, name='bonus-costs'),
    path('add-interventions-costs/<int:id>/<str:type>', views.add_intervention_costs, name='add-bonus-costs'),
    path('edit-interventions-costs/<int:id>/<str:type>', views.edit_intervention_costs, name='edit-bonus-costs'),
    path('add-professional/<int:id>', views.professionals, name='bonus-professional'),
    path('add-professional/<int:id>/<str:type>/<str:prof>/', views.add_professionals, name='bonus-add-professional'),
    path('add-administrator/<int:id>', views.administrator, name='bonus-administrator'),
    path('delete/<str:type>/<int:id>', views.delete_prop, name='bonus-delete'),
    path('bank-requirements/<int:id>/', views.bank_requirements, name='bank-requirements'),
    path('bank-req-file-edit/<int:id>/<int:file_id>/', views.edit_bank_file, name='bank-file-edit'),
    path('bank-file-status-edit/<int:id>/<int:file_id>/', views.edit_bank_file_status, name='bank-file-status-edit'),
    re_path(r'^bank-file/download/(?P<path>.*)$', views.download_bank_file, name='bank-file-download'),
    path('bank-file-status-delete/<int:id>/<int:file_id>/', views.delete_bank_file, name='delete-bank-file'),
]