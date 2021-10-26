from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import OverallExVatForm, OverallTaxable, OverallReport, OverallIncVat
from django import template
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def tables(request):
    context = {'segment': 'table'}
    form_ex_vat = OverallExVatForm()
    form_taxable = OverallTaxable()
    form_report = OverallReport()
    form_inc_vat = OverallIncVat()
    context['form_ex_vat'] = form_ex_vat

    if request.method == 'POST':
        form_ex_vat = OverallExVatForm(request.POST)
        if form_ex_vat.is_valid():
            fnovat = form_ex_vat.save()
            print(fnovat.total_amt_of_work)
            form_taxable.total_amt_of_work = fnovat.total_amt_of_work
            form_taxable.total_amt_safety_charges = fnovat.total_amt_safety_charges
            form_taxable.tech_exp_designer = fnovat.tech_exp_designer * fnovat.ss_cash_for_tech_exp
            form_taxable.tech_exp_coordinator_safety_des = fnovat.tech_exp_coordinator_safety_des * \
                                                           (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_coordinator_safety_exe = fnovat.tech_exp_coordinator_safety_exe * \
                                                           (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_director_of_work = fnovat.tech_exp_director_of_work * \
                                                     (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_thermotechnical = fnovat.tech_exp_thermotechnical * \
                                                    (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_energy_expert = fnovat.tech_exp_energy_expert * \
                                                  (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.poss_respo_work = fnovat.poss_respo_work * fnovat.ss_cash_for_tech_exp

            form_taxable.save()

            form_inc_vat.vat_for_total_work = fnovat.vat_for_total_work
            form_inc_vat.total_amt_of_work = form_taxable.total_amt_of_work * (1 + form_inc_vat.vat_for_total_work)
            form_inc_vat.total_amt_safety_charges = fnovat.total_amt_safety_charges
            form_taxable.tech_exp_designer = fnovat.tech_exp_designer * fnovat.ss_cash_for_tech_exp
            form_taxable.tech_exp_coordinator_safety_des = fnovat.tech_exp_coordinator_safety_des * \
                                                           (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_coordinator_safety_exe = fnovat.tech_exp_coordinator_safety_exe * \
                                                           (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_director_of_work = fnovat.tech_exp_director_of_work * \
                                                     (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_thermotechnical = fnovat.tech_exp_thermotechnical * \
                                                    (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.tech_exp_energy_expert = fnovat.tech_exp_energy_expert * \
                                                  (1 + fnovat.ss_cash_for_tech_exp)
            form_taxable.poss_respo_work = fnovat.poss_respo_work * fnovat.ss_cash_for_tech_exp

            context['form_ex_vat'] = fnovat
            context['form_taxable'] = form_taxable

            html_template = loader.get_template('tables.html')
            return HttpResponse(html_template.render(context, request))

        else:
            print(form_ex_vat.errors)
            context['error'] = form_ex_vat.errors

    html_template = loader.get_template('tables.html')
    return HttpResponse(html_template.render(context, request))
