from django.db import models
import fractions
from django.forms import ModelForm
from django.forms.widgets import Select, NumberInput
from decimal import Decimal

CASSA_CHOICE = [
    (Decimal('0'), '0%'),
    (Decimal('0.04'), '4%'),
    (Decimal('0.05'), '5%')
]

VTA_CHOICE = [
    (Decimal('0.1'), '10%'),
    (Decimal('0.22'), '22%')
]

VTA_TECH_CHOICE = [
    (Decimal('0'), '0%'),
    (Decimal('0.22'), '22%')
]

DISS_CHOICE = [
    (Decimal('0.9'), '90%')
]


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    total_amount_includin_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_of_discount_in_invoice = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_advance_deposit_by_customer = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_taxable_amount = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_of_discount_in_invoice_taxable = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_advance_deposit_by_customer_taxable = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_amount_of_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_of_discount_in_invoice_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_advance_deposit_by_customer_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)

    def save(self, *args, **kwargs):
        self.amount_of_discount_in_invoice = self.total_amount_includin_vat * 0.9
        self.amount_advance_deposit_by_customer = self.total_amount_includin_vat * 0.1
        self.amount_of_discount_in_invoice_taxable = self.total_taxable_amount * 0.9
        self.amount_advance_deposit_by_customer_taxable = self.total_taxable_amount * 0.1
        self.amount_of_discount_in_invoice_vat = self.total_amount_of_vat * 0.9
        self.amount_advance_deposit_by_customer_vat = self.total_amount_of_vat * 0.1
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class ExVat(models.Model):
    id = models.AutoField(primary_key=True)
    total_amt_of_work = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_amt_safety_charges = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    tech_exp_designer = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    vat_for_designer = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.22'), blank=False,
                                           choices=VTA_TECH_CHOICE)
    ss_cash_for_designer = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.04'), blank=False,
                                               choices=CASSA_CHOICE)
    tech_exp_coordinator_safety_des = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    vat_for_coordinator_safety_des = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.22'),
                                                         blank=False, choices=VTA_TECH_CHOICE)
    ss_cash_for_coordinator_safety_des = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                             blank=False, choices=CASSA_CHOICE)
    tech_exp_coordinator_safety_exe = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    vat_for_coordinator_safety_exe = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.22'),
                                                         blank=False, choices=VTA_TECH_CHOICE)
    ss_cash_for_coordinator_safety_exe = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                             blank=False, choices=CASSA_CHOICE)
    tech_exp_director_of_work = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    vat_for_director_of_work = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.22'),
                                                   blank=False, choices=VTA_TECH_CHOICE)
    ss_cash_for_director_of_work = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                       blank=False, choices=CASSA_CHOICE)
    tech_exp_thermotechnical = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    vat_for_thermotechnical = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.22'),
                                                  blank=False, choices=VTA_TECH_CHOICE)
    ss_cash_for_thermotechnical = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                               blank=False, choices=CASSA_CHOICE)
    tech_exp_energy_expert = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    vat_for_energy_expert = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.22'),
                                                blank=False, choices=VTA_TECH_CHOICE)
    ss_cash_for_energy_expert = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                             blank=False, choices=CASSA_CHOICE)
    poss_respo_work = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'), null=True)
    vat_for_respo_work = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.22'),
                                             blank=False, choices=VTA_TECH_CHOICE)
    ss_cash_for_respo_work = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                 blank=False, choices=CASSA_CHOICE)
    total_tech_exp = models.DecimalField(decimal_places=2, max_digits=12, blank=True)
    total_of_the_order = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'), blank=True)
    vat_for_total_work = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.1'), blank=False,
                                             choices=VTA_CHOICE)
    discount_in_invoice = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.9'), blank=False,
                                              choices=DISS_CHOICE)

    def save(self, *args, **kwargs):
        self.total_tech_exp = self.tech_exp_designer + self.tech_exp_coordinator_safety_des + \
                              self.tech_exp_coordinator_safety_exe + self.tech_exp_director_of_work + \
                              self.tech_exp_thermotechnical + self.tech_exp_energy_expert + self.poss_respo_work
        self.total_of_the_order = self.total_amt_of_work + self.total_amt_safety_charges + self.total_tech_exp
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Taxable(models.Model):
    id = models.AutoField(primary_key=True)
    total_amt_of_work = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    total_amt_safety_charges = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_designer = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_coordinator_safety_des = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_coordinator_safety_exe = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_director_of_work = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_thermotechnical = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_energy_expert = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    poss_respo_work = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    total_tech_exp = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    total_of_the_order = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)

    def save(self, *args, **kwargs):
        self.total_tech_exp = self.tech_exp_designer + self.tech_exp_coordinator_safety_des + \
                              self.tech_exp_coordinator_safety_exe + self.tech_exp_director_of_work + \
                              self.tech_exp_thermotechnical + self.tech_exp_energy_expert + self.poss_respo_work
        self.total_of_the_order = self.total_amt_of_work + self.total_amt_safety_charges + self.total_tech_exp
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class IncVat(models.Model):
    id = models.AutoField(primary_key=True)
    vat_for_total_work = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    total_amt_of_work = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_amt_of_work_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_amt_safety_charges = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_amt_safety_charges_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    tech_exp_designer = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_coordinator_safety_des = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_coordinator_safety_exe = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_director_of_work = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_thermotechnical = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_energy_expert = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    poss_respo_work = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    total_tech_exp = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    total_tech_exp_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_of_the_order = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)
    total_of_the_order_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True)

    def save(self, *args, **kwargs):
        self.total_tech_exp = self.tech_exp_designer + self.tech_exp_coordinator_safety_des + \
                              self.tech_exp_coordinator_safety_exe + self.tech_exp_director_of_work + \
                              self.tech_exp_thermotechnical + self.tech_exp_energy_expert + self.poss_respo_work
        self.total_of_the_order = self.total_amt_of_work + self.total_amt_safety_charges + self.total_tech_exp
        self.total_amt_of_work_amount_vat = fractions.Fraction(self.total_amt_of_work, (1 + self.vat_for_total_work))
        self.total_amt_safety_charges_amount_vat = fractions.Fraction(self.total_amt_safety_charges, 1.22)
        self.total_tech_exp_amount_vat = fractions.Fraction(self.total_tech_exp, 1.22)
        self.total_of_the_order_amount_vat = fractions.Fraction(self.total_of_the_order, 1.22)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class OverallReport(Report):
    pass


