from django.urls import path
from apps.tables import views

urlpatterns = [

    path('<int:fff>', views.tables, name='tables'),
    path('overall-edit/<int:id>', views.overall_edit, name='tables-edit'),
    path('common/<int:tc_id>', views.common, name='common'),
    path('edit-common/<int:id>', views.common_edit, name='common-edit'),
    path('subjective/<int:tc_id>', views.subjective, name='subjective'),
    path('sub-edit/<int:id>', views.sub_edit, name='sub-edit'),

]
