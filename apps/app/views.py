# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from apps.app.tables import AdministrationIndividualTable, AdministrationLegalTable, CatastalTable, CondominiumTable
from apps.tables.models import TableContract
from apps.beneficary.models import Beneficiary
from apps.app.models import CondominiumData, CondominiumForm, AdministrationIndividualForm, AdministrationLegalForm,\
    FormFaccata, CatastalDataForm, AdministrationIndividual, AdministrationLegal, CatastalData, DataInitial
from django.shortcuts import get_object_or_404, render



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    context['fff'] = FormFaccata.objects.all()
    context['dform'] = DataInitial.objects.all()
    context['tform'] = TableContract.objects.all()
    context['beneficiary'] = Beneficiary.objects.all()
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

@login_required(login_url="/login")
def condo_list(request):
    table = CondominiumTable(CondominiumData.objects.all())
    print(table)
    return render(request, 'editable-tables.html', {
        'title': 'Condominiums',
        'table': table
    })

@login_required(login_url="/login")
def catastal_list(request):
    table = CatastalTable(CatastalData.objects.all())
    return render(request, 'editable-tables.html', {
        'title': 'Catastals',
        'table': table
    })

@login_required(login_url="/login")
def admin_legal_list(request):
    table = AdministrationLegalTable(AdministrationLegal.objects.all())
    return render(request, 'editable-tables.html', {
        'title': 'Administrators Legal',
        'table': table
    })

@login_required(login_url="/login")
def admin_individual_list(request):
    table = AdministrationIndividualTable(AdministrationLegal.objects.all())
    return render(request, 'editable-tables.html', {
        'title': 'Individual Administrators',
        'table': table
    })


@login_required(login_url="/login")
def edit_form(request, table, id):
    context = {'segment': 'index'}
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
                context['message'] = 'Changes successfully made'
                return HttpResponse(html_template.render(context, request))
        
        print('context')
        print(context)

        return HttpResponse(html_template.render(context, request))
    except ValueError as e:
        context['error'] = e
        return HttpResponse(html_template.render(context, request))
    except Exception as e:
        context['error'] = e
        return HttpResponse(html_template.render(context, request))
    
    
@login_required(login_url="/login")
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




 # columns = [f.name for f in row._meta.get_fields()]
