from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.template import loader
from .calculations import *
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import activate
from apps.beneficary.models import Beneficiary, BeneficiaryForm
from .forms import *
from django.conf import settings


@login_required(login_url="/login/")
def app(request):
    context = {'segment': 'bonus-app-view', 'table': SuperBonus.objects.all()}
    html_template = loader.get_template('superbonus.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_condo(request):
    activate('it')
    context = {'segment': 'bonus-add-condo', 'form': BonusCondoForm()}
    if request.method == 'POST':
        form = BonusCondoForm(request.POST)
        if form.is_valid():
            super_bonus = SuperBonus(bonus_condo=form.save())
            super_bonus.save()
            messages.success(request, 'Creato con successo')
            return redirect('bonus-preview', id=super_bonus.id)
        else:
            context['form'] = form
            messages.error(request, form.errors)

    html_template = loader.get_template('add-condo.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_villa(request):
    activate('it')
    context = {'segment': 'bonus-add-villa', 'form': BonusVillaForm()}
    if request.method == 'POST':
        form = BonusVillaForm(request.POST)
        if form.is_valid():
            super_bonus = SuperBonus(bonus_villa=form.save())
            super_bonus.save()
            messages.success(request, 'Creato con successo')
            return redirect('bonus-preview', id=super_bonus.id)
        else:
            context['form'] = form
            messages.error(request, form.errors)

    html_template = loader.get_template('add-villa.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def interventions(request, id):
    context = {'segment': 'interventions', 'id': id}
    html_template = loader.get_template('interventions.html')
    bonus = get_object_or_404(SuperBonus, pk=id)
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        if villa.interventions:
            intervention = Interventions.objects.get(id=villa.interventions_id)
            context['form'] = InterventionsForm(instance=intervention)
            if request.method == 'POST':
                form = InterventionsForm(request.POST, instance=intervention)
                if form.is_valid():
                    villa.interventions = form.save()
                    villa.save()
                    messages.success(request, 'Modifiche salvate con successo')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)
        else:
            context['form'] = InterventionsForm()
            if request.method == 'POST':
                form = InterventionsForm(request.POST)
                if form.is_valid():
                    villa.interventions = form.save()
                    villa.save()
                    messages.success(request, 'Creato con successo')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)

    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        if condo.interventions:
            intervention = Interventions.objects.get(id=condo.interventions_id)
            context['form'] = InterventionsCondoForm(instance=intervention)
            if request.method == 'POST':
                form = InterventionsCondoForm(request.POST, instance=intervention)
                if form.is_valid():
                    condo.interventions = form.save()
                    condo.save()
                    messages.success(request, 'Modifiche salvate con successo')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)

        else:
            context['form'] = InterventionsCondoForm()
            if request.method == 'POST':
                form = InterventionsCondoForm(request.POST)
                if form.is_valid():
                    condo.interventions = form.save()
                    condo.save()
                    messages.success(request, 'Creato con successo')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def catastal(request, id):
    context = {'segment': 'catastal', 'id': id}
    html_template = loader.get_template('catastal.html')
    bonus = get_object_or_404(SuperBonus, pk=id)
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        if villa.catastal:
            catastal = CatastalData.objects.get(id=villa.catastal_id)
            context['form'] = CatastalDataForm(instance=catastal)
            if request.method == 'POST':
                form = CatastalDataForm(request.POST, instance=catastal)
                if form.is_valid():
                    villa.catastal = form.save()
                    villa.save()
                    messages.success(request, 'Modifiche salvate con successo')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)
        else:
            context['form'] = CatastalDataForm()
            if request.method == 'POST':
                form = CatastalDataForm(request.POST)
                if form.is_valid():
                    villa.catastal = form.save()
                    villa.save()
                    messages.success(request, 'Creato con successo')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)
    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        if condo.catastal:
            catastal = CatastalData.objects.get(id=condo.catastal_id)
            context['form'] = CatastalDataForm(instance=catastal)
            if request.method == 'POST':
                form = CatastalDataForm(request.POST, instance=catastal)
                if form.is_valid():
                    condo.catastal = form.save()
                    condo.save()
                    messages.success(request, 'Modifiche salvate con successo Changed Values')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)
        else:
            context['form'] = CatastalDataForm()
            if request.method == 'POST':
                form = CatastalDataForm(request.POST)
                if form.is_valid():
                    condo.catastal = form.save()
                    condo.save()
                    messages.success(request, 'Creato con successo')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def beneficiary(request, id):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-beneficiary', 'id': id }
    html_template = loader.get_template('bonus-beneficiary.html')
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        context['form'] = BeneficiaryForm()
        context['table'] = villa.beneficiary.all()
        if request.method == 'POST':
            form = BeneficiaryForm(request.POST)
            if form.is_valid():
                f = form.save()
                villa.beneficiary.add(f)
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('bonus-preview', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        context['form'] = BeneficiaryForm()
        context['table'] = condo.beneficiary.all()
        if request.method == 'POST':
            form = BeneficiaryForm(request.POST)
            if form.is_valid():
                f = form.save()
                condo.beneficiary.add(f)
                messages.success(request, 'Modifiche salvate con successo Changed Values')
                return redirect('bonus-preview', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def edit_beneficiary(request, id, ben_id):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-edit-beneficiary', 'id': id }
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        edit = Beneficiary.objects.get(id=ben_id)
        context['form'] = BeneficiaryForm(instance=edit)
        if request.POST:
            form = BeneficiaryForm(request.POST,instance=edit)
            if form.is_valid():
                f = form.save()
                villa.beneficiary.add(f)
                messages.success(request, 'Modifiche salvate con successo Changed Values')
                return redirect('bonus-beneficiary', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        edit = Beneficiary.objects.get(id=ben_id)
        context['form'] = BeneficiaryForm(instance=edit)
        if request.POST:
            form = BeneficiaryForm(request.POST,instance=edit)
            if form.is_valid():
                f = form.save()
                condo.beneficiary.add(f)
                messages.success(request, 'Modifiche salvate con successo Changed Values')
                return redirect('bonus-beneficiary', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    html_template = loader.get_template('bonus-beneficiary.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def intervention_costs(request, id, type):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-costs', 'bonus': bonus, 'type': type, 'id': id}
    html_template = loader.get_template('bonus-overall-inter.html')
    return HttpResponse(html_template.render(context, request))


def add_intervention_costs(request, id, type):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'add-bonus-cost', 'bonus': bonus, 'type': type}
    html_template = loader.get_template('bonus-add-inter-cost.html')
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        if type == 'overall':
            if villa.overall_interventions is None:
                context['form'] = OverallInterCostsNOVatForm()
                if request.method == 'POST':
                    form = OverallInterCostsNOVatForm(request.POST)
                    try:
                        if form.is_valid():
                            cost = OverallInterventions.objects.create(excluding_vat=form.save())
                            villa.overall_interventions = cost
                            villa.save()
                            overall_calculation_villa(cost)
                            messages.success(request, 'Creato con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Overall intervention already exist')

        elif type == 'driving':
            if bonus.bonus_villa.driving_interventions is None:
                context['form'] = InterDrivingWorkNOVatForm()
                if request.method == 'POST':
                    form = InterDrivingWorkNOVatForm(request.POST)
                    try:
                        if form.is_valid():
                            cost = DrivingInterventions.objects.create(excluding_vat=form.save())
                            villa.driving_interventions = cost
                            villa.save()
                            driving_calculation_villa(cost)
                            messages.success(request, 'Creato con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Driving intervention already exist')

        elif type == 'trailed':
            if bonus.bonus_villa.trailed_interventions is None:
                context['form'] = InterTrailedWorkNOVatForm()
                if request.method == 'POST':
                    form = InterTrailedWorkNOVatForm(request.POST)
                    try:
                        if form.is_valid():
                            cost = TrailingInterventions.objects.create(excluding_vat=form.save())
                            villa.trailed_interventions = cost
                            villa.save()
                            trailed_calculation_villa(cost)
                            messages.success(request, 'Creato con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Trailed intervention already exist')

    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        if type == 'overall':
            if condo.overall_interventions is None:
                context['form'] = OverallInterCostsNOVatForm()
                if request.method == 'POST':
                    form = OverallInterCostsNOVatForm(request.POST)
                    try:
                        if form.is_valid():
                            cost = OverallInterventions.objects.create(excluding_vat=form.save())
                            condo.overall_interventions = cost
                            condo.save()
                            overall_calculation_villa(cost)
                            messages.success(request, 'Creato con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)

                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Overall intervention already exist')

        elif type == 'common':
            if bonus.bonus_condo.common_interventions is None:
                context['form'] = CommonWorkNOVatForm()
                if request.method == 'POST':
                    form = CommonWorkNOVatForm(request.POST)
                    try:
                        if form.is_valid():
                            cost = CommonInterventions.objects.create(excluding_vat=form.save())
                            condo.common_interventions = cost
                            condo.save()
                            common_calculation_condo(cost)
                            messages.success(request, 'Creato con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Common intervention already exist')

        elif type == 'subjective':
            if bonus.bonus_condo.subjective_interventions is None:
                context['form'] = SubjectiveWorkNOVatForm()
                if request.method == 'POST':
                    form = SubjectiveWorkNOVatForm(request.POST)
                    try:
                        if form.is_valid():
                            cost = SubjectiveInterventions.objects.create(excluding_vat=form.save())
                            condo.subjective_interventions = cost
                            condo.save()
                            subjective_calculation_condo(cost)
                            messages.success(request, 'Creato con successo Created  Subjective Interventions')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Subjective intervention already exist')

    bonus.save()
    return HttpResponse(html_template.render(context, request))


def edit_intervention_costs(request, id, type):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'edit-bonus-cost', 'bonus': bonus, 'type': type}
    html_template = loader.get_template('bonus-add-inter-cost.html')
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        if type == 'overall':
            if villa.overall_interventions:
                costs = OverallInterventions.objects.get(id=villa.overall_interventions_id)
                prev_form = OverallInterCostsNOVat.objects.get(id=costs.excluding_vat_id)
                context['form'] = OverallInterCostsNOVatForm(instance=prev_form)
                if request.method == 'POST':
                    form = OverallInterCostsNOVatForm(request.POST, instance=prev_form)
                    try:
                        if form.is_valid():
                            costs.excluding_vat = form.save()
                            overall_calculation_villa(costs)
                            messages.success(request, 'Modifiche salvate con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Overall intervention doesnt  exist')

        elif type == 'driving':
            if villa.driving_interventions:
                costs = DrivingInterventions.objects.get(id=villa.driving_interventions_id)
                prev_form = InterDrivingWorkNOVat.objects.get(id=costs.excluding_vat_id)
                context['form'] = InterDrivingWorkNOVatForm(instance=prev_form)
                if request.method == 'POST':
                    form = InterDrivingWorkNOVatForm(request.POST, instance=prev_form)
                    try:
                        if form.is_valid():
                            costs.excluding_vat = form.save()
                            driving_calculation_villa(costs)
                            messages.success(request, 'Modifiche salvate con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Driving intervention does not  exist')

        elif type == 'trailed':
            if villa.trailed_interventions:
                costs = TrailingInterventions.objects.get(id=villa.trailed_interventions_id)
                prev_form = InterTrailedWorkNOVat.objects.get(id=costs.excluding_vat_id)
                context['form'] = InterTrailedWorkNOVatForm(instance=prev_form)
                if request.method == 'POST':
                    form = InterTrailedWorkNOVatForm(request.POST, instance=prev_form)
                    try:
                        if form.is_valid():
                            costs.excluding_vat = form.save()
                            trailed_calculation_villa(costs)
                            messages.success(request, 'Modifiche salvate con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Trailed intervention does not exist')

    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        if type == 'overall':
            if condo.overall_interventions:
                costs = OverallInterventions.objects.get(id=condo.overall_interventions_id)
                prev_form = OverallInterCostsNOVat.objects.get(id=costs.excluding_vat_id)
                context['form'] = OverallInterCostsNOVatForm(instance=prev_form)
                if request.method == 'POST':
                    form = OverallInterCostsNOVatForm(request.POST, instance=prev_form)
                    try:
                        if form.is_valid():
                            costs.excluding_vat = form.save()
                            overall_calculation_villa(costs)
                            messages.success(request, 'Modifiche salvate con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Overall intervention doesnt  exist')

        elif type == 'common':
            if condo.common_interventions:
                costs = CommonInterventions.objects.get(id=condo.common_interventions_id)
                prev_form = CommonWorkNOVat.objects.get(id=costs.excluding_vat_id)
                context['form'] = CommonWorkNOVatForm(instance=prev_form)
                if request.method == 'POST':
                    form = CommonWorkNOVatForm(request.POST, instance=prev_form)
                    try:
                        if form.is_valid():
                            costs.excluding_vat = form.save()
                            common_calculation_condo(costs)
                            messages.success(request, 'Modifiche salvate con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Common intervention does not  exist')

        elif type == 'subjective':
            if condo.subjective_interventions:
                costs = SubjectiveInterventions.objects.get(id=condo.subjective_interventions_id)
                prev_form = SubjectiveWorkNOVat.objects.get(id=costs.excluding_vat_id)
                context['form'] = SubjectiveWorkNOVatForm(instance=prev_form)
                if request.method == 'POST':
                    form = SubjectiveWorkNOVatForm(request.POST, instance=prev_form)
                    try:
                        if form.is_valid():
                            costs.excluding_vat = form.save()
                            subjective_calculation_condo(costs)
                            messages.success(request, 'Modifiche salvate con successo')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Subjective intervention does not exist')

    bonus.save()
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def preview(request, id):
    print(settings.BASE_DIR,settings.CORE_DIR)
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-preview', 'id': id }
    if bonus.bonus_villa:
        villa = get_object_or_404(BonusVilla, pk=bonus.bonus_villa_id)
        context['form'] = BonusVillaForm(instance=villa)
        context['bonus'] = villa
        context['type'] = 'villa'
        if request.POST:
            form = BonusVillaForm(request.POST, instance=villa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('bonus-preview', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    elif bonus.bonus_condo:
        condo = get_object_or_404(BonusCondo, pk=bonus.bonus_condo_id)
        context['form'] = BonusCondoForm(instance=condo)
        context['bonus'] = condo
        context['type'] = 'condo'
        if request.POST:
            form = BonusCondoForm(request.POST, instance=condo)
            if form.is_valid():
                form.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('bonus-preview', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)
    html_template = loader.get_template('bonus-preview.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def professionals(request, id):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-professional', 'id': id}
    if bonus.bonus_villa:
        villa = get_object_or_404(BonusVilla, pk=bonus.bonus_villa_id)
        if villa.professionals is None:
            context['form_inv'] = ProfTableIndividualForm()
            context['form_leg'] = ProfTableLegalForm()
        else:
            prof = Prof_table.objects.get(id=villa.professionals_id)
            context['form_inv'] = ProfTableIndividualForm(instance=prof)
            context['form_leg'] = ProfTableLegalForm(instance=prof)

        if request.POST:
            form = ProfTableForm(request.POST)
            if form.is_valid():
                villa.professionals = form.save()
                villa.save()
                print(villa.professionals_id)
                messages.success(request, 'Creato con successo')
                return redirect('bonus-professional', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    elif bonus.bonus_condo:
        condo = get_object_or_404(BonusCondo, pk=bonus.bonus_condo_id)
        if condo.professionals is None:
            context['form_inv'] = ProfTableIndividualForm()
            context['form_leg'] = ProfTableLegalForm()
        else:
            prof = Prof_table.objects.get(id=condo.professionals_id)
            context['form_inv'] = ProfTableIndividualForm(instance=prof)
            context['form_leg'] = ProfTableLegalForm(instance=prof)

        if request.POST:
            form = ProfTableForm(request.POST)
            if form.is_valid():
                condo.professionals = form.save()
                condo.save()
                messages.success(request, 'Creato con successo')
                return redirect('bonus-professional', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    html_template = loader.get_template('bonus-professionals.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def administrator(request, id):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-administrator', 'id': id}
    condo = get_object_or_404(BonusCondo, pk=bonus.bonus_condo_id)
    if condo.admin_legal is None and condo.admin_individual is None:
        context['form_inv'] = AdministrationIndividualForm()
        context['form_leg'] = AdministrationLegalForm()
    elif condo.admin_legal:
        prev = AdministrationLegal.objects.get(id=condo.admin_legal_id)
        context['form_inv'] = ''
        context['form_leg'] = AdministrationLegalForm(instance=prev)
    elif condo.admin_individual:
        prev = AdministrationIndividual.objects.get(id=condo.admin_individual_id)
        context['form_inv'] = AdministrationIndividualForm(instance=prev)
        context['form_leg'] = ''

    if 'legal' in request.POST:
        form = AdministrationLegalForm(request.POST)
        if form.is_valid():
            condo.admin_legal = form.save()
            condo.save()
            messages.success(request, 'Creato con successo')
            return redirect('bonus-preview', id=id)
        else:
            context['form_leg'] = form
            messages.error(request, form.errors)

    elif 'individual' in request.POST:
        form = AdministrationIndividualForm(request.POST)
        if form.is_valid():
            condo.admin_individual = form.save()
            condo.save()
            messages.success(request, 'Creato con successo')
            return redirect('bonus-preview', id=id)
        else:
            context['form_inv'] = form
            messages.error(request, form.errors)

    html_template = loader.get_template('bonus-administrator.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_professionals(request, id, type, prof):
    if type == 'individual':
        form = get_form_class_individual(prof)
        print(form)
    elif type == 'legal':
        form = get_form_class_legal(prof)
    context = {'segment': 'bonus-add-professional', 'id': id, 'form': form}
    if request.POST:
        form = form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Creato con successo')
            return redirect('bonus-professional', id=id)
        else:
            context['form'] = form
            messages.error(request, form.errors)

    html_template = loader.get_template('bonus-add-professionals.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def delete_prop(request, type, id):
    bonus = get_object_or_404(SuperBonus, pk=id)
    if type == 'condo':
        row = get_object_or_404(BonusCondo, pk=bonus.bonus_condo_id)
        row.delete()
        messages.success(request, 'Eliminato con successo Deleted')

    elif type == 'villa':
        row = get_object_or_404(BonusVilla, pk=bonus.bonus_villa_id)
        print(row)
        row.delete()
        messages.success(request, 'Eliminato con successo Deleted')

    return redirect(reverse('bonus-app-view'))


@login_required(login_url="/login/")
def bank_requirements(request, id):
    context = {'segment': 'bank-requirements', 'id': id,'status_form': StatusFileForm()}
    bonus = get_object_or_404(SuperBonus, pk=id)

    if BankRequirements.objects.filter(bonus=bonus.id).exists():
        bank_req = BankRequirements.objects.get(bonus=bonus.id)
    else:
        bank_req = BankRequirements(bonus=SuperBonus.objects.get(id=id))
        bank_req.save()

    context['bank_req'] = bank_req
    context['file_form'] = FileRequiredForm()
    if request.POST:
        post_list = list(request.POST.items())
        print(post_list)
        value = post_list[3][0]
        s = post_list[2][1]
        form = FileRequiredForm(request.POST, request.FILES)
        status = StatusFileForm(request.POST)
        if form.is_valid():
            f = form.save()
            print(f.id)
            # setattr(bank_req, value, f)
            getattr(bank_req, value).add(f)

            if status.is_valid():
                print('valid status')
                print(f.id)
                s = StatusFile(file_id=f.id, status=s)
                s.save()
            bank_req.save()
            messages.success(request, 'Form saved')
        else:
            messages.error(request, form.errors)

    html_template = loader.get_template('bank-requirements.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def edit_bank_file(request, id, file_id):
    file = get_object_or_404(FileRequired, id=file_id)
    file_form = FileRequiredForm(instance=file)
    context = {'file_form': file_form, 'id':id }
    if request.POST:
        ff = FileRequiredForm(request.POST, instance=file)
        if ff.is_valid():
            ff.save()
            messages.success(request, 'File Edited')
            return redirect('bank-requirements', id=id)
        else:
            messages.error(request, ff.errors)

    html_template = loader.get_template('bank-requirements-edit.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def edit_bank_file_status(request, id, file_id):
    status = get_object_or_404(StatusFile, file=file_id)
    status_form = StatusFileForm(instance=status)
    context = {'status_form': status_form, 'id':id}
    if request.POST:
        sf = StatusFileForm(request.POST, instance=status)
        if sf.is_valid():
            sf.save()
            messages.success(request, 'Status Edited')
            return redirect('bank-requirements', id=id)
        else:
            messages.error(request, sf.errors)

    html_template = loader.get_template('bank-requirements-edit.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def download_bank_file(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@login_required(login_url="/login/")
def delete_bank_file(request, id, file_id):
    file = FileRequired.objects.get(id=file_id)
    status = StatusFile.objects.get(file=file.id)
    file.delete()
    status.delete()
    messages.success(request, 'Eliminato con successo Deleted')
    return redirect('bank-requirements', id=id)





# @login_required(login_url="/login/")
# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             messages.success(request, 'Upload Successfully')
#         else:
#             messages.error(request, 'Failed Upload')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form, 'images': BonusVillaFiles.objects.all()})

# class FileFieldFormView(FormView):
#     form_class = FileFieldForm
#     template_name = 'upload.html'
#     success_url = '/superbonus/'
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 handle_uploaded_file(f)
#             messages.success(request, 'Uploaded')
#             return self.form_valid(form)
#         else:
#             messages.error(request, 'Didnt Upload')
#             return self.form_invalid(form)
#
#
# def handle_uploaded_file(f):
#     with open(f'core/staticfiles/${f.name}', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)