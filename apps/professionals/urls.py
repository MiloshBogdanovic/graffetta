from django.urls import path
from apps.professionals import views

urlpatterns = [
    path('choose/<int:fff>', views.choose_profession,  name='choose-profession'),
    path('prof=<str:prof>/type=<str:type>/fff=<int:fff>', views.choose_profession_and_type, name='create-profession'),
    path('edit/prof=<str:prof>/type=<str:type>/fff=<int:fff>', views.edit_profession, name='edit-profession')
]
