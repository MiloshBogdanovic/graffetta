# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.app.models import CondominiumForm, AdministrationIndividualForm, AdministrationLegalForm


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        print(load_template)
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        if load_template == 'bonus_faccata.html':
            html_template = loader.get_template('bonus_faccata.html')
            context['forms'] = CondominiumForm()
            if request.POST:
                form = CondominiumForm(request.POST)
                if form.is_valid():
                    f = form.save()
                    print(f.id, f.select_administrator)
                    if f.select_administrator == 'Legal':
                        context['form_id'] = f.id
                        context['forms'] = AdministrationLegalForm()
                        html_template = loader.get_template('bonus_faccata_legal.html')
                        return HttpResponse(html_template.render(context, request))

                    elif f.select_administrator == 'Individual':
                        context['form_id'] = f.id
                        context['forms'] = AdministrationIndividualForm()
                        html_template = loader.get_template('bonus_faccata_individual.html')
                        return HttpResponse(html_template.render(context, request))

                else:
                    print(form.errors)
                    context['errors'] = form.errors
                    return HttpResponse(html_template.render(context, request))

            return HttpResponse(html_template.render(context, request))

        if load_template == 'bonus_faccata_legal.html':
            html_template = loader.get_template('bonus_faccata_legal.html')
            if request.POST:
                form = AdministrationLegalForm(request.POST)
                if form.is_valid():
                    pass

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
