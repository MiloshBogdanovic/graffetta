# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.forms.forms import Form
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from apps.app.tables import AdministrationIndividualTable, AdministrationLegalTable, CatastalTable, CondominiumTable
from apps.tables.models import TableContract
from apps.professionals.models import Prof_table
from apps.beneficary.models import Beneficiary
from apps.app.models import CondominiumData, CondominiumForm, AdministrationIndividualForm, AdministrationLegalForm,\
    FormFaccata, CatastalDataForm, AdministrationIndividual, AdministrationLegal, CatastalData, DataInitial
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from mailmerge import MailMerge
import os 


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    context['fform'] = FormFaccata.objects.all()
    context['dform'] = DataInitial.objects.all()
    context['tform'] = TableContract.objects.all()
    context['beneficiary'] = Beneficiary.objects.all()
    context['ptform'] = Prof_table.objects.all()
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
            context['fff'] = fff.id
            if f.select_administrator == 'Legal':
                return redirect('legal', form=dform.id, fff=fff.id)
            elif f.select_administrator == 'Individual':
                return redirect('individual', form=dform.id)

        else:
            context['errors'] = form.errors
            return render(request, 'bonus_faccata.html', context)

    html_template = loader.get_template('bonus_faccata.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def legal(request, form, fff):
    context = {'segment': 'legal', 'fff': fff}
    dform = get_object_or_404(DataInitial, pk=form)
    fff = get_object_or_404(FormFaccata, pk=fff)
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
def individual(request, form, fff):
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
    context['dform'] = dform
    context['forms'] = forms
    context['form'] = form
    context['fff'] = fff.id
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

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def condo_list(request):
    table = CondominiumTable(CondominiumData.objects.all())
    print(table)
    return render(request, 'editable-tables.html', {
        'title': 'Condominiums',
        'table': table
    })

@login_required(login_url="/login/")
def catastal_list(request):
    table = CatastalTable(CatastalData.objects.all())
    return render(request, 'editable-tables.html', {
        'title': 'Catastals',
        'table': table
    })

@login_required(login_url="/login/")
def admin_legal_list(request):
    table = AdministrationLegalTable(AdministrationLegal.objects.all())
    return render(request, 'editable-tables.html', {
        'title': 'Administrators Legal',
        'table': table
    })

@login_required(login_url="/login/")
def admin_individual_list(request):
    table = AdministrationIndividualTable(AdministrationLegal.objects.all())
    return render(request, 'editable-tables.html', {
        'title': 'Individual Administrators',
        'table': table
    })


@login_required(login_url="/login/")
def edit_form(request, table, id):
    context = {'segment': 'edit-form'}
    html_template = loader.get_template('edit-form.html')
    row = None
    form = None
    form_type = None 
    try: 
        if table == 'Condominium':
            form_type = CondominiumForm
            row = CondominiumData.objects.get(pk=id)
            form = CondominiumForm(instance=row)
        elif table == 'AdministrationIndividual':
            form_type = AdministrationIndividualForm
            row = AdministrationIndividual.objects.get(pk=id)
            form = AdministrationIndividualForm(instance=row)
        elif table == 'AdministrationLegal':
            form_type = AdministrationLegalForm
            row = AdministrationLegal.objects.get(pk=id)
            form = AdministrationLegalForm(instance=row)
        elif table == 'CatastalData':
            form_type = CatastalDataForm
            row = CatastalData.objects.get(pk=id)
            form = CatastalDataForm(instance=row)
        
        
        context['form'] = form
        
        if request.POST:
            form=form_type(request.POST, instance=row)
            if form.is_valid():
                form.save()
                messages.success(request, 'Modifiche salvate con successo')
                return redirect('home')
            else:
                messages.success(request, form.errors)
                return redirect('edit-form', table=table, id=id)
        
        print('context')
        print(context)

        return HttpResponse(html_template.render(context, request))
    except ValueError as e:
        context['error'] = e
        return HttpResponse(html_template.render(context, request))
    except Exception as e:
        context['error'] = e
        return HttpResponse(html_template.render(context, request))
    
    
@login_required(login_url="/login/")
def save_table_data(request):
    if(request.method =='POST'):
        try:
            id=request.POST.get('id','')
            type=request.POST.get('type', '')
            value=request.POST.get('value', '')
            table=request.POST.get('table', '') 
            write_to = None
            
            if(table == 'condo'):
                write_to = CondominiumData.objects.get(pk=id)
            elif(table == 'individual'):
                write_to = AdministrationIndividual.objects.get(id=id)
            elif(table == 'legal'):
                write_to = AdministrationLegal.objects.get(id=id)
            elif(table == 'cat'):
                write_to = CatastalData.objects.get(id=id)
            
            setattr(write_to, type, value)
            write_to.save()
            return JsonResponse({"success":"Info updated."})

        except Exception as e:
            print('Error saving table data:')
            print(e)
            return JsonResponse({'success':False})
    else:
        return JsonResponse({'success':False})



@login_required(login_url="/login/")
def generate_contract(request, id):
    try:
        print(os.getcwd())
        template = 'apps/app/contracts/bonus-facciata.docx'
        ff = FormFaccata.objects.get(pk=id)
        admin = None
        
        legal = ff.datainit.condominium.select_administrator == 'Legal'

        if legal:
            admin = ff.datainit.admin_legal 
        else:
            admin = ff.datainit.admin_individual
        
        print(admin.name)
        print(admin.company_name)
        print('lel')
        with MailMerge(template) as document:
            document.merge(
                condo_name=ff.datainit.condominium.name,
                condo_fiscal_code=ff.datainit.condominium.fiscal_code,
                condo_street=ff.datainit.condominium.street,
                condo_city=ff.datainit.condominium.cap,
                condo_province=ff.datainit.condominium.province,
                rep_name=admin.company_name if legal else admin.name,
                rep_fiscal_code=admin.fiscal_code if legal else admin.vat_number,
                rep_street=admin.street if legal else admin.activity_street,
                rep_city =admin.cap if legal else admin.activity_location_cap,
                rep_province=admin.province_reg_office if legal else admin.activity_province,
                owner_title=admin.legal_title_rep if legal else admin.title,
                subject_of_intervention=ff.datainit.catastal.description_of_intervention,#Catastal -> description_of_intervention
                total_order_with_taxable_vat=ff.tables.overall_taxable.total_of_the_order, #Overall Taxable total_of_the_order
                total_price_with_amount_vat=ff.tables.overall_in_vat.total_of_the_order_amount_vat,  #Inc Vat total_of_the_order_amount_vat 
                total_price_with_vat=ff.tables.overall_in_vat.total_of_the_order, #Inc Vat total_of_the_order
                total_amount_of_work_to_be_performed=ff.tables.overall_taxable.total_amt_of_work, #Taxable total_amt_of_work overall
                total_amount_of_common_work=ff.tables.common_taxable.total_amt_of_work,#CommonTaxabe -> total_amt_of_work
                total_amount_of_common_work_to_be_performed=ff.tables.common_taxable.total_tech_exp, #CommonTaxable -> total_tech_exp ,
                total_amount_of_safety_charges=ff.tables.common_taxable.total_amt_safety_charges, #CommonTaxable -> total_amt_safety_charges
                date_of_condo_meeting=ff.datainit.catastal.data_of_condominium_assembly, #Catastall -> data_of_condominium_assembly
                advanced_deposit_with_taxable_vat=ff.tables.overall_rep.amount_advance_deposit_by_customer_taxable,#OverallReport -> amount_advance_deposit_by_customer_taxable
                total_amount_including_vat=ff.tables.overall_rep.total_amount_includin_vat, #OverallReport -> total_amount_includin_vat
                amount_of_discount_applied_excluding_vat=ff.tables.overall_rep.amount_of_discount_in_invoice_taxable,#OverallReport -> amount_of_discount_in_invoice_taxable
                amount_of_discount_in_invoice_applied=ff.tables.overall_rep.amount_of_discount_in_invoice,#OverallReport -> amount_of_discount_in_invoice
                name_of_bank_for_the_payment='',
                duration_of_works='',
                date_of_payment_from_condo_to_aurica='',
            )
            save_template = '/contracts/${id}.docx'.format(id=ff.id)
            document.write(save_template)
            with open(save_template, 'r') as f:
                file_data = f.read()
                response = HttpResponse(file_data, content_type='application/msword')
                file_name = '${id}-contract.docx'
                response['Content-Disposition'] = 'attachment; filename="' + file_name + '"'
                return response
    except IOError as e:
        print(e)
        return JsonResponse({'success': False, 'msg': 'No file found!'})
    except Exception as e:
        print(e)
        return JsonResponse({'success':False})
 # columns = [f.name for f in row._meta.get_fields()]