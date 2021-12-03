from django.shortcuts import render
from django.core.exceptions import ValidationError
from .tables import overall_calculation, common_calculation, subjective_calculation
# Create your views here.
from .models import TableContract, OverallExVatForm, OverallExVat, CommonExVatForm, SubjectiveExVatForm, OverallReport, \
    CommonWorkReport, SubjectiveWorkReport, CommonWorkExVat, SubjectiveWorkExVat
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from apps.app.models import FormFaccata


@login_required(login_url="/login/")
def tables(request, fff):
    fff = get_object_or_404(FormFaccata, id=fff)
    context = {'segment': 'table', 'form_ex_vat': OverallExVatForm(),'fff': fff.id, 'fform': fff}
    if fff.tables_id is None:
        table_cont = TableContract()
        table_cont.save()
        tc_id = table_cont.id
        form_ex_vat = OverallExVatForm()
        context = {'segment': 'table', 'form_ex_vat': form_ex_vat, 'table_cont': tc_id, 'fff': fff.id}
        fff.tables = TableContract.objects.get(id=table_cont.id)
        fff.save()

    elif fff.tables_id and fff.tables.overall_rep_id:
        table_cont = get_object_or_404(TableContract, id=fff.tables_id)
        context = {'segment': 'table', 'report': OverallReport.objects.get(id=table_cont.overall_rep_id),
                   'table_cont': table_cont.id, 'fff': fff.id, 'edit_id': table_cont.overall_ex_vat_id}
        html_template = loader.get_template('tables.html')
        return HttpResponse(html_template.render(context, request))

    if request.method == 'POST':
        form_ex_vat = OverallExVatForm(request.POST)
        table_cont = get_object_or_404(TableContract, id=fff.tables_id)
        if form_ex_vat.is_valid():
            fnovat = form_ex_vat.save()
            fnovat.save()
            table_cont.overall_ex_vat = OverallExVat.objects.get(id=fnovat.id)
            try:
                table_cont, form_report, form_taxable, form_inc_vat = overall_calculation(fnovat, table_cont)
            except ValidationError as e:
                context['error'] = e
                html_template = loader.get_template('tables.html')
                return HttpResponse(html_template.render(context, request))

            context['edit_id'] = fnovat.id
            context['table_cont'] = table_cont.id
            html_template = loader.get_template('tables.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors
            context['form_ex_vat'] = form_ex_vat
    else:
        html_template = loader.get_template('tables.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def overall_edit(request, id):
    overall_nv = get_object_or_404(OverallExVat, pk=id)
    form = OverallExVatForm(instance=overall_nv)
    context = {'segment': 'tables-edit', 'form_ex_vat': form}
    if request.POST:
        try:
            form = OverallExVatForm(request.POST, instance=overall_nv)
            if form.is_valid():
                fnovat=form.save()
                fnovat.save()
                table_cont = get_object_or_404(TableContract, overall_ex_vat=overall_nv.id)
                table_cont, form_report, form_taxable, form_inc_vat = overall_calculation(fnovat, table_cont)
                context['message'] = 'Modifiche effettuate con successo'
                html_template = loader.get_template('tables-edit.html')
                return HttpResponse(html_template.render(context, request))

        except ValidationError as e:
            context['error'] = e
            context['form_ex_vat'] = form
            html_template = loader.get_template('tables-edit.html')
            return HttpResponse(html_template.render(context, request))

    html_template = loader.get_template('tables-edit.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def common(request, tc_id):
    fff = FormFaccata.objects.get(tables=tc_id)
    context = {'segment': 'table', 'form_ex_vat': CommonExVatForm(), 'table_cont': tc_id, 'fff': fff.id}
    table_cont = get_object_or_404(TableContract, id=tc_id)
    if table_cont.common_rep:
        context = {'segment': 'common', 'report': CommonWorkReport.objects.get(id=table_cont.common_rep_id),
                   'table_cont': table_cont.id, 'fff': fff.id, 'edit_id': table_cont.common_ex_vat_id}
        html_template = loader.get_template('tables-common.html')
        return HttpResponse(html_template.render(context, request))
    if request.method == 'POST':
        form_ex_vat = CommonExVatForm(request.POST)
        if form_ex_vat.is_valid():
            fnovat = form_ex_vat.save()
            fnovat.save()
            table_cont.common_ex_vat = CommonWorkExVat.objects.get(id=fnovat.id)
            try:
                table_cont, form_report, form_taxable, form_inc_vat = common_calculation(fnovat, table_cont)
            except ValidationError as e:
                context['error'] = e
                html_template = loader.get_template('tables-common.html')
                return HttpResponse(html_template.render(context, request))

            context['edit_id'] = fnovat.id
            context['table_cont'] = table_cont.id
            html_template = loader.get_template('tables-common.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors
            context['form_ex_vat'] = form_ex_vat

    html_template = loader.get_template('tables-common.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def common_edit(request, id):
    common_nv = get_object_or_404(CommonWorkExVat, pk=id)
    form = CommonExVatForm(instance=common_nv)
    context = {'segment': 'common-edit', 'form_ex_vat': form}
    if request.POST:
        try:
            form = CommonExVatForm(request.POST, instance=common_nv)
            if form.is_valid():
                fnovat = form.save()
                fnovat.save()
                table_cont = get_object_or_404(TableContract, common_ex_vat=common_nv.id)
                table_cont, form_report, form_taxable, form_inc_vat = common_calculation(fnovat, table_cont)
                context['message'] = 'Modifiche effettuate con successo'
                html_template = loader.get_template('edit-common.html')
                return HttpResponse(html_template.render(context, request))

        except ValidationError as e:
            context['error'] = e
            context['form_ex_vat'] = form
            html_template = loader.get_template('edit-common.html')
            return HttpResponse(html_template.render(context, request))

    html_template = loader.get_template('edit-common.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def subjective(request, tc_id):
    fff = FormFaccata.objects.get(tables=tc_id)
    table_cont = get_object_or_404(TableContract, id=tc_id)
    context = {'segment': 'subjective', 'form_ex_vat': SubjectiveExVatForm(), 'table_cont': tc_id, 'fff': fff.id}
    if table_cont.subjective_rep:
        context = {'segment': 'common', 'report': SubjectiveWorkReport.objects.get(id=table_cont.subjective_rep_id),
                   'table_cont': table_cont.id, 'fff': fff.id, 'edit_id': table_cont.subjective_ex_vat_id}
        html_template = loader.get_template('tables-subjective.html')
        return HttpResponse(html_template.render(context, request))

    if request.method == 'POST':
        form_ex_vat = SubjectiveExVatForm(request.POST)
        if form_ex_vat.is_valid():
            fnovat = form_ex_vat.save()
            fnovat.save()
            table_cont.subjective_ex_vat = SubjectiveWorkExVat.objects.get(id=fnovat.id)
            try:
                table_cont, form_report, form_taxable, form_inc_vat = subjective_calculation(fnovat, table_cont)
            except ValidationError as e:
                context['error'] = e
                html_template = loader.get_template('tables-subjective.html')
                return HttpResponse(html_template.render(context, request))

            context['edit_id'] = fnovat.id
            context['table_cont'] = table_cont.id
            html_template = loader.get_template('tables-subjective.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors
            context['form_ex_vat'] = form_ex_vat

    html_template = loader.get_template('tables-subjective.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def sub_edit(request, id):
    sub_nv = get_object_or_404(SubjectiveWorkExVat, pk=id)
    form = SubjectiveExVatForm(instance=sub_nv)
    context = {'segment': 'sub-edit', 'form_ex_vat': form}
    if request.POST:
        try:
            form = SubjectiveExVatForm(request.POST, instance=sub_nv)
            if form.is_valid():
                fnovat=form.save()
                fnovat.save()
                table_cont = get_object_or_404(TableContract, subjective_ex_vat=sub_nv.id)
                table_cont, form_report, form_taxable, form_inc_vat = subjective_calculation(fnovat, table_cont)
                context['message'] = 'Modifiche effettuate con successo'
                html_template = loader.get_template('sub-edit.html')
                return HttpResponse(html_template.render(context, request))

        except ValidationError as e:
            context['error'] = e
            context['form_ex_vat'] = form
            html_template = loader.get_template('sub-edit.html')
            return HttpResponse(html_template.render(context, request))

    html_template = loader.get_template('sub-edit.html')
    return HttpResponse(html_template.render(context, request))