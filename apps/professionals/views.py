from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.professionals.models import DataDesignerIndividualForm, DataDesignerLegalForm, ProfessionChoiceForm

# Create your views here.
@login_required(login_url="/login/")
def data_designer_individual(request):
    form = DataDesignerIndividualForm()
    if request.method == 'POST':
        form_to_save = DataDesignerIndividualForm(request.POST)
        if form_to_save.is_valid():
            form_to_save.save()
    return render(request, 'professional-individual.html', {'title': 'Data Designer Individual', 'form': form})

@login_required(login_url="/login/")
def data_designer_legal(request):
    form = DataDesignerLegalForm()
    if request.method == 'POST':
        form_to_save = DataDesignerLegalForm(request.POST)
        if form_to_save.is_valid():
            form_to_save.save()
    return render(request, 'professional-legal.html', {'title': 'Data Designer Legal', 'form': form})

@login_required(login_url="/login/")
def choose_profession(request):
    form = ProfessionChoiceForm()
    if request.method == 'POST':
        print('yeet')
        print(request.POST)
        form_to_redirect = ProfessionChoiceForm(request.POST)     
        print (form_to_redirect['type'])
        print(form_to_redirect['professions'])
        
    return render(request, 'choose-profession.html', {'form':form})
