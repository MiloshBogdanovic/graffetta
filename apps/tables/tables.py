from django.core.exceptions import ValidationError
from .models import OverallTaxable, OverallReport, OverallIncVat, CommonWorkTaxable, CommonWorkIncVat, CommonWorkReport, \
    SubjectiveWorkTaxable, SubjectiveWorkIncVat, SubjectiveWorkReport
from decimal import Decimal


def overall_calculation(fnovat, table_cont):
    print(fnovat)
    try:
        if table_cont.overall_taxable:
            form_taxable = OverallTaxable.objects.get(pk=table_cont.overall_taxable_id)
        else:
            form_taxable = OverallTaxable()

        form_taxable.total_amt_of_work = fnovat.total_amt_of_work
        form_taxable.total_amt_safety_charges = fnovat.total_amt_safety_charges
        form_taxable.tech_exp_designer = fnovat.tech_exp_designer * (1 + fnovat.ss_cash_for_designer)
        form_taxable.tech_exp_coordinator_safety_des = fnovat.tech_exp_coordinator_safety_des * \
                                                       (1 + fnovat.ss_cash_for_coordinator_safety_des)
        form_taxable.tech_exp_coordinator_safety_exe = fnovat.tech_exp_coordinator_safety_exe * \
                                                       (1 + fnovat.ss_cash_for_coordinator_safety_exe)
        form_taxable.tech_exp_director_of_work = fnovat.tech_exp_director_of_work * \
                                                 (1 + fnovat.ss_cash_for_director_of_work)
        form_taxable.tech_exp_thermotechnical = fnovat.tech_exp_thermotechnical * \
                                                (1 + fnovat.ss_cash_for_thermotechnical)
        form_taxable.tech_exp_energy_expert = fnovat.tech_exp_energy_expert * \
                                              (1 + fnovat.ss_cash_for_energy_expert)
        form_taxable.poss_respo_work = fnovat.poss_respo_work * (1 + fnovat.ss_cash_for_respo_work)

        form_taxable.save()
        table_cont.overall_taxable = OverallTaxable.objects.get(id=form_taxable.id)
        table_cont.save()
        print(form_taxable)
        print('Form Taxable saved')

    except ValidationError as e:
        print(e.message_dict)
        return e.message_dict

    try:
        if table_cont.overall_in_vat:
            form_inc_vat = OverallIncVat.objects.get(pk=table_cont.overall_in_vat_id)
        else:
            form_inc_vat = OverallIncVat()

        form_inc_vat.vat_for_total_work = fnovat.vat_for_total_work
        form_inc_vat.total_amt_of_work = form_taxable.total_amt_of_work * (1 + fnovat.vat_for_total_work)
        form_inc_vat.total_amt_safety_charges = form_taxable.total_amt_safety_charges * Decimal('1.22')
        form_inc_vat.tech_exp_designer = form_taxable.tech_exp_designer * (1 + fnovat.vat_for_designer)
        form_inc_vat.tech_exp_coordinator_safety_des = form_taxable.tech_exp_coordinator_safety_des * \
                                                       (1 + fnovat.vat_for_coordinator_safety_des)
        form_inc_vat.tech_exp_coordinator_safety_exe = form_taxable.tech_exp_coordinator_safety_exe * \
                                                       (1 + fnovat.vat_for_coordinator_safety_exe)
        form_inc_vat.tech_exp_director_of_work = form_taxable.tech_exp_director_of_work * \
                                                 (1 + fnovat.vat_for_director_of_work)
        form_inc_vat.tech_exp_thermotechnical = form_taxable.tech_exp_thermotechnical * \
                                                (1 + fnovat.vat_for_thermotechnical)
        form_inc_vat.tech_exp_energy_expert = form_taxable.tech_exp_energy_expert * \
                                              (1 + fnovat.vat_for_energy_expert)
        form_inc_vat.poss_respo_work = form_taxable.poss_respo_work * (1 + fnovat.vat_for_respo_work)

        form_inc_vat.save()

        form_inc_vat.tech_exp_designer_amount_vat = form_inc_vat.tech_exp_designer - \
            (form_inc_vat.tech_exp_designer / (1 + fnovat.vat_for_designer))
        form_inc_vat.tech_exp_coordinator_safety_des_amount_vat = form_inc_vat.tech_exp_coordinator_safety_des - \
            (form_inc_vat.tech_exp_coordinator_safety_des / (1 + fnovat.vat_for_coordinator_safety_des))
        form_inc_vat.tech_exp_coordinator_safety_exe_amount_vat = form_inc_vat.tech_exp_coordinator_safety_exe - \
            (form_inc_vat.tech_exp_coordinator_safety_exe/ (1 + fnovat.vat_for_coordinator_safety_exe))
        form_inc_vat.tech_exp_director_of_work_amount_vat = form_inc_vat.tech_exp_director_of_work - \
            (form_inc_vat.tech_exp_director_of_work / (1 + fnovat.vat_for_director_of_work))
        form_inc_vat.tech_exp_designer_amount_vat = form_inc_vat.tech_exp_designer - \
            (form_inc_vat.tech_exp_designer / (1 + fnovat.vat_for_thermotechnical))
        form_inc_vat.tech_exp_energy_expert_amount_vat = form_inc_vat.tech_exp_energy_expert - \
            (form_inc_vat.tech_exp_energy_expert / (1 + fnovat.vat_for_energy_expert))
        form_inc_vat.poss_respo_work_amount_vat = form_inc_vat.poss_respo_work - \
            (form_inc_vat.poss_respo_work / (1 + fnovat.vat_for_respo_work))
        form_inc_vat.save()
        table_cont.overall_in_vat = OverallIncVat.objects.get(id=form_inc_vat.id)
        table_cont.save()
        print(form_inc_vat)
        print('Form IncVat saved')

    except ValidationError as e:
        print(e.message_dict)
        return e

    try:
        print(form_inc_vat.total_of_the_order)
        if table_cont.overall_rep:
            form_report = OverallReport.objects.get(pk=table_cont.overall_rep_id)
        else:
            form_report = OverallReport()

        form_report.total_amount_includin_vat = form_inc_vat.total_of_the_order
        form_report.total_taxable_amount = form_taxable.total_of_the_order
        form_report.total_amount_of_vat = form_inc_vat.total_of_the_order_amount_vat
        form_report.save()
        table_cont.overall_rep = OverallReport.objects.get(id=form_report.id)
        table_cont.save()
        print(form_report)
        print('Form Report saved')
        return table_cont, form_report, form_taxable, form_inc_vat

    except ValidationError as e:
        print(e.message_dict)
        return e


