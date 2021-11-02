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
from apps.tables.models import TableContract
from apps.app.models import CondominiumData, CondominiumForm, AdministrationIndividualForm, AdministrationLegalForm,\
    FormFaccata, CatastalDataForm, AdministrationIndividual, AdministrationLegal, CatastalData, DataInitial
from django.shortcuts import get_object_or_404, render
from itertools import chain


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    context['fff'] = FormFaccata.objects.all()
    context['dform'] = DataInitial.objects.all()
    context['tform'] = TableContract.objects.all()
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def condt(request, id):
    context = {'segment': 'index'}
    fform = FormFaccata.objects.all()
    context['fform'] = fform
    cform = CondominiumData.objects.filter(id=id)
    context['cform'] = cform
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def individt(request, id):
    context = {'segment': 'index'}
    fform = FormFaccata.objects.all()
    context['fform'] = fform
    iform = AdministrationIndividual.objects.filter(id=id)
    context['iform'] = iform
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def flegalt(request, id):
    context = {'segment': 'index'}
    fform = FormFaccata.objects.all()
    context['fform'] = fform
    flform = AdministrationLegal.objects.filter(id=id)
    context['flform'] = flform
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def catastt(request, id):
    context = {'segment': 'index'}
    fform = FormFaccata.objects.all()
    context['fform'] = fform
    ctform = CatastalData.objects.filter(id=id)
    context['ctform'] = ctform
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def bonus(request):
    fff = FormFaccata()
    forms = CondominiumForm()
    context = {'segment': 'bonus', 'forms': forms}
    if request.method == 'POST':
        form = CondominiumForm(request.POST)
        dform = DataInitial()
        if form.is_valid():
            f = form.save()
            dform.condominium_id = f.id
            dform.save()
            fff.datainit_id = dform.id
            fff.user_id = request.user.id
            fff.save()
            context['fff']= fff.id
            if f.select_administrator == 'Legal':
                return redirect('legal', form=dform.id)
            elif f.select_administrator == 'Individual':
                return redirect('individual', form=dform.id)

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata.html', context)

    html_template = loader.get_template('bonus_faccata.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def legal(request, form):
    context = {'segment': 'legal'}
    dform = get_object_or_404(DataInitial, pk=form)
    fff = get_object_or_404(FormFaccata, datainit=form)
    forms = AdministrationLegalForm()
    context['forms'] = forms
    if request.method == 'POST':
        form = AdministrationLegalForm(request.POST)
        if form.is_valid():
            f = form.save()
            dform.admin_legal_id = f.id
            dform.save()
            fff.save()
            context['fff'] = fff.id
            return redirect('catastal', form=dform.id)

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata_legal.html', context)

    return render(request, 'bonus_faccata_legal.html', context)


@login_required(login_url="/login/")
def individual(request, form):
    context = {'segment': 'individual'}
    dform = get_object_or_404(DataInitial, pk=form)
    fff = get_object_or_404(FormFaccata, datainit=form)
    forms = AdministrationIndividualForm()
    context['forms'] = forms
    if request.method == 'POST':
        form = AdministrationIndividualForm(request.POST)
        if form.is_valid():
            f = form.save()
            dform.admin_individual_id = f.id
            dform.save()
            fff.save()
            context['fff'] = fff.id
            return redirect('catastal', form=dform.id)

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata_individual.html', context)

    return render(request, 'bonus_faccata_individual.html', context)


@login_required(login_url="/login/")
def catastal(request, form):
    context = {'segment': 'catastal'}
    dform = get_object_or_404(DataInitial, pk=form)
    forms = CatastalDataForm()
    fff = get_object_or_404(FormFaccata, datainit=form)
    context['forms'] = forms
    context['form'] = form
    if request.method == 'POST':
        form = CatastalDataForm(request.POST)
        if form.is_valid():
            f = form.save()
            dform.catastal_id = f.id
            dform.save()
            fff.save()
            context['fff'] = fff.id
            return redirect(reverse('tables', args=(fff.id,)))

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

@login_required(login_url="/login")
def search(request):
    context = {}
    load_template = 'search.html'
    html_template = loader.get_template(load_template)
    try:
        value = request.GET.get('q')
        print(request.user.id)
        print(value)
        user_forms = FormFaccata.objects.filter(user='{}'.format(request.user.id)).values_list('condominium_id', flat=True)
        print(list(user_forms))
        context['results'] = CondominiumData.objects.filter(name__icontains='{}'.format(value), pk__in=user_forms)
        print(list(context['results']))
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
    except:
        return HttpResponse(html_template.render(context, request))