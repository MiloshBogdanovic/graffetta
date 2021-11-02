from django.shortcuts import render
from django.core.exceptions import ValidationError
from .tables import overall_calculation, common_calculation, subjective_calculation
# Create your views here.
from .models import TableContract, OverallExVatForm, CommonExVatForm, SubjectiveExVatForm, OverallReport, \
    CommonWorkReport, SubjectiveWorkReport
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from apps.app.models import FormFaccata


@login_required(login_url="/login/")
def tables(request, fff):
    fff = get_object_or_404(FormFaccata, id=fff)
    context = {'segment': 'table', 'form_ex_vat': OverallExVatForm()}
    if fff.tables_id is None:
        table_cont = TableContract()
        table_cont.save()
        context = {'segment': 'table', 'form_ex_vat': OverallExVatForm(), 'table_cont': table_cont.id, 'fff': fff.id}
        fff.tables = TableContract.objects.get(id=table_cont.id)
        fff.save()

    elif fff.tables_id and fff.tables.overall_rep_id:
        table_cont = get_object_or_404(TableContract, id=fff.tables_id)
        context = {'segment': 'table', 'report': OverallReport.objects.get(id=table_cont.overall_rep_id),
                   'table_cont': table_cont.id, 'fff': fff.id}
        html_template = loader.get_template('tables.html')
        return HttpResponse(html_template.render(context, request))

    if request.method == 'POST':
        form_ex_vat = OverallExVatForm(request.POST)
        table_cont = get_object_or_404(TableContract, id=fff.tables_id)
        if form_ex_vat.is_valid():
            fnovat = form_ex_vat.save()
            try:
                table_cont, form_report, form_taxable, form_inc_vat = overall_calculation(fnovat, table_cont)
            except ValidationError as e:
                context['error'] = e
                html_template = loader.get_template('tables.html')
                return HttpResponse(html_template.render(context, request))

            context['form_ex_vat'] = form_ex_vat
            html_template = loader.get_template('tables.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors

    html_template = loader.get_template('tables.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def common(request, tc_id):
    fff = FormFaccata.objects.get(tables=tc_id)
    print(fff.id)
    context = {'segment': 'table', 'form_ex_vat': CommonExVatForm(), 'table_cont': tc_id, 'fff': fff.id}
    table_cont = get_object_or_404(TableContract, id=tc_id)
    if table_cont.common_rep:
        context = {'segment': 'common', 'report': CommonWorkReport.objects.get(id=table_cont.common_rep_id),
                   'table_cont': table_cont.id, 'fff': fff.id}
        html_template = loader.get_template('tables-common.html')
        return HttpResponse(html_template.render(context, request))
    if request.method == 'POST':
        form_ex_vat = CommonExVatForm(request.POST)
        if form_ex_vat.is_valid():

            fnovat = form_ex_vat.save()
            try:
                table_cont, form_report, form_taxable, form_inc_vat = common_calculation(fnovat, table_cont)
            except ValidationError as e:
                context['error'] = e
                html_template = loader.get_template('tables-common.html')
                return HttpResponse(html_template.render(context, request))
            context['form_ex_vat'] = form_ex_vat

            html_template = loader.get_template('tables-common.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors

    html_template = loader.get_template('tables-common.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def subjective(request, tc_id):
    fff = FormFaccata.objects.get(tables=tc_id)
    table_cont = get_object_or_404(TableContract, id=tc_id)
    context = {'segment': 'subjective', 'form_ex_vat': SubjectiveExVatForm(), 'table_cont': tc_id, 'fff': fff.id}
    if table_cont.subjective_rep:
        context = {'segment': 'common', 'report': SubjectiveWorkReport.objects.get(id=table_cont.subjective_rep_id),
                   'table_cont': table_cont.id, 'fff': fff.id}
        html_template = loader.get_template('tables-subjective.html')
        return HttpResponse(html_template.render(context, request))

    if request.method == 'POST':
        form_ex_vat = SubjectiveExVatForm(request.POST)
        if form_ex_vat.is_valid():
            fnovat = form_ex_vat.save()
            try:
                table_cont, form_report, form_taxable, form_inc_vat = subjective_calculation(fnovat, table_cont)
            except ValidationError as e:
                context['error'] = e
                html_template = loader.get_template('tables-subjective.html')
                return HttpResponse(html_template.render(context, request))

            context['form_ex_vat'] = form_ex_vat
            html_template = loader.get_template('tables-subjective.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors

    html_template = loader.get_template('tables-subjective.html')
    return HttpResponse(html_template.render(context, request))