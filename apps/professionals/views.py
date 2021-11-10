from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.app.models import FormFaccata
from .models import Prof_table, DataDesignerIndividual, DataDesignerIndividualForm, DataDesignerLegalForm, \
    DataDesignerLegal, DataDirectorWorksIndividual, DataDirectorWorksIndividualForm, DataDirectorWorksLegalForm, \
    DataEnergyExpertIndividualForm, \
    DataEnergyExpertLegal, DataEnergyExpertLegalForm, DataResponsibleForWorksIndividualForm, \
    DataResponsibleForWorksLegalForm, \
    DataSecurityCoordinatorExecutionIndividualForm, DataSecurityCoordinatorExecutionLegal, \
    DataSecurityCoordinatorExecutionLegalForm, \
    DataSecurityCoordinatorIndividual, DataSecurityCoordinatorIndividualForm, DataSecurityCoordinatorLegal, \
    DataSecurityCoordinatorLegalForm, \
    DataThermoTechnicalIndividual, DataThermoTechnicalLegalForm, ProfessionChoiceForm, \
    DataSecurityCoordinatorExecutionIndividual, \
    DataDirectorWorksLegal, DataThermoTechnicalIndividualForm, DataThermoTechnicalLegal, DataEnergyExpertIndividual, \
    DataResponsibleForWorksIndividual, DataResponsibleForWorksLegal


@login_required(login_url="/login/")
def choose_profession(request, fff):
    form = ProfessionChoiceForm()
    if request.method == 'POST':
        form_to_redirect = ProfessionChoiceForm(request.POST)

    return render(request, 'choose-profession.html', {'form': form})


@login_required(login_url="/login/")
def choose_profession_and_type(request, prof, type, fff):
    print(prof,type,fff)
    profession = prof
    prof_table = Prof_table()
    prof_table.save()
    ff = FormFaccata.objects.get(pk=fff)
    ff.professionals = Prof_table.objects.get(pk=prof_table.id)
    ff.save()
    if profession == 'data-designer' and type == 'individual':
        form = DataDesignerIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataDesignerIndividualForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.designer_individual = DataDesignerIndividual.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif profession == 'data-designer' and type == 'legal':
        form = DataDesignerLegalForm()
        template = 'professional-legal.html'
        if request.method == 'POST':
            form = DataDesignerLegalForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.designer_legal = DataDesignerLegal.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif profession == 'data-security-coordinator-design' and type == 'individual':
        form = DataSecurityCoordinatorIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataSecurityCoordinatorIndividualForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.security_plan_individual = DataSecurityCoordinatorIndividual.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'data-security-coordinator-design' and type == 'legal':
        form = DataSecurityCoordinatorLegalForm()
        template = 'professional-legal.html'
        if request.method == 'POST':
            form = DataSecurityCoordinatorLegalForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.security_plan_legal = DataSecurityCoordinatorLegal.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'data-security-coordinator-execution' and type == 'individual':
        form = DataSecurityCoordinatorExecutionIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            form=DataSecurityCoordinatorExecutionIndividualForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.security_exe_individual = DataSecurityCoordinatorExecutionIndividual.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'data-security-coordinator-execution' and type == 'legal':
        form = DataSecurityCoordinatorExecutionLegalForm()
        template = 'professional-legal.html'
        if request.method == 'POST':
            form = DataSecurityCoordinatorExecutionLegalForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.security_exe_legal = DataSecurityCoordinatorExecutionLegal.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'director-works' and type == 'individual':
        form = DataDirectorWorksIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataDirectorWorksIndividualForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.director_works_individual = DataDirectorWorksIndividual.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'director-works' and type == 'legal':
        form = DataDirectorWorksLegalForm()
        template = 'professional-legal.html'
        if request.method == 'POST':
            form = DataDirectorWorksLegalForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.director_works_legal = DataDirectorWorksLegal.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'thermotechnical' and type == 'individual':
        form = DataThermoTechnicalIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataThermoTechnicalIndividualForm()
            if form.is_valid():
                m = form.save()
                prof_table.thermotechnical_individual = DataThermoTechnicalIndividual.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'thermotechnical' and type == 'legal':
        form = DataThermoTechnicalLegalForm()
        template = 'professional-legal.html'
        if request.method == 'POST':
            form = DataThermoTechnicalLegalForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.thermotechnical_legal = DataThermoTechnicalLegal.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', args={'fff': fff})
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'data-energy-expert' and type == 'individual':
        form = DataEnergyExpertIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataEnergyExpertIndividualForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.energy_expert_individual = DataEnergyExpertIndividual.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'data-energy-expert' and type == 'legal':
        form = DataEnergyExpertLegalForm()
        template = 'professional-legal.html'
        if request.method == 'POST':
            form = DataEnergyExpertLegalForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.energy_expert_legal = DataEnergyExpertLegal.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'data-responsible' and type == 'individual':
        form = DataResponsibleForWorksIndividualForm()
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataResponsibleForWorksIndividualForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.resp_work_individual = DataResponsibleForWorksIndividual.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})

    elif profession == 'data-responsible' and type == 'lega':
        form = DataResponsibleForWorksLegalForm()
        template = 'professional-legal.html'
        if request.method == 'POST':
            form = DataResponsibleForWorksLegalForm(request.POST)
            if form.is_valid():
                m = form.save()
                prof_table.resp_work_legal = DataResponsibleForWorksLegal.objects.get(pk=m.id)
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('choose-profession', fff=fff)
            else:
                messages.error(request, form.errors)
                return render(request, template, {'error': form.errors})
    print('im down')
    return render(request, template, {'form': form, 'fff': fff})
