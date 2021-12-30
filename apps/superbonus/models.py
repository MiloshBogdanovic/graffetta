
from apps.beneficary.models import Beneficiary, BeneficiaryForm
from apps.professionals.models import *
from decimal import Decimal
from django.forms import ModelForm
from django.forms.widgets import Textarea, DateInput
from internationalflavor.vat_number import VATNumberField
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
# Create your models here.

YN = [
    ('NO', 'NO'),
    ('SI', 'SI')
]

TITLE = [
    ('SIG.RA', 'SIG.RA'),
    ('GEOM.', 'GEOM.'),
    ('RAG.', 'RAG.'),
    ('ING.', 'ING.'),
    ('ARCH', 'ARCH'),
    ('ALTRO', 'ALTRO')
]

CASSA_CHOICE = [
    (Decimal('0'), '0%'),
    (Decimal('0.04'), '4%'),
    (Decimal('0.05'), '5%')
]

VTA_CHOICE = [
    (Decimal('0.1'), '10%'),
    (Decimal('0.22'), '22%')
]


def validate_cap(value):
    if not re.match(r'^([\s\d]{5})$', value):
        raise ValidationError(
            _('%(value)s is not an 5 digits cap number'),
            params={'value': value},
        )


class InterventionReport(models.Model):
    id = models.AutoField(primary_key=True)
    total_amt_inc_vat = models.DecimalField("IMPORTO COMPLESSIVO IVA INCLUSA", decimal_places=2,
                                            max_digits=12, default=0, null=True)
    amt_discount_applied = models.DecimalField("IMPORTO DELLO SCONTO IN FATTURA APPLICATO", decimal_places=2,
                                               max_digits=12, default=0, null=True)
    amt_deduction_accrued = models.DecimalField("IMPORTO DELLA DETRAZIONE MATURATA", decimal_places=2,
                                                max_digits=12, default=0, null=True)

    def save(self, *args, **kwargs):
        self.amt_discount_applied = self.total_amt_inc_vat
        self.amt_deduction_accrued = self.total_amt_inc_vat * Decimal('1.1')
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        managed = True


