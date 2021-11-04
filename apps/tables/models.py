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
    total_amount_includin_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    amount_of_discount_in_invoice = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_advance_deposit_by_customer = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_taxable_amount = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_of_discount_in_invoice_taxable = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_advance_deposit_by_customer_taxable = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    total_amount_of_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_of_discount_in_invoice_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount_advance_deposit_by_customer_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True)

    def save(self, *args, **kwargs):
        self.amount_of_discount_in_invoice = self.total_amount_includin_vat * Decimal('0.9')
        self.amount_advance_deposit_by_customer = self.total_amount_includin_vat * Decimal('0.1')
        self.amount_of_discount_in_invoice_taxable = self.total_taxable_amount * Decimal('0.9')
        self.amount_advance_deposit_by_customer_taxable = self.total_taxable_amount * Decimal('0.1')
        self.amount_of_discount_in_invoice_vat = self.total_amount_of_vat * Decimal('0.9')
        self.amount_advance_deposit_by_customer_vat = self.total_amount_of_vat * Decimal('0.1')
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
    discount_in_invoice = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.9'), blank=True,
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
    vat_for_total_work = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_amt_of_work = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_amt_of_work_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_amt_safety_charges = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_amt_safety_charges_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    tech_exp_designer = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                            null=True, blank=True)
    tech_exp_designer_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                       null=True, blank=True)
    tech_exp_coordinator_safety_des = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                          null=True, blank=True)
    tech_exp_coordinator_safety_des_amount_vat = models.DecimalField(decimal_places=2, max_digits=12,
                                                                     default=Decimal('0'), null=True, blank=True)
    tech_exp_coordinator_safety_exe = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                          null=True, blank=True)
    tech_exp_coordinator_safety_exe_amount_vat = models.DecimalField(decimal_places=2, max_digits=12,
                                                                     default=Decimal('0'), null=True, blank=True)
    tech_exp_director_of_work = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                    null=True, blank=True)
    tech_exp_director_of_work_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                               null=True, blank=True)
    tech_exp_thermotechnical = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                   null=True, blank=True)
    tech_exp_thermotechnical_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                              null=True, blank=True)
    tech_exp_energy_expert = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                 null=True, blank=True)
    tech_exp_energy_expert_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                            null=True, blank=True)
    poss_respo_work = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'), null=True,
                                          blank=True)
    poss_respo_work_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                     null=True, blank=True)
    total_tech_exp = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'), null=True,
                                         blank=True)
    total_tech_exp_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                    null=True, blank=True)
    total_of_the_order = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                             null=True, blank=True)
    total_of_the_order_amount_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0'),
                                                        null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_tech_exp = self.tech_exp_designer + self.tech_exp_coordinator_safety_des + \
                              self.tech_exp_coordinator_safety_exe + self.tech_exp_director_of_work + \
                              self.tech_exp_thermotechnical + self.tech_exp_energy_expert + self.poss_respo_work
        self.total_of_the_order = self.total_amt_of_work + self.total_amt_safety_charges + self.total_tech_exp
        self.total_amt_of_work_amount_vat = self.total_amt_of_work - (
                self.total_amt_of_work / (1 + self.vat_for_total_work))
        self.total_amt_safety_charges_amount_vat = self.total_amt_safety_charges - (
                self.total_amt_safety_charges / Decimal('1.22'))
        self.total_tech_exp_amount_vat = self.tech_exp_designer_amount_vat + \
                                         self.tech_exp_coordinator_safety_des_amount_vat + self.tech_exp_coordinator_safety_exe_amount_vat + \
                                         self.tech_exp_director_of_work_amount_vat + self.tech_exp_thermotechnical_amount_vat + \
                                         self.tech_exp_energy_expert_amount_vat + self.poss_respo_work_amount_vat

        self.total_of_the_order_amount_vat = self.total_amt_of_work_amount_vat + self.total_amt_safety_charges_amount_vat \
                                             + self.total_tech_exp_amount_vat
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class OverallReport(Report):
    class Meta:
        managed = True


class OverallExVat(ExVat):
    class Meta:
        managed = True


class OverallIncVat(IncVat):
    class Meta:
        managed = True


class OverallTaxable(Taxable):
    class Meta:
        managed = True


class CommonWorkReport(Report):
    class Meta:
        managed = True


class CommonWorkExVat(ExVat):
    class Meta:
        managed = True


class CommonWorkIncVat(IncVat):
    class Meta:
        managed = True


class CommonWorkTaxable(Taxable):
    class Meta:
        managed = True


class SubjectiveWorkReport(Report):
    class Meta:
        managed = True


class SubjectiveWorkExVat(ExVat):
    class Meta:
        managed = True