def common_calculation(fnovat, table_cont):
    print(fnovat)
    try:
        if table_cont.common_taxable:
            form_taxable = CommonWorkTaxable.objects.get(pk=table_cont.common_taxable_id)
        else:
            form_taxable = CommonWorkTaxable()

        form_taxable.total_amt_of_work = fnovat.total_amt_of_work
        form_taxable.total_amt_safety_charges = fnovat.total_amt_safety_charges
        form_taxable.tech_exp_designer = fnovat.tech_exp_designer * (1 + fnovat.ss_cash_for_designer)
        form_taxable.tech_exp_coordinator_safety_des = fnovat.tech_exp_coordinator_safety_des * \
                                                       (1 + fnovat.ss_cash_for_coordinator_safety_des)
        form_taxable.tech_exp_coordinator_safety_exe = fnovat.tech_exp_coordinator_safety_exe * \
                                                       (1 + fnovat.ss_cash_for_coordinator_safety_exe)
        form_taxable.tech_exp_director_of_work = fnovat.tech_exp_director_of_work * \
                                                 (1 + fnovat.ss_cash_for_director_of_work)
        form_taxable.tech_exp_thermotechnical = fnovat.tech_exp_thermotechnical * \
                                                (1 + fnovat.ss_cash_for_thermotechnical)
        form_taxable.tech_exp_energy_expert = fnovat.tech_exp_energy_expert * \
                                              (1 + fnovat.ss_cash_for_energy_expert)
        form_taxable.poss_respo_work = fnovat.poss_respo_work * (1 + fnovat.ss_cash_for_respo_work)

        form_taxable.save()
        table_cont.common_taxable = CommonWorkTaxable.objects.get(id=form_taxable.id)
        table_cont.save()
        print(form_taxable)
        print('Form Taxable saved')

    except ValidationError as e:
        print(e.message_dict)
        return e.message_dict

    try:
        if table_cont.common_in_vat:
            form_inc_vat = CommonWorkIncVat.objects.get(pk=table_cont.common_in_vat_id)
        else:
            form_inc_vat = CommonWorkIncVat()

        form_inc_vat.vat_for_total_work = fnovat.vat_for_total_work
        form_inc_vat.total_amt_of_work = form_taxable.total_amt_of_work * (1 + fnovat.vat_for_total_work)
        form_inc_vat.total_amt_safety_charges = form_taxable.total_amt_safety_charges * Decimal('1.22')
        form_inc_vat.tech_exp_designer = form_taxable.tech_exp_designer * (1 + fnovat.vat_for_designer)
        form_inc_vat.tech_exp_coordinator_safety_des = form_taxable.tech_exp_coordinator_safety_des * \
                                                       (1 + fnovat.vat_for_coordinator_safety_des)
        form_inc_vat.tech_exp_coordinator_safety_exe = form_taxable.tech_exp_coordinator_safety_exe * \
                                                       (1 + fnovat.vat_for_coordinator_safety_exe)
        form_inc_vat.tech_exp_director_of_work = form_taxable.tech_exp_director_of_work * \
                                                 (1 + fnovat.vat_for_director_of_work)
        form_inc_vat.tech_exp_thermotechnical = form_taxable.tech_exp_thermotechnical * \
                                                (1 + fnovat.vat_for_thermotechnical)
        form_inc_vat.tech_exp_energy_expert = form_taxable.tech_exp_energy_expert * \
                                              (1 + fnovat.vat_for_energy_expert)
        form_inc_vat.poss_respo_work = form_taxable.poss_respo_work * (1 + fnovat.vat_for_respo_work)

        form_inc_vat.save()

        form_inc_vat.tech_exp_designer_amount_vat = form_inc_vat.tech_exp_designer - \
            (form_inc_vat.tech_exp_designer / (1 + fnovat.vat_for_designer))
        form_inc_vat.tech_exp_coordinator_safety_des_amount_vat = form_inc_vat.tech_exp_coordinator_safety_des - \
            (form_inc_vat.tech_exp_coordinator_safety_des / (1 + fnovat.vat_for_coordinator_safety_des))
        form_inc_vat.tech_exp_coordinator_safety_exe_amount_vat = form_inc_vat.tech_exp_coordinator_safety_exe - \
            (form_inc_vat.tech_exp_coordinator_safety_exe/ (1 + fnovat.vat_for_coordinator_safety_exe))
        form_inc_vat.tech_exp_director_of_work_amount_vat = form_inc_vat.tech_exp_director_of_work - \
            (form_inc_vat.tech_exp_director_of_work / (1 + fnovat.vat_for_director_of_work))
        form_inc_vat.tech_exp_designer_amount_vat = form_inc_vat.tech_exp_designer - \
            (form_inc_vat.tech_exp_designer / (1 + fnovat.vat_for_thermotechnical))
        form_inc_vat.tech_exp_energy_expert_amount_vat = form_inc_vat.tech_exp_energy_expert - \
            (form_inc_vat.tech_exp_energy_expert / (1 + fnovat.vat_for_energy_expert))
        form_inc_vat.poss_respo_work_amount_vat = form_inc_vat.poss_respo_work - \
            (form_inc_vat.poss_respo_work / (1 + fnovat.vat_for_respo_work))
        form_inc_vat.save()
        table_cont.common_in_vat = CommonWorkIncVat.objects.get(id=form_inc_vat.id)
        table_cont.save()
        print(form_inc_vat)
        print('Form IncVat saved')

    except ValidationError as e:
        print(e.message_dict)
        return e

    try:
        print(form_inc_vat.total_of_the_order)
        if table_cont.common_rep:
            form_report = CommonWorkReport.objects.get(pk=table_cont.common_rep_id)
        else:
            form_report = CommonWorkReport()

        form_report.total_amount_includin_vat = form_inc_vat.total_of_the_order
        form_report.total_taxable_amount = form_taxable.total_of_the_order
        form_report.total_amount_of_vat = form_inc_vat.total_of_the_order_amount_vat
        form_report.save()
        table_cont.common_rep = CommonWorkReport.objects.get(id=form_report.id)
        table_cont.save()
        print(form_report)
        print('Form Report saved')
        return table_cont, form_report, form_taxable, form_inc_vat

    except ValidationError as e:
        print(e.message_dict)
        return e


