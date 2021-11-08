from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from .models import BeneficiaryForm, Beneficiary
from apps.app.models import FormFaccata



@login_required(login_url="/login/")
def beneficiary(request, fff):
    form = BeneficiaryForm(initial={'select_form': fff})
    context = {'form': form, 'segment': 'beneficiary', 'fff': fff}
    if request.POST:
        form = BeneficiaryForm(request.POST)
        print(form.is_valid())
        try:
            if form.is_valid():
                f = form.save()
                print(f.id)
                prev_form = Beneficiary.objects.get(pk=f.id)
                saved_form = BeneficiaryForm(instance=prev_form)
                context['form'] = saved_form
                context['form_id'] = f.id
                html_template = loader.get_template('beneficiary.html')
                return HttpResponse(html_template.render(context, request))

        except ValidationError as e:
            context['error'] = e
            html_template = loader.get_template('beneficiary.html')
            return HttpResponse(html_template.render(context, request))
    html_template = loader.get_template('beneficiary.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def beneficiary_add(request, id):
    prev_form = Beneficiary.objects.get(pk=id)

    context = {'segment': 'beneficiaryadd', 'form': BeneficiaryForm(instance=prev_form)}

    if request.POST:
        form = BeneficiaryForm(request.POST)
        try:
            if form.is_valid():
                f = form.save()
                prev_form = Beneficiary.objects.get(pk=f.id)
                saved_form = BeneficiaryForm(instance=prev_form)
                context['form'] = saved_form
                context['form_id'] = f.id
                html_template = loader.get_template('beneficiary.html')
                return HttpResponse(html_template.render(context, request))

        except ValidationError as e:
            context['error'] = e
            html_template = loader.get_template('beneficiary.html')
            return HttpResponse(html_template.render(context, request))

    html_template = loader.get_template('beneficiary.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def beneficiary_edit(request, id):
    prev_form = Beneficiary.objects.get(pk=id)
    context = {'segment': 'beneficiary_edit', 'form': BeneficiaryForm(instance=prev_form)}

    if request.POST:
        form = BeneficiaryForm(request.POST, instance=prev_form)
        try:
            if form.is_valid():
                f = form.save()
                context['form_id'] = f.id
                html_template = loader.get_template('beneficiary.html')
                return HttpResponse(html_template.render(context, request))

        except ValidationError as e:
            context['error'] = e
            html_template = loader.get_template('beneficiary.html')
            return HttpResponse(html_template.render(context, request))

    html_template = loader.get_template('beneficiary.html')
    return HttpResponse(html_template.render(context, request))
