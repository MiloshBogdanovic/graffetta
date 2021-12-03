from django.urls import path
from apps.superbonus import views



urlpatterns = [
    path('', views.app,  name='bonus-app-view'),
    path('add<int:id>', views.add_condo,  name='bonus-add-condo'),
    path('add<int:id>', views.add_villa,  name='bonus-add-villa'),
]
