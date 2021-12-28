from .models import *
from django.core.exceptions import ValidationError
from django.contrib import messages
from decimal import Decimal


def overall_calculation_villa(costs):
    try:
        excluding_vat = OverallInterCostsNOVat.objects.get(pk=costs.excluding_vat_id)
        if costs.taxable_vat:
            taxable_vat = OverallInterCostsTaxableVat.objects.get(pk=costs.taxable_vat_id)
        else:
            taxable_vat = OverallInterCostsTaxableVat()

        taxable_vat.total_amt_of_work = excluding_vat.total_amt_of_work
        taxable_vat.total_amt_safety_charges = excluding_vat.total_amt_safety_charges
        taxable_vat.tech_exp_designer = excluding_vat.tech_exp_designer * (1 + excluding_vat.ss_cash_for_designer)
        taxable_vat.tech_exp_coordinator_safety_des = excluding_vat.tech_exp_coordinator_safety_des * \
                                                      (1 + excluding_vat.ss_cash_for_coordinator_safety_des)
        taxable_vat.tech_exp_coordinator_safety_exe = excluding_vat.tech_exp_coordinator_safety_exe * \
                                                      (1 + excluding_vat.ss_cash_for_coordinator_safety_exe)
        taxable_vat.tech_exp_director_of_work = excluding_vat.tech_exp_director_of_work * \
                                                (1 + excluding_vat.ss_cash_for_director_of_work)
        taxable_vat.tech_exp_thermotechnical = excluding_vat.tech_exp_thermotechnical * \
                                               (1 + excluding_vat.ss_cash_for_thermotechnical)
        taxable_vat.tech_exp_energy_expert = excluding_vat.tech_exp_energy_expert * \
                                             (1 + excluding_vat.ss_cash_for_energy_expert)
        taxable_vat.poss_respo_work = excluding_vat.poss_respo_work * (1 + excluding_vat.ss_cash_for_respo_work)
        taxable_vat.app_for_conformity_visa = excluding_vat.app_for_conformity_visa * \
                                              (1 + excluding_vat.ss_app_for_conformity_visa)

        taxable_vat.save()
        costs.taxable_vat = OverallInterCostsTaxableVat.objects.get(pk=taxable_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.included_vat:
            included_vat = OverallInterCostsVatIncluded.objects.get(pk=costs.included_vat_id)
        else:
            included_vat = OverallInterCostsVatIncluded()

        included_vat.total_amt_of_work = taxable_vat.total_amt_of_work * Decimal('1.22')
        included_vat.total_amt_safety_charges = taxable_vat.total_amt_safety_charges * Decimal('1.22')
        included_vat.tech_exp_designer = taxable_vat.tech_exp_designer * Decimal('1.22')
        included_vat.tech_exp_coordinator_safety_des = taxable_vat.tech_exp_coordinator_safety_des * Decimal('1.22')
        included_vat.tech_exp_coordinator_safety_exe = taxable_vat.tech_exp_coordinator_safety_exe * Decimal('1.22')
        included_vat.tech_exp_director_of_work = taxable_vat.tech_exp_director_of_work * Decimal('1.22')
        included_vat.tech_exp_thermotechnical = taxable_vat.tech_exp_thermotechnical * Decimal('1.22')
        included_vat.tech_exp_energy_expert = taxable_vat.tech_exp_energy_expert * Decimal('1.22')
        included_vat.poss_respo_work = taxable_vat.poss_respo_work * Decimal('1.22')
        included_vat.app_for_conformity_visa = taxable_vat.app_for_conformity_visa * Decimal('1.22')

        included_vat.save()
        costs.included_vat = OverallInterCostsVatIncluded.objects.get(pk=included_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.amount_vat:
            amount_vat = OverallInterCostsAmountVat.objects.get(pk=costs.amount_vat_id)
        else:
            amount_vat = OverallInterCostsAmountVat()
        amount_vat.total_amt_of_work = included_vat.total_amt_of_work - taxable_vat.total_amt_of_work
        amount_vat.total_amt_safety_charges = included_vat.total_amt_safety_charges - taxable_vat.total_amt_safety_charges
        amount_vat.tech_exp_designer = included_vat.tech_exp_designer - taxable_vat.tech_exp_designer
        amount_vat.tech_exp_coordinator_safety_des = included_vat.tech_exp_coordinator_safety_des - \
                                                     taxable_vat.tech_exp_coordinator_safety_des
        amount_vat.tech_exp_coordinator_safety_exe = included_vat.tech_exp_coordinator_safety_exe - \
                                                     taxable_vat.tech_exp_coordinator_safety_exe
        amount_vat.tech_exp_director_of_work = included_vat.tech_exp_director_of_work - \
                                               taxable_vat.tech_exp_director_of_work
        amount_vat.tech_exp_thermotechnical = included_vat.tech_exp_thermotechnical - \
                                              taxable_vat.tech_exp_thermotechnical
        amount_vat.tech_exp_energy_expert = included_vat.tech_exp_energy_expert - \
                                            taxable_vat.tech_exp_energy_expert
        amount_vat.poss_respo_work = included_vat.poss_respo_work - taxable_vat.poss_respo_work
        amount_vat.app_for_conformity_visa = included_vat.app_for_conformity_visa - \
                                             taxable_vat.app_for_conformity_visa
        amount_vat.save()
        costs.amount_vat = OverallInterCostsAmountVat.objects.get(pk=amount_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.report:
            report = OverallInterCostsReport.objects.get(pk=costs.report_id)
        else:
            report = OverallInterCostsReport()
        report.total_amt_inc_vat = included_vat.total_of_the_order
        report.save()
        costs.report = OverallInterCostsReport.objects.get(pk=report.id)
        costs.save()

    except ValidationError as e:
        return messages.error(e)


def driving_calculation_villa(costs):
    try:
        excluding_vat = InterDrivingWorkNOVat.objects.get(pk=costs.excluding_vat_id)
        if costs.taxable_vat:
            taxable_vat = InterDrivingWorkTaxableVat.objects.get(pk=costs.taxable_vat_id)
        else:
            taxable_vat = InterDrivingWorkTaxableVat()

        taxable_vat.total_amt_of_work = excluding_vat.total_amt_of_work
        taxable_vat.total_amt_safety_charges = excluding_vat.total_amt_safety_charges
        taxable_vat.tech_exp_designer = excluding_vat.tech_exp_designer * (1 + excluding_vat.ss_cash_for_designer)
        taxable_vat.tech_exp_coordinator_safety_des = excluding_vat.tech_exp_coordinator_safety_des * \
                                                      (1 + excluding_vat.ss_cash_for_coordinator_safety_des)
        taxable_vat.tech_exp_coordinator_safety_exe = excluding_vat.tech_exp_coordinator_safety_exe * \
                                                      (1 + excluding_vat.ss_cash_for_coordinator_safety_exe)
        taxable_vat.tech_exp_director_of_work = excluding_vat.tech_exp_director_of_work * \
                                                (1 + excluding_vat.ss_cash_for_director_of_work)
        taxable_vat.tech_exp_thermotechnical = excluding_vat.tech_exp_thermotechnical * \
                                               (1 + excluding_vat.ss_cash_for_thermotechnical)
        taxable_vat.tech_exp_energy_expert = excluding_vat.tech_exp_energy_expert * \
                                             (1 + excluding_vat.ss_cash_for_energy_expert)
        taxable_vat.poss_respo_work = excluding_vat.poss_respo_work * (1 + excluding_vat.ss_cash_for_respo_work)
        taxable_vat.app_for_conformity_visa = excluding_vat.app_for_conformity_visa * \
                                              (1 + excluding_vat.ss_app_for_conformity_visa)

        taxable_vat.save()
        costs.taxable_vat = InterDrivingWorkTaxableVat.objects.get(pk=taxable_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.included_vat:
            included_vat = InterDrivingWorkVatIncluded.objects.get(pk=costs.included_vat_id)
        else:
            included_vat = InterDrivingWorkVatIncluded()

        included_vat.total_amt_of_work = taxable_vat.total_amt_of_work * Decimal('1.22')
        included_vat.total_amt_safety_charges = taxable_vat.total_amt_safety_charges * Decimal('1.22')
        included_vat.tech_exp_designer = taxable_vat.tech_exp_designer * Decimal('1.22')
        included_vat.tech_exp_coordinator_safety_des = taxable_vat.tech_exp_coordinator_safety_des * Decimal('1.22')
        included_vat.tech_exp_coordinator_safety_exe = taxable_vat.tech_exp_coordinator_safety_exe * Decimal('1.22')
        included_vat.tech_exp_director_of_work = taxable_vat.tech_exp_director_of_work * Decimal('1.22')
        included_vat.tech_exp_thermotechnical = taxable_vat.tech_exp_thermotechnical * Decimal('1.22')
        included_vat.tech_exp_energy_expert = taxable_vat.tech_exp_energy_expert * Decimal('1.22')
        included_vat.poss_respo_work = taxable_vat.poss_respo_work * Decimal('1.22')
        included_vat.app_for_conformity_visa = taxable_vat.app_for_conformity_visa * Decimal('1.22')

        included_vat.save()
        costs.included_vat = InterDrivingWorkVatIncluded.objects.get(pk=included_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.amount_vat:
            amount_vat = InterDrivingWorkAmountVat.objects.get(pk=costs.amount_vat_id)
        else:
            amount_vat = InterDrivingWorkAmountVat()
        amount_vat.total_amt_of_work = included_vat.total_amt_of_work - taxable_vat.total_amt_of_work
        amount_vat.total_amt_safety_charges = included_vat.total_amt_safety_charges - taxable_vat.total_amt_safety_charges
        amount_vat.tech_exp_designer = included_vat.tech_exp_designer - taxable_vat.tech_exp_designer
        amount_vat.tech_exp_coordinator_safety_des = included_vat.tech_exp_coordinator_safety_des - \
                                                     taxable_vat.tech_exp_coordinator_safety_des
        amount_vat.tech_exp_coordinator_safety_exe = included_vat.tech_exp_coordinator_safety_exe - \
                                                     taxable_vat.tech_exp_coordinator_safety_exe
        amount_vat.tech_exp_director_of_work = included_vat.tech_exp_director_of_work - \
                                               taxable_vat.tech_exp_director_of_work
        amount_vat.tech_exp_thermotechnical = included_vat.tech_exp_thermotechnical - \
                                              taxable_vat.tech_exp_thermotechnical
        amount_vat.tech_exp_energy_expert = included_vat.tech_exp_energy_expert - \
                                            taxable_vat.tech_exp_energy_expert
        amount_vat.poss_respo_work = included_vat.poss_respo_work - taxable_vat.poss_respo_work
        amount_vat.app_for_conformity_visa = included_vat.app_for_conformity_visa - \
                                             taxable_vat.app_for_conformity_visa
        amount_vat.save()
        costs.amount_vat = InterDrivingWorkAmountVat.objects.get(pk=amount_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.report:
            report = InterDrivingWorkReport.objects.get(pk=costs.report_id)
        else:
            report = InterDrivingWorkReport()
        report.total_amt_inc_vat = included_vat.total_of_the_order
        report.save()
        costs.report = InterDrivingWorkReport.objects.get(pk=report.id)
        costs.save()

    except ValidationError as e:
        return messages.error(e)


def trailed_calculation_villa(costs):
    try:
        excluding_vat = InterTrailedWorkNOVat.objects.get(pk=costs.excluding_vat_id)
        if costs.taxable_vat:
            taxable_vat = InterTrailedWorkTaxableVat.objects.get(pk=costs.taxable_vat_id)
        else:
            taxable_vat = InterTrailedWorkTaxableVat()

        taxable_vat.total_amt_of_work = excluding_vat.total_amt_of_work
        taxable_vat.total_amt_safety_charges = excluding_vat.total_amt_safety_charges
        taxable_vat.tech_exp_designer = excluding_vat.tech_exp_designer * (1 + excluding_vat.ss_cash_for_designer)
        taxable_vat.tech_exp_coordinator_safety_des = excluding_vat.tech_exp_coordinator_safety_des * \
                                                      (1 + excluding_vat.ss_cash_for_coordinator_safety_des)
        taxable_vat.tech_exp_coordinator_safety_exe = excluding_vat.tech_exp_coordinator_safety_exe * \
                                                      (1 + excluding_vat.ss_cash_for_coordinator_safety_exe)
        taxable_vat.tech_exp_director_of_work = excluding_vat.tech_exp_director_of_work * \
                                                (1 + excluding_vat.ss_cash_for_director_of_work)
        taxable_vat.tech_exp_thermotechnical = excluding_vat.tech_exp_thermotechnical * \
                                               (1 + excluding_vat.ss_cash_for_thermotechnical)
        taxable_vat.tech_exp_energy_expert = excluding_vat.tech_exp_energy_expert * \
                                             (1 + excluding_vat.ss_cash_for_energy_expert)
        taxable_vat.poss_respo_work = excluding_vat.poss_respo_work * (1 + excluding_vat.ss_cash_for_respo_work)
        taxable_vat.app_for_conformity_visa = excluding_vat.app_for_conformity_visa * \
                                              (1 + excluding_vat.ss_app_for_conformity_visa)

        taxable_vat.save()
        costs.taxable_vat = InterTrailedWorkTaxableVat.objects.get(pk=taxable_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.included_vat:
            included_vat = InterTrailedWorkVatIncluded.objects.get(pk=costs.included_vat_id)
        else:
            included_vat = InterTrailedWorkVatIncluded()

        included_vat.total_amt_of_work = taxable_vat.total_amt_of_work * Decimal('1.22')
        included_vat.total_amt_safety_charges = taxable_vat.total_amt_safety_charges * Decimal('1.22')
        included_vat.tech_exp_designer = taxable_vat.tech_exp_designer * Decimal('1.22')
        included_vat.tech_exp_coordinator_safety_des = taxable_vat.tech_exp_coordinator_safety_des * Decimal('1.22')
        included_vat.tech_exp_coordinator_safety_exe = taxable_vat.tech_exp_coordinator_safety_exe * Decimal('1.22')
        included_vat.tech_exp_director_of_work = taxable_vat.tech_exp_director_of_work * Decimal('1.22')
        included_vat.tech_exp_thermotechnical = taxable_vat.tech_exp_thermotechnical * Decimal('1.22')
        included_vat.tech_exp_energy_expert = taxable_vat.tech_exp_energy_expert * Decimal('1.22')
        included_vat.poss_respo_work = taxable_vat.poss_respo_work * Decimal('1.22')
        included_vat.app_for_conformity_visa = taxable_vat.app_for_conformity_visa * Decimal('1.22')

        included_vat.save()
        costs.included_vat = InterTrailedWorkVatIncluded.objects.get(pk=included_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.amount_vat:
            amount_vat = InterTrailedWorkAmountVat.objects.get(pk=costs.amount_vat_id)
        else:
            amount_vat = InterTrailedWorkAmountVat()

        amount_vat.total_amt_of_work = included_vat.total_amt_of_work - taxable_vat.total_amt_of_work
        amount_vat.total_amt_safety_charges = included_vat.total_amt_safety_charges - taxable_vat.total_amt_safety_charges
        amount_vat.tech_exp_designer = included_vat.tech_exp_designer - taxable_vat.tech_exp_designer
        amount_vat.tech_exp_coordinator_safety_des = included_vat.tech_exp_coordinator_safety_des - \
                                                     taxable_vat.tech_exp_coordinator_safety_des
        amount_vat.tech_exp_coordinator_safety_exe = included_vat.tech_exp_coordinator_safety_exe - \
                                                     taxable_vat.tech_exp_coordinator_safety_exe
        amount_vat.tech_exp_director_of_work = included_vat.tech_exp_director_of_work - \
                                               taxable_vat.tech_exp_director_of_work
        amount_vat.tech_exp_thermotechnical = included_vat.tech_exp_thermotechnical - \
                                              taxable_vat.tech_exp_thermotechnical
        amount_vat.tech_exp_energy_expert = included_vat.tech_exp_energy_expert - \
                                            taxable_vat.tech_exp_energy_expert
        amount_vat.poss_respo_work = included_vat.poss_respo_work - taxable_vat.poss_respo_work
        amount_vat.app_for_conformity_visa = included_vat.app_for_conformity_visa - \
                                             taxable_vat.app_for_conformity_visa
        amount_vat.save()
        costs.amount_vat = InterTrailedWorkAmountVat.objects.get(pk=amount_vat.id)

    except ValidationError as e:
        return messages.error(e)

    try:
        if costs.report:
            report = InterTrailedWorkReport.objects.get(pk=costs.report_id)
        else:
            report = InterTrailedWorkReport()
        report.total_amt_inc_vat = included_vat.total_of_the_order
        report.save()
        costs.report = InterTrailedWorkReport.objects.get(pk=report.id)
        costs.save()

    except ValidationError as e:
        return messages.error(e)