class InterventionCost(models.Model):
    id = models.AutoField(primary_key=True)
    total_amt_of_work = models.DecimalField("IMPORTO COMPLESSIVO DEI LAVORI DA ESEGUIRE", decimal_places=2,
                                            max_digits=12, default=0, null=True)
    total_amt_safety_charges = models.DecimalField("IMPORTO COMPLESSIVO ONERI SICUREZZA ", decimal_places=2,
                                                   max_digits=12, default=0, null=True)
    tech_exp_designer = models.DecimalField("SPESE TECNICHE PROGETTISTA ", decimal_places=2, max_digits=12, default=0,
                                            null=True)
    tech_exp_coordinator_safety_des = models.DecimalField("SPESE TECNICHE COORDINATORE SICUREZZA PROGETTAZIONE",
                                                          decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_coordinator_safety_exe = models.DecimalField("SPESE TECNICHE COORDINATORE SICUREZZA ESECUZIONE",
                                                          decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_director_of_work = models.DecimalField("SPESE TECNICHE DIRETTORE LAVORI", decimal_places=2, max_digits=12,
                                                    default=0, null=True)
    tech_exp_thermotechnical = models.DecimalField("SPESE TECNICHE TERMOTECNICO", decimal_places=2, max_digits=12,
                                                   default=0, null=True)
    tech_exp_energy_expert = models.DecimalField("SPESE TECNICHE ESPERTO ENERGETICO", decimal_places=2, max_digits=12,
                                                 default=0, null=True)
    poss_respo_work = models.DecimalField("EVENTUALE RESPONSABILE DEI LAVORI", decimal_places=2, max_digits=12,
                                          default=0, null=True)
    app_for_conformity_visa = models.DecimalField("APPOSIZIONE VISTO DI CONFORMTA'", decimal_places=2, max_digits=12,
                                                  default=0, null=True)
    total_tech_exp = models.DecimalField("TOTALE TECNICHE", decimal_places=2, max_digits=12, default=0, null=True)
    total_of_the_order = models.DecimalField("TOTALE DELLA COMMESSA", decimal_places=2, max_digits=12, default=0,
                                             null=True)

    def save(self, *args, **kwargs):
        self.total_tech_exp = self.tech_exp_designer + self.tech_exp_coordinator_safety_des + \
                              self.tech_exp_coordinator_safety_exe + self.tech_exp_director_of_work + \
                              self.tech_exp_thermotechnical + self.tech_exp_energy_expert + self.poss_respo_work + \
                              self.app_for_conformity_visa
        self.total_of_the_order = self.total_amt_of_work + self.total_amt_safety_charges + self.total_tech_exp
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        managed = True


class InterCostsNOVat(InterventionCost):
    vat_for_total_work = models.DecimalField("IMPORTO COMPLESSIVO IVA DA APPLICARE", decimal_places=2, max_digits=10,
                                             default=Decimal('0.22'), blank=False,
                                             choices=VTA_CHOICE)
    ss_cash_for_designer = models.DecimalField("CASSA PREVIDENZA PROGETTISTA", decimal_places=2, max_digits=10,
                                               default=Decimal('0.04'), blank=False,
                                               choices=CASSA_CHOICE)
    ss_cash_for_coordinator_safety_des = models.DecimalField("CASSA PREVIDENZA COORDINATORE SICUREZZA PROGETTAZIONE",
                                                             decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                             blank=False, choices=CASSA_CHOICE)
    ss_cash_for_coordinator_safety_exe = models.DecimalField("CASSA PREVIDENZA COORDINATORE SICUREZZA ESECUZIONE",
                                                             decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                             blank=False, choices=CASSA_CHOICE)
    ss_cash_for_director_of_work = models.DecimalField("CASSA PREVIDENZA DIRETTORE LAVORI", decimal_places=2,
                                                       max_digits=10, default=Decimal('0.04'),
                                                       blank=False, choices=CASSA_CHOICE)
    ss_cash_for_thermotechnical = models.DecimalField("CASSA PREVIDENZA TECNICHE TERMOTECNICO", decimal_places=2,
                                                      max_digits=10, default=Decimal('0.04'),
                                                      blank=False, choices=CASSA_CHOICE)
    ss_cash_for_energy_expert = models.DecimalField("CASSA PREVIDENZA ESPERTO ENERGETICO", decimal_places=2,
                                                    max_digits=10, default=Decimal('0.04'),
                                                    blank=False, choices=CASSA_CHOICE)
    ss_cash_for_respo_work = models.DecimalField("CASSA PREVIDENZA RESPONSABILE DEI LAVORI", decimal_places=2,
                                                 max_digits=10, default=Decimal('0.04'),
                                                 blank=False, choices=CASSA_CHOICE)
    ss_app_for_conformity_visa = models.DecimalField("CASSA PREVIDENZA ", decimal_places=2, max_digits=10,
                                                     default=Decimal('0.0'),
                                                     blank=False, choices=CASSA_CHOICE)

    class Meta:
        abstract = True
        managed = True


class AdministrationIndividual(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('TITOLO AMMINISTRATORE', max_length=50, choices=TITLE)
    name = models.CharField('COGNOME e NOME', max_length=120)
    fiscal_code = models.CharField('CODICE FISCALE', max_length=16, blank=True)
    vat_number = VATNumberField(countries=['IT'], verbose_name='PARTITA IVA', default='IT12345678901')
    dob = models.DateField('DATA DI NASCITA', auto_now=False, auto_now_add=False, default=date.today)
    birthplace = models.CharField('COMUNE DI NASCITA', max_length=50, blank=True)
    birthplace_county = models.CharField('PROVINCIA DI NASCITA', max_length=30, blank=True)
    activity_street = models.CharField("VIA E NUMERO/I SEDE ATTIVITA'", max_length=50, blank=True)
    activity_location_cap = models.CharField("CAP SEDE ATTIVITA'", max_length=5, validators=[validate_cap])
    activity_municipality = models.CharField("COMUNE SEDE ATTIVITA'", max_length=50, blank=True)
    activity_province = models.CharField("PROVINCIA SEDE ATTIVITA'", max_length=50, blank=True)
    residence_street = models.CharField('VIA E NUMERO RESIDENZA', max_length=50, blank=True)
    residence_cap = models.CharField("CAP RESIDENZA", max_length=5, validators=[validate_cap])
    residence_city = models.CharField('COMUNE DI RESIDENZA', max_length=50, blank=True)
    residence_province = models.CharField('PROVINCIA DI RESIDENZA', max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True


class AdministrationLegal(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField("DENOMINAZIONE SOCIETA'", max_length=50)
    province = models.CharField('PROVINCIA/E ISCRIZIONE', max_length=20, blank=True)
    company_register = models.BigIntegerField('REGISTRO IMPRESE', blank=True)
    vat_number = VATNumberField(countries=['IT'], verbose_name='N° ISCRIZIONE REGISTRO IMPRESE - PARTITA IVA - C.F.',
                                default='IT12345678901')
    street_legal = models.CharField('VIA E NUMERO SEDE LEGALE', max_length=100, blank=True)
    cap_legal = models.CharField('CAP SEDE LEGALE',  max_length=5, validators=[validate_cap])
    municipal_reg_office = models.CharField('COMUNE SEDE LEGALE', max_length=30, blank=True)
    province_reg_office = models.CharField('PROVINCIA SEDE LEGALE', max_length=20, blank=True)
    legal_title_rep = models.CharField('TITOLO LEGALE RAPPRESENTATE', null=True, max_length=10, choices=TITLE)
    leg_rep_name = models.CharField('COGNOME E NOME LEGALE RAPPRESENTANTE', max_length=100, blank=True)
    leg_rep_tax_code = models.CharField('CODICE FISCALE LEGALE RAPPRESENTATE', max_length=20, blank=True)
    leg_rep_dob = models.DateField('DATA DI NASCITA LEGALE RAPPRESENTANTE', auto_now=False, auto_now_add=False, default=date.today)
    municipal_of_birth_of_leg = models.CharField('COMUNE DI NASCITA DEL LEGALE RAPPRESENTANTE', max_length=30, blank=True)
    province_of_birth_of_leg = models.CharField('PROVINCIA DI NASCITA DEL LEGALE RAPPRESENTANTE', max_length=30, blank=True)
    leg_rep_street = models.CharField('VIA E NUMERO RESIDENZA LEGALE RAPPRESENTANTE', max_length=50, blank=True)
    cap_rep_res = models.CharField('CAP RESIDENZA LEGALE RAPPRESENTANTE', max_length=5, validators=[validate_cap])
    municipal_of_leg_residence = models.CharField('COMUNE DI RESIDENZA LEGALE RAPPRESENTANTE', max_length=30, blank=True)
    province_of_leg_residence = models.CharField('PROVINCIA DI RESIDENZA LEGALE RAPPRESENTANTE', max_length=30, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = True


class OverallInterCostsNOVat(InterCostsNOVat):
    pass


class OverallInterCostsTaxableVat(InterventionCost):
    pass


class OverallInterCostsVatIncluded(InterventionCost):
    pass


class OverallInterCostsAmountVat(InterventionCost):
    pass


class OverallInterCostsReport(InterventionReport):
    pass


class InterDrivingWorkNOVat(InterCostsNOVat):
    pass


class InterDrivingWorkTaxableVat(InterventionCost):
    pass


class InterDrivingWorkVatIncluded(InterventionCost):
    pass


class InterDrivingWorkAmountVat(InterventionCost):
    pass


class InterDrivingWorkReport(InterventionReport):
    pass


class CommonWorkNOVat(InterCostsNOVat):
    pass


class CommonWorkTaxableVat(InterventionCost):
    pass


class CommonWorkVatIncluded(InterventionCost):
    pass


class CommonWorkAmountVat(InterventionCost):
    pass


class CommonWorkReport(InterventionReport):
    pass


class SubjectiveWorkNOVat(InterCostsNOVat):
    pass


class SubjectiveWorkTaxableVat(InterventionCost):
    pass


class SubjectiveWorkVatIncluded(InterventionCost):
    pass


class SubjectiveWorkAmountVat(InterventionCost):
    pass


class SubjectiveWorkReport(InterventionReport):
    pass


class InterTrailedWorkNOVat(InterCostsNOVat):
    pass


class InterTrailedWorkTaxableVat(InterventionCost):
    pass


class InterTrailedWorkVatIncluded(InterventionCost):
    pass


class InterTrailedWorkAmountVat(InterventionCost):
    pass


class InterTrailedWorkReport(InterventionReport):
    pass


class CatastalData(models.Model):
    id = models.AutoField(primary_key=True)
    n_catastal_cheet = models.IntegerField("N° FOGLIO CATASTALE DI APPARTENENZA", blank=False)
    n_first_particle = models.IntegerField("N° PRIMA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=False)
    n_subscribers_to_first_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA PRIMA PARTICELLA", max_length=20,
                                                        blank=False)
    n_second_particle = models.IntegerField("N° SECONDA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True)
    n_subscribers_to_second_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA SECONDA PARTICELLA",
                                                         max_length=20, blank=True, null=True)
    n_third_particle = models.IntegerField("N° TERZA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True)
    n_subscribers_to_third_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA TERZA PARTICELLA", max_length=20,
                                                        blank=True, null=True)
    n_fourth_particle = models.IntegerField("N° QUARTA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True)
    n_subscribers_to_fourth_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA QUARTA PARTICELLA",
                                                         max_length=20, blank=True, null=True)
    n_fifth_particle = models.IntegerField("N° QUINTA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True)
    n_subscribers_to_fifth_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA QUINTA PARTICELLA",
                                                        max_length=20, blank=True, null=True)


class Interventions(models.Model):
    id = models.AutoField(primary_key=True)
    art119_c1_a = models.CharField(max_length=2, choices=YN)
    art119_c1_b = models.CharField(max_length=2, choices=YN)
    art119c_4 = models.CharField(max_length=2, choices=YN)
    art1_c345 = models.CharField(max_length=2, choices=YN)
    art1_c345_art14 = models.CharField(max_length=2, choices=YN)
    art1_c346 = models.CharField(max_length=2, choices=YN)
    art1_c286 = models.CharField(max_length=2, choices=YN)
    art14_2_1 = models.CharField(max_length=2, choices=YN)
    art14_2_1_B = models.CharField(max_length=2, choices=YN)
    art14_2_1_C = models.CharField(max_length=2, choices=YN)
    art4_c4 = models.CharField(max_length=2, choices=YN)
    art1_c88 = models.CharField(max_length=2, choices=YN)
    art14_c2 = models.CharField(max_length=2, choices=YN)
    art14_c2_bis = models.CharField(max_length=2, choices=YN)
    art14_c2_b_bis = models.CharField(max_length=2, choices=YN)
    trailed_art16_bis_c = models.CharField(max_length=2, choices=YN)
    trailed_art119_c = models.CharField(max_length=2, choices=YN)
    towed_art119_c = models.CharField(max_length=2, choices=YN)
    description = models.TextField(max_length=500)
    date_of_assembly = models.DateField('DATA ASSEMBLEA CONDOMINIALE IN CUI I CONDOMINI HANNO IRREVOCABILMENTE OPTATO PER LO SCONTO IN FATTURA',
                                        auto_now=False, auto_now_add=False, default=date.today)

    class Meta:
        managed = True


class OverallInterventions(models.Model):
    id = models.AutoField(primary_key=True)
    excluding_vat = models.ForeignKey(OverallInterCostsNOVat, on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name="IMPORTO IVA ESCLUSA")
    taxable_vat = models.ForeignKey(OverallInterCostsTaxableVat, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="IMPONIBILE IVA")
    included_vat = models.ForeignKey(OverallInterCostsVatIncluded, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="IMPORTO IVA INCLUSA")
    amount_vat = models.ForeignKey(OverallInterCostsAmountVat, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name="IMPORTO IVA")
    report = models.ForeignKey(OverallInterCostsReport, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="RAPPORTO")

    class Meta:
        managed = True


class DrivingInterventions(models.Model):
    id = models.AutoField(primary_key=True)
    excluding_vat = models.ForeignKey(InterDrivingWorkNOVat, on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name="IMPORTO IVA ESCLUSA")
    taxable_vat = models.ForeignKey(InterDrivingWorkTaxableVat, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="IMPONIBILE IVA")
    included_vat = models.ForeignKey(InterDrivingWorkVatIncluded, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="IMPORTO IVA INCLUSA")
    amount_vat = models.ForeignKey(InterDrivingWorkAmountVat, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name="IMPORTO IVA")
    report = models.ForeignKey(InterDrivingWorkReport, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="RAPPORTO")


class CommonInterventions(models.Model):
    id = models.AutoField(primary_key=True)
    excluding_vat = models.ForeignKey(CommonWorkNOVat, on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name="IMPORTO IVA ESCLUSA")
    taxable_vat = models.ForeignKey(CommonWorkTaxableVat, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="IMPONIBILE IVA")
    included_vat = models.ForeignKey(CommonWorkVatIncluded, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="IMPORTO IVA INCLUSA")
    amount_vat = models.ForeignKey(CommonWorkAmountVat, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name="IMPORTO IVA")
    report = models.ForeignKey(CommonWorkReport, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="RAPPORTO")


class SubjectiveInterventions(models.Model):
    id = models.AutoField(primary_key=True)
    excluding_vat = models.ForeignKey(SubjectiveWorkNOVat, on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name="IMPORTO IVA ESCLUSA")
    taxable_vat = models.ForeignKey(SubjectiveWorkTaxableVat, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="IMPONIBILE IVA")
    included_vat = models.ForeignKey(SubjectiveWorkVatIncluded, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="IMPORTO IVA INCLUSA")
    amount_vat = models.ForeignKey(SubjectiveWorkAmountVat, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name="IMPORTO IVA")
    report = models.ForeignKey(SubjectiveWorkReport, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="RAPPORTO")


class TrailingInterventions(models.Model):
    id = models.AutoField(primary_key=True)
    excluding_vat = models.ForeignKey(InterTrailedWorkNOVat, on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name="IMPORTO IVA ESCLUSA")
    taxable_vat = models.ForeignKey(InterTrailedWorkTaxableVat, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="IMPONIBILE IVA")
    included_vat = models.ForeignKey(InterTrailedWorkVatIncluded, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="IMPORTO IVA INCLUSA")
    amount_vat = models.ForeignKey(InterTrailedWorkAmountVat, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name="IMPORTO IVA")
    report = models.ForeignKey(InterTrailedWorkReport, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="RAPPORTO")


class BonusVilla(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("DENOMINAZIONE DELL'IMMOBILE", max_length=50, blank=False)
    street = models.CharField("VIA E NUMERO/I UBICAZIONE  DELL'IMMOBILE", max_length=50, blank=False)
    cap = models.CharField("CAP UBICAZIONE DELL'IMMOBILE", max_length=5, validators=[validate_cap])
    municipality = models.CharField("COMUNE UBICAZIONE DELL'IMMOBILE", max_length=50, blank=False)
    province = models.CharField("PROVINCIA UBICAZIONE DELL'IMMOBILE", max_length=10, blank=False)
    email = models.EmailField("INDIRIZZO MAIL DELL'IMMOBILE - DEL CLIENTE", max_length=254, blank=False)
    pec_mail = models.EmailField("INDIRIZZO PEC DELL'IMMOBILE - DEL CLIENTE", max_length=254, blank=False)
    catastal = models.ForeignKey(CatastalData, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="DATI CATASTALI")
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name="DETTAGLIO DEI BENEFICIARI")
    professionals = models.ForeignKey(Prof_table, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="PROFESSIONALI")
    interventions = models.ForeignKey(Interventions, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="INTERVENTI")
    overall_interventions = models.ForeignKey(OverallInterventions, on_delete=models.SET_NULL, blank=True, null=True,
                                              verbose_name="COMPLESSIVA DELL'INTERVENTO")
    driving_interventions = models.ForeignKey(DrivingInterventions, on_delete=models.SET_NULL, blank=True, null=True,
                                              verbose_name="DETTAGLIO INTERVENTO LAVORI TRAINANTI")
    trailed_interventions = models.ForeignKey(TrailingInterventions, on_delete=models.SET_NULL, blank=True, null=True,
                                              verbose_name="DETTAGLIO INTERVENTO LAVORI TRAINATI")

    class Meta:
        managed = True


class BonusCondo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("DENOMINAZIONE CONDOMINIO", max_length=50, blank=False)
    fiscal_code = models.CharField("CODICE FISCALE", max_length=16, blank=True)
    street = models.CharField("CONDOMINIO VIA E NUMERO/I UBICAZIONE", max_length=50, blank=False)
    cap = models.CharField("CAP UBICAZIONE CONDOMINIO - IMMOBILE", max_length=5, validators=[validate_cap])
    common_location = models.CharField("COMUNE UBICAZIONE CONDOMINIO - IMMOBILE", max_length=50, blank=True)
    province = models.CharField("CONDOMINIO - IMMOBILE PROVINCIA UBICAZIONE ", max_length=10, blank=True)
    email = models.EmailField("CONDOMINIO - IMMOBILE INDIRIZZO MAIL DEL", max_length=54, blank=False)
    pec_mail = models.EmailField("CONDOMINIO INDIRIZZO PEC DEL CONDOMINIO", max_length=54, blank=False)
    catastal = models.ForeignKey(CatastalData, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="DATI CATASTALI")
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name="DETTAGLIO DEI BENEFICIARI")
    professionals = models.ForeignKey(Prof_table, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="PROFESSIONALI")
    interventions = models.ForeignKey(Interventions, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="INTERVENTI")
    overall_interventions = models.ForeignKey(OverallInterventions, on_delete=models.SET_NULL, blank=True, null=True,
                                              verbose_name="COMPLESSIVA DELL'INTERVENTO")
    common_interventions = models.ForeignKey(CommonInterventions, on_delete=models.SET_NULL, blank=True, null=True,
                                              verbose_name="DETTAGLIO INTERVENTO LAVORI COMUNI")
    subjective_interventions = models.ForeignKey(SubjectiveInterventions, on_delete=models.SET_NULL, blank=True,
                                                 null=True, verbose_name="DETTAGLIO INTERVENTO LAVORI SOGGETTIVI")
    admin_legal = models.ForeignKey(AdministrationLegal, on_delete=models.SET_NULL, blank=True,
                                                 null=True, verbose_name="AMMINISTRATORE PERSONA GIURIDICA")
    admin_individual = models.ForeignKey(AdministrationIndividual, on_delete=models.SET_NULL, blank=True,
                                                 null=True, verbose_name="AMMINISTRATORE PERSONA FISICA")


class SuperBonus(models.Model):
    id = models.AutoField(primary_key=True)
    bonus_villa = models.ForeignKey(BonusVilla, on_delete=models.CASCADE, blank=True, null=True)
    bonus_condo = models.ForeignKey(BonusCondo, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True


class BonusVillaForm(ModelForm):
    class Meta:
        model = BonusVilla
        exclude = ['id', 'catastal', 'beneficiary', 'professionals', 'interventions', 'overall_interventions', 'driving_interventions', 'trailed_interventions']
        labels = {}
        widgets = {}


class InterventionsForm(ModelForm):
    class Meta:
        model = Interventions
        exclude = ['id', 'date_of_assembly']
        labels = {
            'art119_c1_a': 'Intervento “trainante” ai sensi dell’art. 119 c. 1 lett a), D.L. 34/2020: intervento di “isolamento termico” (con materiali isolanti che rispettano i “CAM” del D.M. dell’Ambiente del 11/10/2017) delle superfici opache verticali (pareti isolanti o cappotti, anche sulla superficie intera delle pareti), orizzontali (pavimenti e coperture) e inclinate (falde di copertura del sottotetto), che interessa l’involucro dell’Immobile, con un’incidenza superiore al 25% della superficie disperdente lorda;',
            'art119_c1_b': ' Intervento “trainante” ai sensi dell’art. 119 c. 1 lett. b), D.L. 34/2020 per la “sostituzione degli impianti di climatizzazione invernale” esistenti nell’Immobile con (i) impianti per il riscaldamento, il raffrescamento o la fornitura di acqua calda sanitaria, a condensazione, con efficienza almeno pari alla classe A (regolamento UE n. 811/2013), a pompa di calore, ivi compresi gli impianti ibridi o geotermici ovvero con impianti di microcogenerazione, a collettori solari; (ii) allaccio a sistemi di teleriscaldamento efficiente (art. 2, c. 2, lett. tt), D.Lgs. 102/2014), solo nelle aree non metanizzate nei comuni montani non interessati dalle procedure europee di infrazione n. 2014/2147 o 2015/2043',
            'art119c_4': "Intervento “trainante” ai sensi dell’art. 119 c. 4, D.L. 34/2020 per la realizzazione di misure antisismiche dell'articolo 16, commi da 1-bis a 1-septies, D.L. 63/2013.",
            'art1_c345': 'art. 1, co. 345, L. 296/2006 per la realizzazione di strutture opache verticali (pareti) ed orizzontali (coperture e pavimenti);',
            'art1_c345_art14': 'art. 1, co. 345, L. 296/2006 e art. 14, D.L. 63/2013 per la installazione di finestre comprensive di infissi delimitanti il volume riscaldato verso l’esterno ovvero vani non riscaldati, con i requisiti di trasmittanza termica di legge;',
            'art1_c346': 'art. 1, co. 346, L. 296/2006 per l’installazione di pannelli solari per la produzione di acqua calda;',
            'art1_c286': 'art. 1, co. 286, L. 244/2007 per la sostituzione di impianti di climatizzazione invernale con caldaie dotate di pompe di calore ad alta efficienza o impianti geotermici a bassa entalpia;',
            'art14_2_1': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013',
            'art14_2_1_B': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013 e contestuale installazione di sistemi di termoregolazione di cui alle classi V, VI o VIII della Comunicazione della Commissione 2014/C 207/02',
            'art14_2_1_C': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con apparecchi ibridi, costituiti da pompa di calore integrata con caldaia a condensazione, assemblati in fabbrica per funzionare in abbinamento tra loro;',
            'art4_c4': 'art. 4, co. 4, D.L. 201/2011 per la sostituzione di scaldacqua tradizionali con scaldacqua a pompa di calore per la produzione di acqua calda sanitaria che rispettino i valori fissati dalle relative tabelle vigenti,',
            'art1_c88': 'art. 1, co. 88, L. 208/2015 per l’acquisto ed installazione di dispositivi multimediali per il controllo da remoto degli impianti di riscaldamento o produzione di acqua calda o di climatizzazione delle unità abitative;',
            'art14_c2': 'art. 14, co. 2 lett b) del D.L. 63/2013 per l’acquisto ed installazione di schermature solari di cui all’allegato M), D.Lgs. 311/2006;',
            'art14_c2_bis': 'art. 14, co. 2-bis, D.L. 63/2013 par l’acquisto ed installazione di impianti di climatizzazione invernale con impianti dotati di generatori di calore alimentati da biomasse combustibili;',
            'art14_c2_b_bis': 'art. 14, co. 2, lett. b-bis) D.L. 63/2013 per l’acquisto ed installazione di micro-cogeneratori che permettano un risparmio di energia primaria (PES) di almeno il 20%, come disciplinato dall’allegato III del D.M. 4.8.2011; ',
            'trailed_art16_bis_c': 'Interventi “trainati” per l’eliminazione di barriere architettoniche di cui all’art. 16-bis c. 1 lett. e) del TUIR, anche ove effettuati in favore di persone con più di 65 anni ai sensi dell’art. 119, c. 2, D.L. 34/2020;',
            'trailed_art119_c': 'Interventi “trainati” di installazione di impianti solari fotovoltaici con, contestuale o successiva installazione di, sistemi di accumulo, ai sensi dell’art. 119, c. 5 e c. 6, D.L. 34/2020;',
            'towed_art119_c': 'Interventi “trainati” di installazione di colonnine di ricarica di veicoli elettrici, ai sensi dell’art. 119, c. 8, D.L. 34/2020',
            'description': "DESCRIZIONE SINTETICA DELL'INTERVENTO",
        }
        widgets = {
            'description': Textarea(attrs={
                'class': 'ml-0',
                'id': 'description'
            }),
        }


class InterventionsCondoForm(ModelForm):
    class Meta:
        model = Interventions
        exclude = ['id']
        labels = {
            'art119_c1_a': 'Intervento “trainante” ai sensi dell’art. 119 c. 1 lett a), D.L. 34/2020: intervento di “isolamento termico” (con materiali isolanti che rispettano i “CAM” del D.M. dell’Ambiente del 11/10/2017) delle superfici opache verticali (pareti isolanti o cappotti, anche sulla superficie intera delle pareti), orizzontali (pavimenti e coperture) e inclinate (falde di copertura del sottotetto), che interessa l’involucro dell’Immobile, con un’incidenza superiore al 25% della superficie disperdente lorda;',
            'art119_c1_b': ' Intervento “trainante” ai sensi dell’art. 119 c. 1 lett. b), D.L. 34/2020 per la “sostituzione degli impianti di climatizzazione invernale” esistenti nell’Immobile con (i) impianti per il riscaldamento, il raffrescamento o la fornitura di acqua calda sanitaria, a condensazione, con efficienza almeno pari alla classe A (regolamento UE n. 811/2013), a pompa di calore, ivi compresi gli impianti ibridi o geotermici ovvero con impianti di microcogenerazione, a collettori solari; (ii) allaccio a sistemi di teleriscaldamento efficiente (art. 2, c. 2, lett. tt), D.Lgs. 102/2014), solo nelle aree non metanizzate nei comuni montani non interessati dalle procedure europee di infrazione n. 2014/2147 o 2015/2043',
            'art119c_4': "Intervento “trainante” ai sensi dell’art. 119 c. 4, D.L. 34/2020 per la realizzazione di misure antisismiche dell'articolo 16, commi da 1-bis a 1-septies, D.L. 63/2013.",
            'art1_c345': 'art. 1, co. 345, L. 296/2006 per la realizzazione di strutture opache verticali (pareti) ed orizzontali (coperture e pavimenti);',
            'art1_c345_art14': 'art. 1, co. 345, L. 296/2006 e art. 14, D.L. 63/2013 per la installazione di finestre comprensive di infissi delimitanti il volume riscaldato verso l’esterno ovvero vani non riscaldati, con i requisiti di trasmittanza termica di legge;',
            'art1_c346': 'art. 1, co. 346, L. 296/2006 per l’installazione di pannelli solari per la produzione di acqua calda;',
            'art1_c286': 'art. 1, co. 286, L. 244/2007 per la sostituzione di impianti di climatizzazione invernale con caldaie dotate di pompe di calore ad alta efficienza o impianti geotermici a bassa entalpia;',
            'art14_2_1': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013',
            'art14_2_1_B': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013 e contestuale installazione di sistemi di termoregolazione di cui alle classi V, VI o VIII della Comunicazione della Commissione 2014/C 207/02',
            'art14_2_1_C': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con apparecchi ibridi, costituiti da pompa di calore integrata con caldaia a condensazione, assemblati in fabbrica per funzionare in abbinamento tra loro;',
            'art4_c4': 'art. 4, co. 4, D.L. 201/2011 per la sostituzione di scaldacqua tradizionali con scaldacqua a pompa di calore per la produzione di acqua calda sanitaria che rispettino i valori fissati dalle relative tabelle vigenti,',
            'art1_c88': 'art. 1, co. 88, L. 208/2015 per l’acquisto ed installazione di dispositivi multimediali per il controllo da remoto degli impianti di riscaldamento o produzione di acqua calda o di climatizzazione delle unità abitative;',
            'art14_c2': 'art. 14, co. 2 lett b) del D.L. 63/2013 per l’acquisto ed installazione di schermature solari di cui all’allegato M), D.Lgs. 311/2006;',
            'art14_c2_bis': 'art. 14, co. 2-bis, D.L. 63/2013 par l’acquisto ed installazione di impianti di climatizzazione invernale con impianti dotati di generatori di calore alimentati da biomasse combustibili;',
            'art14_c2_b_bis': 'art. 14, co. 2, lett. b-bis) D.L. 63/2013 per l’acquisto ed installazione di micro-cogeneratori che permettano un risparmio di energia primaria (PES) di almeno il 20%, come disciplinato dall’allegato III del D.M. 4.8.2011; ',
            'trailed_art16_bis_c': 'Interventi “trainati” per l’eliminazione di barriere architettoniche di cui all’art. 16-bis c. 1 lett. e) del TUIR, anche ove effettuati in favore di persone con più di 65 anni ai sensi dell’art. 119, c. 2, D.L. 34/2020;',
            'trailed_art119_c': 'Interventi “trainati” di installazione di impianti solari fotovoltaici con, contestuale o successiva installazione di, sistemi di accumulo, ai sensi dell’art. 119, c. 5 e c. 6, D.L. 34/2020;',
            'towed_art119_c': 'Interventi “trainati” di installazione di colonnine di ricarica di veicoli elettrici, ai sensi dell’art. 119, c. 8, D.L. 34/2020',
            'description': "DESCRIZIONE SINTETICA DELL'INTERVENTO",
        }
        widgets = {
            'description': Textarea(attrs={
                'class': 'ml-0',
                'id': 'description'
            }),
            'date_of_assembly': DateInput(attrs={
                'class': 'form-control',
                'id': 'date_of_assembly',
                'type': 'date'
            })
        }


class CatastalDataForm(ModelForm):
    class Meta:
        model = CatastalData
        exclude = ['id']


class OverallInterCostsNOVatForm(ModelForm):
    class Meta:
        model = OverallInterCostsNOVat
        exclude = ['id']


class InterDrivingWorkNOVatForm(ModelForm):
    class Meta:
        model = InterDrivingWorkNOVat
        exclude = ['id']


class InterTrailedWorkNOVatForm(ModelForm):
    class Meta:
        model = InterTrailedWorkNOVat
        exclude = ['id']


class CommonWorkNOVatForm(ModelForm):
    class Meta:
        model = CommonWorkNOVat
        exclude = ['id']


class SubjectiveWorkNOVatForm(ModelForm):
    class Meta:
        model = SubjectiveWorkNOVat
        exclude = ['id']


class BonusCondoForm(ModelForm):
    class Meta:
        model = BonusCondo
        exclude = ['id', 'beneficiary', 'catastal', 'professionals', 'interventions', 'overall_interventions',
                   'common_interventions', 'subjective_interventions', 'admin_legal', 'admin_individual']\



class AdministrationIndividualForm(ModelForm):
    class Meta:
        model = AdministrationIndividual
        exclude = ['id']
        widgets = {
            'dob': DateInput(attrs={
                'class': 'form-control',
                'id': 'dob',
                'type': 'date'
            })
        }

class AdministrationLegalForm(ModelForm):
    class Meta:
        model = AdministrationLegal
        exclude = ['id']
