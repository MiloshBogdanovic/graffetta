from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from .models import *
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ValidationError


# Create your views here.


@login_required(login_url="/login/")
def app(request):
    context = {'segment': 'bonus-app-view', 'table': SuperBonus.objects.all()}
    html_template = loader.get_template('superbonus.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_condo(request):
    context = {'segment': 'bonus-app-view'}
    html_template = loader.get_template('add-condo.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_villa(request):
    context = {'segment': 'bonus-add-villa', 'form': BonusVillaForm()}
    if request.method == 'POST':
        form = BonusVillaForm(request.POST)
        if form.is_valid():
            super_bonus = SuperBonus(bonus_villa=form.save())
            super_bonus.save()
            messages.success(request, 'Successfully')
            return render(request, 'add-villa.html', context)
        else:
            messages.error(request, 'Error')
            return render(request, 'add-villa.html', context)
    html_template = loader.get_template('add-villa.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def interventions(request, id):
    context = {'segment': 'interventions'}
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
                    messages.error(request, 'Error in validation')
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
                    messages.error(request, 'Error in validation')

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
                    messages.error(request, 'Error in validation')
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
                    messages.error(request, 'Error in validation')

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def catastal(request, id):
    context = {'segment': 'catastal'}
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
                    messages.error(request, 'Error in validation')
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
                    messages.error(request, 'Error in validation')
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
                    messages.error(request, 'Error in validation')
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
                    messages.error(request, 'Error in validation')

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def beneficiary(request, id):
    context = {'segment': 'bonus-beneficiary'}
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
                    messages.error(request, 'Error in validation')
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
                        messages.error(request, 'Error in validation')
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
                    messages.error(request, 'Error in validation')

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
                        messages.error(request, 'Error in validation')
                except:
                    raise ValidationError(form.errors)

    return HttpResponse(html_template.render(context, request))

#Ovde sam stao!
@login_required(login_url="/login/")
def intervention_costs(request, id):
    context = {'segment': 'bonus-beneficiary'}
    html_template = loader.get_template('bonus-overall-inter.html')
    bonus = get_object_or_404(SuperBonus, pk=id)
    if bonus.bonus_villa:
        villa = BonusVilla.objects.get(id=bonus.bonus_villa_id)
        if villa.interventions:
            intervention = Beneficiary.objects.get(id=villa.beneficiary_id)
            context['form'] = BeneficiaryForm(instance=beneficiary)
            if request.method == 'POST':
                form = BeneficiaryForm(request.POST, instance=beneficiary)
                if form.is_valid():
                    villa.beneficiary = form.save()
                    villa.save()
                    messages.success(request, 'Successfully Changed Values')
                    return redirect('bonus-preview', id=id)
                else:
                    messages.error(request, 'Error in validation')
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
                        messages.error(request, 'Error in validation')
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
                    messages.error(request, 'Error in validation')

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
                        messages.error(request, 'Error in validation')
                except:
                    raise ValidationError(form.errors)

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def preview(request, id):
    bonus = get_object_or_404(SuperBonus, pk=id)
    context = {'segment': 'bonus-preview', 'id': id}
    if bonus.bonus_villa:
        villa = get_object_or_404(BonusVilla, pk=bonus.bonus_villa_id)
        context['form'] = BonusVillaForm(instance=villa)
        context['bonus'] = villa
        if request.POST:
            form = BonusVillaForm(request.POST, instance=villa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully')
                return redirect('bonus-preview', id=id)
            else:
                messages.error(request, 'Invalid Entry')
                return render(request, 'bonus-preview.html', context)

    elif bonus.bonus_condo:
        condo = get_object_or_404(BonusCondo, pk=bonus.bonus_condo_id)
        context['form'] = BonusVillaForm(instance=condo)
        context['bonus'] = condo
    html_template = loader.get_template('bonus-preview.html')
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
