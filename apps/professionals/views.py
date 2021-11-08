from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.professionals.models import DataDesignerIndividualForm, DataDesignerLegalForm

# Create your views here.
@login_required(login_url="/login/")
def data_designer_individual(request):
    print('yeet')
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
    return render(request, 'professional-individual.html', {'title': 'Data Designer Legal', 'form': form})

