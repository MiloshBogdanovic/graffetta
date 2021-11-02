from django.urls import path
from apps.tables import views

urlpatterns = [

    path('<int:fff>', views.tables, name='tables'),
    path('common/<int:tc_id>', views.common, name='common'),
    path('subjective/<int:tc_id>', views.subjective, name='subjective'),

]
