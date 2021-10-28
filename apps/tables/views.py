from django.shortcuts import render
from django.core.exceptions import ValidationError
from .tables import overall_calculation
# Create your views here.
from .models import TableContract, OverallExVatForm, OverallTaxable, OverallExVat
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def tables(request):
    context = {'segment': 'table'}
    form_ex_vat = OverallExVatForm()
    form_taxable = OverallTaxable()
    context['form_ex_vat'] = form_ex_vat
    if request.method == 'POST':
        form_ex_vat = OverallExVatForm(request.POST)
        if form_ex_vat.is_valid():
            table_cont = TableContract()
            fnovat = form_ex_vat.save()
            fexvat = OverallExVat.objects.get(id=fnovat.id)
            table_cont.overall_ex_vat = fexvat
            try:
                table_cont, form_report, form_taxable, form_inc_vat = overall_calculation(fnovat, table_cont)
            except ValidationError as e:
                context['error'] = e
                html_template = loader.get_template('tables.html')
                return HttpResponse(html_template.render(context, request))

            context['form_ex_vat'] = fnovat
            context['form_taxable'] = form_taxable
            context['form_report'] = form_report
            context['table_cont'] = table_cont
            context['form_inc_vat'] = form_inc_vat
            html_template = loader.get_template('tables.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors

    html_template = loader.get_template('tables.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def common(request):
    pass
    # context = {'segment': 'common'}
    # form_ex_vat = CommonExVatForm()
    # form_taxable = CommonWorkTaxable()
    # form_report = CommonWorkReport()
    # form_inc_vat = CommonWorkIncVat()
    # context['form_ex_vat'] = form_ex_vat
    #
    # if request.method == 'POST':
    #     form_ex_vat = OverallExVatForm(request.POST)
    #     if form_ex_vat.is_valid():
    #         fnovat = form_ex_vat.save()
    #         error = overall_calculation(fnovat)
    #         context['form_ex_vat'] = fnovat
    #         context['form_taxable'] = form_taxable
    #         context['error'] = error
    #         html_template = loader.get_template('tables.html')
    #         return HttpResponse(html_template.render(context, request))
    #
    #     else:
    #         print(form_ex_vat.errors)
    #         context['error'] = form_ex_vat.errors
    #
    # html_template = loader.get_template('tables.html')
    # return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def subjective(request):
    pass
    # context = {'segment': 'subjective'}
    # form_ex_vat = SubjectiveExVatForm()
    # form_taxable = SubjectiveWorkTaxable()
    # form_report = OverallReport()
    # form_inc_vat = OverallIncVat()
    # context['form_ex_vat'] = form_ex_vat
    #
    # if request.method == 'POST':
    #     form_ex_vat = OverallExVatForm(request.POST)
    #     if form_ex_vat.is_valid():
    #         fnovat = form_ex_vat.save()
    #         error = overall_calculation(fnovat)
    #         context['form_ex_vat'] = fnovat
    #         context['form_taxable'] = form_taxable
    #         context['error'] = error
    #         html_template = loader.get_template('tables.html')
    #         return HttpResponse(html_template.render(context, request))
    #
    #     else:
    #         print(form_ex_vat.errors)
    #         context['error'] = form_ex_vat.errors
    #
    # html_template = loader.get_template('tables.html')
    # return HttpResponse(html_template.render(context, request))