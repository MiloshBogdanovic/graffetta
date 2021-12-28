from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from .models import *
from .calculations import overall_calculation_villa, trailed_calculation_villa, driving_calculation_villa
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ValidationError
from apps.professionals.models import *
from django.utils.translation import activate
from django.apps import apps
from django.forms import modelform_factory
# Create your views here.


@login_required(login_url="/login/")
def app(request):
    context = {'segment': 'bonus-app-view', 'table': SuperBonus.objects.all()}
    html_template = loader.get_template('superbonus.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_condo(request):
    context = {'segment': 'bonus-add-condo'}
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
            messages.success(request, 'Successfully')
            return redirect('bonus-preview', id=super_bonus.bonus_villa_id)
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
                    messages.success(request, 'Successfully Changed Values')
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
                    messages.success(request, 'Successfully Created Interventions')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)

    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        if condo.interventions:
            intervention = Interventions.objects.get(id=condo.interventions_id)
            context['form'] = InterventionsForm(instance=intervention)
            if request.method == 'POST':
                form = InterventionsForm(request.POST, instance=intervention)
                if form.is_valid():
                    condo.interventions = form.save()
                    condo.save()
                    messages.success(request, 'Successfully Changed Values')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)
        else:
            context['form'] = InterventionsForm()
            if request.method == 'POST':
                form = InterventionsForm(request.POST)
                if form.is_valid():
                    condo.interventions = form.save()
                    condo.save()
                    messages.success(request, 'Successfully Created Interventions')
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
                    messages.success(request, 'Successfully Changed Values')
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
                    messages.success(request, 'Successfully Created Interventions')
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
                    messages.success(request, 'Successfully Changed Values')
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
                    messages.success(request, 'Successfully Created Interventions')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def beneficiary(request, id):
    context = {'segment': 'bonus-beneficiary', 'id':id}
    html_template = loader.get_template('bonus-beneficiary.html')
    bonus = get_object_or_404(SuperBonus, pk=id)
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        if villa.beneficiary:
            beneficiary = Beneficiary.objects.get(id=villa.beneficiary_id)
            context['form'] = BeneficiaryForm(instance=beneficiary)
            if request.method == 'POST':
                form = BeneficiaryForm(request.POST, instance=beneficiary)
                if form.is_valid():
                    villa.beneficiary = form.save()
                    villa.save()
                    messages.success(request, 'Successfully Changed Values')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)
        else:
            context['form'] = BeneficiaryForm()
            if request.method == 'POST':
                form = BeneficiaryForm(request.POST)
                try:
                    if form.is_valid():
                        villa.beneficiary = form.save()
                        villa.save()
                        messages.success(request, 'Successfully Created Interventions')
                        return redirect('bonus-preview', id=id)
                    else:
                        context['form'] = form
                        messages.error(request, form.errors)
                except:
                    raise ValidationError(form.errors)

    elif bonus.bonus_condo:
        condo = BonusCondo.objects.get(id=bonus.bonus_condo_id)
        if condo.catastal:
            beneficiary = Beneficiary.objects.get(id=condo.beneficiary_id)
            context['form'] = BeneficiaryForm(instance=catastal)
            if request.method == 'POST':
                form = BeneficiaryForm(request.POST, instance=beneficiary)
                if form.is_valid():
                    condo.beneficiary = form.save()
                    condo.save()
                    messages.success(request, 'Successfully Changed Values')
                    return redirect('bonus-preview', id=id)
                else:
                    context['form'] = form
                    messages.error(request, form.errors)

        else:
            context['form'] = BeneficiaryForm()
            if request.method == 'POST':
                form = BeneficiaryForm(request.POST)
                try:
                    if form.is_valid():
                        condo.beneficiary = form.save()
                        condo.save()
                        messages.success(request, 'Successfully Created Interventions')
                        return redirect('bonus-preview', id=id)
                    else:
                        context['form'] = form
                        messages.error(request, form.errors)
                except:
                    raise ValidationError(form.errors)

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
                            messages.success(request, 'Successfully Created Interventions')
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
                            messages.success(request, 'Successfully Created Interventions')
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
                            messages.success(request, 'Successfully Created Interventions')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Trailed intervention already exist')

    elif bonus.bonus_condo:
        pass

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
                            messages.success(request, 'Successfully Edited Interventions')
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
                            messages.success(request, 'Successfully Edited Interventions')
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
                    form = InterTrailedWorkNOVatForm(request.POST,instance=prev_form)
                    try:
                        if form.is_valid():
                            costs.excluding_vat = form.save()
                            trailed_calculation_villa(costs)
                            messages.success(request, 'Successfully Edited Interventions')
                            return redirect('bonus-costs', id=bonus.id, type=type)
                        else:
                            context['form'] = form
                            messages.error(request, form.errors)
                    except:
                        raise ValidationError(form.errors)
            else:
                messages.warning(request, 'Trailed intervention does not exist')

    elif bonus.bonus_condo:
        pass

    bonus.save()
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def preview(request, id):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-preview', 'id': id}
    if bonus.bonus_villa:
        villa = get_object_or_404(BonusVilla, pk=bonus.bonus_villa_id)
        context['form'] = BonusVillaForm(instance=villa)
        context['bonus'] = villa
        context['type'] = 'villa'
        if request.POST:
            form = BonusVillaForm(request.POST, instance=villa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully')
                return redirect('bonus-preview', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    elif bonus.bonus_condo:
        condo = get_object_or_404(BonusCondo, pk=bonus.bonus_condo_id)
        context['form'] = BonusVillaForm(instance=condo)
        context['bonus'] = condo
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
                messages.success(request, 'Successfully')
                return redirect('bonus-professional', id=id)
            else:
                context['form'] = form
                messages.error(request, form.errors)

    elif bonus.bonus_condo:
        pass

    html_template = loader.get_template('bonus-professionals.html')
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
            messages.success(request, 'Successfully')
            return redirect('bonus-professional', id=id)
        else:
            context['form'] = form
            messages.error(request, form.errors)

    html_template = loader.get_template('bonus-add-professionals.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def delete_prop(request, type, id):
    if type == 'condo':
        row = BonusCondo.objects.get(id=id)
        row.delete()
        messages.success(request, 'Successfully Deleted')

    elif type == 'villa':
        row = get_object_or_404(BonusVilla, pk=id)
        print(row)
        row.delete()
        messages.success(request, 'Successfully Deleted')

    return redirect(reverse('bonus-app-view'))
