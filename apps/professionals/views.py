from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.app.models import FormFaccata

from apps.professionals.models import DataDesignerIndividual, DataDesignerIndividualForm, DataDesignerLegalForm, DataDirectorWorksIndividual, DataDirectorWorksIndividualForm, DataDirectorWorksLegalForm, DataEnergyExpertIndividualForm, DataEnergyExpertLegal, DataEnergyExpertLegalForm, DataResponsibleForWorksIndividualForm, DataResponsibleForWorksLegalForm, DataSecurityCoordinatorExecutionIndividualForm, DataSecurityCoordinatorExecutionLegal, DataSecurityCoordinatorExecutionLegalForm, DataSecurityCoordinatorIndividual, DataSecurityCoordinatorIndividualForm, DataSecurityCoordinatorLegal, DataSecurityCoordinatorLegalForm, DataThermoTechnicalIndividual, DataThermoTechnicalLegalForm, ProfessionChoiceForm

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
        form_to_redirect = ProfessionChoiceForm(request.POST)
        print(form_to_redirect['type'])
        print(form_to_redirect['professions'])

    return render(request, 'choose-profession.html', {'form': form})

@login_required(login_url="/login/")
def choose_profession_and_type(request, profession, type, ff):
    form = None
    template = None
    prof_table = Prof_table()
    prof_table.save()
    f = FormFaccata.objects.get(pk=ff)
    f.Prof_table= Prof_table.objects.get(pk=prof_table.id)
    f.save()
    if(profession == 'data-designer' and type == 'individual'):
        form = DataDesignerIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            if form.is_valid():
                m=form.save()
                prof_table.data_designer= DataDesignerIndividual.objects.get(pk=prof_table.id)
                
    elif(profession == 'data-designer' and type == 'legal'):
        form = DataDesignerLegalForm()
        template = 'professional-legal.html'
    elif(profession == 'data-security-coordinator-design' and type == 'individual'):
        form = DataSecurityCoordinatorIndividualForm()
        template = 'professional-individual.html'
    elif(profession == 'data-security-coordinator-design' and type == 'legal'):
        form = DataSecurityCoordinatorLegalForm()
        template = 'professional-legal.html'
    elif(profession == 'data-security-coordinator-execution' and type == 'individual'):
        form = DataSecurityCoordinatorExecutionIndividualForm()
        template = 'professional-individual.html'
    elif(profession == 'data-security-coordinator-execution' and type == 'legal'):
        form = DataSecurityCoordinatorExecutionLegalForm()
        template = 'professional-legal.html'
    elif(profession == 'director-works' and type == 'individual'):
        form = DataDirectorWorksIndividualForm()
        template = 'professional-individual.html'
    elif(profession == 'director-works' and type == 'legal'):
        form = DataDirectorWorksLegalForm()
        template = 'professional-legal.html'
    elif(profession == 'thermotechnical' and type == 'individual'):
        form = DataThermoTechnicalIndividual()
        template = 'professional-individual.html'
    elif(profession == 'thermotechnical' and type == 'legal'):
        form = DataThermoTechnicalLegalForm()
        template = 'professional-legal.html'
    elif(profession == 'data-energy-expert' and type == 'individual'):
        form = DataEnergyExpertIndividualForm()
        template = 'professional-individual.html'
    elif(profession == 'data-energy-expert' and type == 'legal'):
        form = DataEnergyExpertLegalForm()
        template = 'professional-legal.html'
    elif(profession == 'data-responsible' and type == 'individual'):
        form = DataResponsibleForWorksIndividualForm()
        template = 'professional-individual.html'
    elif(profession == 'data-responsible' and type == 'lega'):
        form = DataResponsibleForWorksLegalForm()
        template = 'professional-legal.html'
    
    
    
    return render(request, template, {'form':form})
    