def subjective_calculation(fnovat, table_cont):
    print(fnovat)
    try:
        if table_cont.subjective_taxable:
            form_taxable = SubjectiveWorkTaxable.objects.get(pk=table_cont.subjective_taxable_id)
        else:
            form_taxable = SubjectiveWorkTaxable()

        form_taxable.total_amt_of_work = fnovat.total_amt_of_work
        form_taxable.total_amt_safety_charges = fnovat.total_amt_safety_charges
        form_taxable.tech_exp_designer = fnovat.tech_exp_designer * (1 + fnovat.ss_cash_for_designer)
        form_taxable.tech_exp_coordinator_safety_des = fnovat.tech_exp_coordinator_safety_des * \
                                                       (1 + fnovat.ss_cash_for_coordinator_safety_des)
        form_taxable.tech_exp_coordinator_safety_exe = fnovat.tech_exp_coordinator_safety_exe * \
                                                       (1 + fnovat.ss_cash_for_coordinator_safety_exe)
        form_taxable.tech_exp_director_of_work = fnovat.tech_exp_director_of_work * \
                                                 (1 + fnovat.ss_cash_for_director_of_work)
        form_taxable.tech_exp_thermotechnical = fnovat.tech_exp_thermotechnical * \
                                                (1 + fnovat.ss_cash_for_thermotechnical)
        form_taxable.tech_exp_energy_expert = fnovat.tech_exp_energy_expert * \
                                              (1 + fnovat.ss_cash_for_energy_expert)
        form_taxable.poss_respo_work = fnovat.poss_respo_work * (1 + fnovat.ss_cash_for_respo_work)

        form_taxable.save()
        table_cont.subjective_taxable = SubjectiveWorkTaxable.objects.get(id=form_taxable.id)
        table_cont.save()
        print(form_taxable)
        print('Form Taxable saved')

    except ValidationError as e:
        print(e.message_dict)
        return e.message_dict

    try:
        if table_cont.subjective_in_vat:
            form_inc_vat = SubjectiveWorkIncVat.objects.get(pk=table_cont.subjective_in_vat_id)
        else:
            form_inc_vat = SubjectiveWorkIncVat()

        form_inc_vat.vat_for_total_work = fnovat.vat_for_total_work
        form_inc_vat.total_amt_of_work = form_taxable.total_amt_of_work * (1 + fnovat.vat_for_total_work)
        form_inc_vat.total_amt_safety_charges = form_taxable.total_amt_safety_charges * Decimal('1.22')
        form_inc_vat.tech_exp_designer = form_taxable.tech_exp_designer * (1 + fnovat.vat_for_designer)
        form_inc_vat.tech_exp_coordinator_safety_des = form_taxable.tech_exp_coordinator_safety_des * \
                                                       (1 + fnovat.vat_for_coordinator_safety_des)
        form_inc_vat.tech_exp_coordinator_safety_exe = form_taxable.tech_exp_coordinator_safety_exe * \
                                                       (1 + fnovat.vat_for_coordinator_safety_exe)
        form_inc_vat.tech_exp_director_of_work = form_taxable.tech_exp_director_of_work * \
                                                 (1 + fnovat.vat_for_director_of_work)
        form_inc_vat.tech_exp_thermotechnical = form_taxable.tech_exp_thermotechnical * \
                                                (1 + fnovat.vat_for_thermotechnical)
        form_inc_vat.tech_exp_energy_expert = form_taxable.tech_exp_energy_expert * \
                                              (1 + fnovat.vat_for_energy_expert)
        form_inc_vat.poss_respo_work = form_taxable.poss_respo_work * (1 + fnovat.vat_for_respo_work)

        form_inc_vat.save()

        form_inc_vat.tech_exp_designer_amount_vat = form_inc_vat.tech_exp_designer - \
            (form_inc_vat.tech_exp_designer / (1 + fnovat.vat_for_designer))
        form_inc_vat.tech_exp_coordinator_safety_des_amount_vat = form_inc_vat.tech_exp_coordinator_safety_des - \
            (form_inc_vat.tech_exp_coordinator_safety_des / (1 + fnovat.vat_for_coordinator_safety_des))
        form_inc_vat.tech_exp_coordinator_safety_exe_amount_vat = form_inc_vat.tech_exp_coordinator_safety_exe - \
            (form_inc_vat.tech_exp_coordinator_safety_exe/ (1 + fnovat.vat_for_coordinator_safety_exe))
        form_inc_vat.tech_exp_director_of_work_amount_vat = form_inc_vat.tech_exp_director_of_work - \
            (form_inc_vat.tech_exp_director_of_work / (1 + fnovat.vat_for_director_of_work))
        form_inc_vat.tech_exp_designer_amount_vat = form_inc_vat.tech_exp_designer - \
            (form_inc_vat.tech_exp_designer / (1 + fnovat.vat_for_thermotechnical))
        form_inc_vat.tech_exp_energy_expert_amount_vat = form_inc_vat.tech_exp_energy_expert - \
            (form_inc_vat.tech_exp_energy_expert / (1 + fnovat.vat_for_energy_expert))
        form_inc_vat.poss_respo_work_amount_vat = form_inc_vat.poss_respo_work - \
            (form_inc_vat.poss_respo_work / (1 + fnovat.vat_for_respo_work))
        form_inc_vat.save()
        table_cont.subjective_in_vat = SubjectiveWorkIncVat.objects.get(id=form_inc_vat.id)
        table_cont.save()
        print(form_inc_vat)
        print('Form IncVat saved')

    except ValidationError as e:
        print(e.message_dict)
        return e

    try:
        if table_cont.subjective_rep:
            form_report = SubjectiveWorkReport.objects.get(pk=table_cont.subjective_rep_id)
        else:
            form_report = SubjectiveWorkReport()

        form_report.total_amount_includin_vat = form_inc_vat.total_of_the_order
        form_report.total_taxable_amount = form_taxable.total_of_the_order
        form_report.total_amount_of_vat = form_inc_vat.total_of_the_order_amount_vat
        form_report.save()
        table_cont.subjective_rep = SubjectiveWorkReport.objects.get(id=form_report.id)
        table_cont.save()
        print(form_report)
        print('Form Report saved')
        return table_cont, form_report, form_taxable, form_inc_vat

    except ValidationError as e:
        print(e.message_dict)
        return e