class SubjectiveWorkIncVat(IncVat):
    class Meta:
        managed = True


class SubjectiveWorkTaxable(Taxable):
    class Meta:
        managed = True


class ExVatForm(ModelForm):
    class Meta:
        model = OverallExVat
        exclude = ['id']
        labels = {
            'total_amt_of_work': 'IMPORTO COMPLESSIVO DEI LAVORI DA ESEGUIRE',
            'total_amt_safety_charges': 'IMPORTO COMPLESSIVO ONERI SICUREZZA ',
            'tech_exp_designer': 'SPESE TECNICHE PROGETTISTA ',
            'tech_exp_coordinator_safety_des': 'SPESE TECNICHE COORDINATORE SICUREZZA PROGETTAZIONE',
            'tech_exp_coordinator_safety_exe': 'SPESE TECNICHE COORDINATORE SICUREZZA ESECUZIONE',
            'tech_exp_director_of_work': 'SPESE TECNICHE DIRETTORE LAVORI',
            'tech_exp_thermotechnical': 'SPESE TECNICHE TERMOTECNICO',
            'tech_exp_energy_expert': 'SPESE TECNICHE ESPERTO ENERGETICO',
            'poss_respo_work': 'EVENTUALE RESPONSABILE DEI LAVORI',
            'vat_for_total_work': 'IVA DA APPLICARE  DEI LAVORI DA ESEGUIRE',
            'ss_cash_for_designer': 'CASSA PREVIDENZA PROGETTISTA',
            'vat_for_designer': 'IVA DA APPLICARE PROGETTISTA',
            'vat_for_coordinator_safety_des': 'IVA DA APPLICARE SICUREZZA PROGETTAZIONE',
            'ss_cash_for_coordinator_safety_des': 'CASSA PREVIDENZA SICUREZZA PROGETTAZIONE',
            'vat_for_coordinator_safety_exe': 'IVA DA APPLICARE SICUREZZA ESECUZIONE',
            'ss_cash_for_coordinator_safety_exe': 'CASSA PREVIDENZA SICUREZZA ESECUZIONE',
            'vat_for_director_of_work': 'IVA DA APPLICARE DIRETTORE LAVORI',
            'ss_cash_for_director_of_work': 'CASSA PREVIDENZA DIRETTORE LAVORI',
            'vat_for_thermotechnical': 'IVA DA APPLICARE TERMOTECNICO',
            'ss_cash_for_thermotechnical': 'CASSA PREVIDENZA TERMOTECNICO',
            'vat_for_energy_expert': 'IVA DA APPLICARE ESPERTO ENERGETICO',
            'ss_cash_for_energy_expert': 'CASSA PREVIDENZA ESPERTO ENERGETICO',
            'vat_for_respo_work': 'IVA DA APPLICARE RESPONSABILE DEI LAVORI',
            'ss_cash_for_respo_work': 'CASSA PREVIDENZA  RESPONSABILE DEI LAVORI'

        }
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


class CommonExVatForm(ExVatForm):
    class Meta(ExVatForm.Meta):
        model = CommonWorkExVat


class OverallExVatForm(ExVatForm):
    pass


class SubjectiveExVatForm(ExVatForm):
    class Meta(ExVatForm.Meta):
        model = SubjectiveWorkExVat


class TableContract(models.Model):
    id = models.AutoField(primary_key=True)
    overall_rep = models.ForeignKey(OverallReport, models.SET_NULL, blank=True, null=True)
    overall_ex_vat = models.ForeignKey(OverallExVat, models.SET_NULL, blank=True, null=True)
    overall_in_vat = models.ForeignKey(OverallIncVat, models.SET_NULL, blank=True, null=True)
    overall_taxable = models.ForeignKey(OverallTaxable, models.SET_NULL, blank=True, null=True)
    common_rep = models.ForeignKey(CommonWorkReport, models.SET_NULL, blank=True, null=True)
    common_ex_vat = models.ForeignKey(CommonWorkExVat, models.SET_NULL, blank=True, null=True)
    common_in_vat = models.ForeignKey(CommonWorkIncVat, models.SET_NULL, blank=True, null=True)
    common_taxable = models.ForeignKey(CommonWorkTaxable, models.SET_NULL, blank=True, null=True)
    subjective_rep = models.ForeignKey(SubjectiveWorkReport, models.SET_NULL, blank=True, null=True)
    subjective_ex_vat = models.ForeignKey(SubjectiveWorkExVat, models.SET_NULL, blank=True, null=True)
    subjective_in_vat = models.ForeignKey(SubjectiveWorkIncVat, models.SET_NULL, blank=True, null=True)
    subjective_taxable = models.ForeignKey(SubjectiveWorkTaxable, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = True