class OverallExVat(ExVat):
    pass


class OverallIncVat(IncVat):
    pass


class OverallTaxable(Taxable):
    pass


class CommonWorkReport(Report):
    pass


class CommonWorkExVat(ExVat):
    pass


class CommonWorkIncVat(IncVat):
    pass


class CommonWorkTaxable(Taxable):
    pass


class SubjectiveWorkReport(Report):
    pass


class SubjectiveWorkExVat(ExVat):
    pass


class SubjectiveWorkIncVat(IncVat):
    pass


class SubjectiveWorkTaxable(Taxable):
    pass


class ExVatForm(ModelForm):
    class Meta:
        model = OverallExVat
        exclude = ['id']
        widgets = {
            'total_amt_of_work': NumberInput(attrs={
                'class': 'form-control',
                'id': 'total_amt_of_work'
            }),
            'total_amt_safety_charges': NumberInput(attrs={
                'class': 'form-control',
                'id': 'total_amt_safety_charges'
            }),
            'tech_exp_designer': NumberInput(attrs={
                'class': 'form-control',
                'id': 'tech_exp_designer'
            }),
            'tech_exp_coordinator_safety_des': NumberInput(attrs={
                'class': 'form-control',
                'id': 'tech_exp_coordinator_safety_des'
            }),
            'tech_exp_coordinator_safety_exe': NumberInput(attrs={
                'class': 'form-control',
                'id': 'tech_exp_coordinator_safety_exe'
            }),
            'tech_exp_director_of_work': NumberInput(attrs={
                'class': 'form-control',
                'id': 'tech_exp_director_of_work'
            }),
            'tech_exp_thermotechnical': NumberInput(attrs={
                'class': 'form-control',
                'id': 'tech_exp_thermotechnical'
            }),
            'tech_exp_energy_expert': NumberInput(attrs={
                'class': 'form-control',
                'id': 'tech_exp_energy_expert'
            }),
            'poss_respo_work': NumberInput(attrs={
                'class': 'form-control',
                'id': 'poss_respo_work'
            }),
            'vat_for_total_work': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_total_work'
            }),
            'ss_cash_for_designer': Select(attrs={
                'class': 'form-control',
                'id': 'ss_cash_for_designer'
            }),
            'vat_for_designer': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_designer'
            }),
            'vat_for_coordinator_safety_des': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_coordinator_safety_des'
            }),
            'ss_cash_for_coordinator_safety_des': Select(attrs={
                'class': 'form-control',
                'id': 'ss_cash_for_coordinator_safety_des'
            }),
            'vat_for_coordinator_safety_exe': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_coordinator_safety_exe'
            }),
            'ss_cash_for_coordinator_safety_exe': Select(attrs={
                'class': 'form-control',
                'id': 'ss_cash_for_coordinator_safety_exe'
            }),
            'vat_for_director_of_work': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_director_of_work'
            }),
            'ss_cash_for_director_of_work': Select(attrs={
                'class': 'form-control',
                'id': 'ss_cash_for_director_of_work'
            }),
            'vat_for_thermotechnical': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_thermotechnical'
            }),
            'ss_cash_for_thermotechnical': Select(attrs={
                'class': 'form-control',
                'id': 'ss_cash_for_thermotechnical'
            }),
            'vat_for_energy_expert': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_energy_expert'
            }),
            'ss_cash_for_energy_expert': Select(attrs={
                'class': 'form-control',
                'id': 'ss_cash_for_energy_expert'
            }),
            'vat_for_respo_work': Select(attrs={
                'class': 'form-control',
                'id': 'vat_for_respo_work'
            }),
            'ss_cash_for_respo_work': Select(attrs={
                'class': 'form-control',
                'id': 'ss_cash_for_respo_work'
            }),

        }


class OverallExVatForm(ExVatForm):
    pass
