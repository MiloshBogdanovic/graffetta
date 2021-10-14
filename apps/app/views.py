# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from apps.app.models import CondominiumForm, AdministrationIndividualForm, AdministrationLegalForm,\
    FormFaccata, CatastalDataForm
from django.shortcuts import get_object_or_404, render


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def bonus(request):
    context = {'segment': 'bonus'}
    forms = CondominiumForm()
    context['forms'] = forms
    if request.method == 'POST':
        form = CondominiumForm(request.POST)
        fform = FormFaccata()
        if form.is_valid():
            f = form.save()
            fform.condominium_id = f.id
            fform.user_id = request.user.id
            fform.save()
            if f.select_administrator == 'Legal':
                return redirect('legal', form=fform.id)
            elif f.select_administrator == 'Individual':
                return redirect('individual', form=fform.id)

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata.html', context)

    html_template = loader.get_template('bonus_faccata.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def legal(request, form):
    context = {'segment': 'legal'}
    fform = get_object_or_404(FormFaccata, pk=form)
    forms = AdministrationLegalForm()
    context['forms'] = forms
    if request.method == 'POST':
        form = AdministrationLegalForm(request.POST)
        if form.is_valid():
            f = form.save()
            fform.admin_legal_id = f.id
            fform.admin_individual_id = 0
            fform.save()
            return redirect('catastal', form=fform.id)

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata_legal.html', context)

    return render(request, 'bonus_faccata_legal.html', context)


@login_required(login_url="/login/")
def individual(request, form):
    context = {'segment': 'individual'}
    fform = get_object_or_404(FormFaccata, pk=form)
    forms = AdministrationIndividualForm()
    context['forms'] = forms
    if request.method == 'POST':
        form = AdministrationIndividualForm(request.POST)
        if form.is_valid():
            f = form.save()
            fform.admin_legal_id = 0
            fform.admin_individual_id = f.id
            fform.save()
            return redirect('catastal', form=fform.id)

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata_individual.html', context)

    return render(request, 'bonus_faccata_individual.html', context)

@login_required(login_url="/login/")
def catastal(request, form):
    context = {'segment': 'catastal'}
    fform = get_object_or_404(FormFaccata, pk=form)
    forms = CatastalDataForm()
    context['forms'] = forms
    if request.method == 'POST':
        form = CatastalDataForm(request.POST)
        if form.is_valid():
            f = form.save()
            fform.catastal_id = f.id
            fform.save()
            return redirect(reverse('home'))

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata_catastal.html', context)

    return render(request, 'bonus_faccata_catastal.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template


        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
