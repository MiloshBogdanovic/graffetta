from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
    DataResponsibleForWorksIndividual, DataResponsibleForWorksLegal, ProfTableForm


@login_required(login_url="/login/")
def choose_profession(request, fff):
    form = ProfessionChoiceForm()
    context = {}
    if request.method == 'POST':
        form_to_redirect = ProfessionChoiceForm(request.POST)
    ff = FormFaccata.objects.get(pk=fff)
    print(ff.professionals_id)
    if ff.professionals_id:
        prof_table = Prof_table.objects.get(pk=ff.professionals_id)
        prof_form = ProfTableForm(instance=prof_table)
        context['prof_form'] = prof_form
    context['form'] = form
    context['fff'] = fff
    return render(request, 'choose-profession.html', context)


@login_required(login_url="/login/")
def choose_profession_and_type(request, prof, type, fff):
    print(prof,type,fff)
    profession = prof
    ff = FormFaccata.objects.get(pk=fff)
    if ff.professionals_id:
        prof_table = Prof_table.objects.get(pk=ff.professionals_id)
    else:
        prof_table = Prof_table()
        prof_table.save()
        ff.professionals_id = Prof_table.objects.get(pk=prof_table.id)
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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})

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
                return render(request, template, {'form': form})
    print('im down')
    return render(request, template, {'form': form, 'fff': fff})


@login_required(login_url="/login/")
def edit_profession(request, prof, type, fff):
    ff = get_object_or_404(FormFaccata, id=fff)
    prof_table = get_object_or_404(Prof_table, id=ff.professionals_id)
    if prof == 'data-designer' and type == 'individual':
        edit_tbl = get_object_or_404(DataDesignerIndividual, id=prof_table.designer_individual_id)
        form = DataDesignerIndividualForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataDesignerIndividualForm(request.POST,instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})
    elif prof == 'data-designer' and type == 'legal':
        edit_tbl = get_object_or_404(DataDesignerLegal, id=prof_table.designer_legal_id)
        form = DataDesignerLegalForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataDesignerIndividualForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'data-security-coordinator-design' and type == 'individual':
        edit_tbl = get_object_or_404(DataSecurityCoordinatorIndividual, id=prof_table.security_plan_individual_id)
        form = DataSecurityCoordinatorIndividualForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataSecurityCoordinatorIndividualForm(request.POST,instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})
    elif prof == 'data-security-coordinator-design' and type == 'legal':
        edit_tbl = get_object_or_404(DataSecurityCoordinatorLegal, id=prof_table.security_plan_legal_id)
        form = DataSecurityCoordinatorLegalForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataSecurityCoordinatorLegalForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'data-security-coordinator-execution' and type == 'individual':
        edit_tbl = get_object_or_404(DataSecurityCoordinatorExecutionIndividual, id=prof_table.security_exe_individual_id)
        form = DataSecurityCoordinatorExecutionIndividualForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataSecurityCoordinatorExecutionIndividualForm(request.POST,instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})
    elif prof == 'data-security-coordinator-execution' and type == 'legal':
        edit_tbl = get_object_or_404(DataSecurityCoordinatorExecutionLegal, id=prof_table.security_exe_legal_id)
        form = DataSecurityCoordinatorExecutionLegalForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataSecurityCoordinatorExecutionLegalForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'director-works' and type == 'individual':
        edit_tbl = get_object_or_404(DataDirectorWorksIndividual, id=prof_table.director_works_individual_id)
        form = DataDirectorWorksIndividualForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataDirectorWorksIndividualForm(request.POST,instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'director-works' and type == 'legal':
        edit_tbl = get_object_or_404(DataDirectorWorksLegal, id=prof_table.director_works_legal_id)
        form = DataDirectorWorksLegalForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataDirectorWorksLegalForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'thermotechnical' and type == 'individual':
        edit_tbl = get_object_or_404(DataThermoTechnicalIndividual, id=prof_table.thermotechnical_individual_id)
        form = DataThermoTechnicalIndividualForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataThermoTechnicalIndividualForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'thermotechnical' and type == 'legal':
        edit_tbl = get_object_or_404(DataThermoTechnicalLegal, id=prof_table.thermotechnical_legal_id)
        form = DataThermoTechnicalLegalForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataThermoTechnicalLegalForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'data-energy-expert' and type == 'individual':
        edit_tbl = get_object_or_404(DataEnergyExpertIndividual, id=prof_table.energy_expert_individual_id)
        form = DataEnergyExpertIndividualForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataEnergyExpertIndividualForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'data-energy-expert' and type == 'legal':
        edit_tbl = get_object_or_404(DataEnergyExpertLegal, id=prof_table.energy_expert_legal_id)
        form = DataEnergyExpertLegalForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataEnergyExpertLegalForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'data-responsible' and type == 'individual':
        edit_tbl = get_object_or_404(DataResponsibleForWorksIndividual, id=prof_table.resp_work_individual_id)
        form = DataResponsibleForWorksIndividualForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataResponsibleForWorksIndividualForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    elif prof == 'data-responsible' and type == 'legal':
        edit_tbl = get_object_or_404(DataResponsibleForWorksLegal, id=prof_table.resp_work_legal_id)
        form = DataResponsibleForWorksLegalForm(instance=edit_tbl)
        template = 'professional-individual.html'
        if request.method == 'POST':
            form = DataResponsibleForWorksLegalForm(request.POST, instance=edit_tbl)
            if form.is_valid():
                m = form.save()
                prof_table.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')

            else:
                messages.error(request, form.errors)
                return render(request, template, {'form': form})

    return render(request, template, {'form': form, 'fff': fff})