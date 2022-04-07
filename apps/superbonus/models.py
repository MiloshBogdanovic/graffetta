import os
from apps.beneficary.models import Beneficiary
from apps.professionals.models import *
from decimal import Decimal
from django.forms import ModelForm
from django.forms.widgets import Textarea, DateInput
from internationalflavor.vat_number import VATNumberField
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from .csv_reader import get_cap_list


YN = [
    ('NO', 'NO'),
    ('SI', 'SI')
]

STATUS_CHOICE = [
    ('UPLOADED', 'CARICATO'),
    ('VERIFIED', 'VERIFICATO'),
    ('AUTHORISED', 'AUTORIZZATO')
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


def positive_num_validator(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s Assicurarsi che questo valore sia maggiore o uguale a 0.'),
            params={'value': value},
        )

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Estensione file non supportata.')


def validate_cap(value):
    if not re.match(r'^([\s\d]{5})$', value):
        raise ValidationError(
            _('%(value)s non è un numero massimo di 5 cifre'),
            params={'value': value},
        )
    elif value not in get_cap_list():
        raise ValidationError(
            _('%(value)s non è un numero di cap valido'),
            params={'value': value},
        )


def validate_fiscal_code(value):
    if not re.match(r'^[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}$', value):
        raise ValidationError(
            _('%(value)s valore inserito non è codice fiscale valido'),
            params={'value': value},
        )


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.name, filename)


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
    fiscal_code = models.CharField('CODICE FISCALE', max_length=16, blank=True, validators=[validate_fiscal_code])
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
    leg_rep_tax_code = models.CharField('CODICE FISCALE LEGALE RAPPRESENTATE', max_length=16, blank=True, validators=[validate_fiscal_code])
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
    n_catastal_cheet = models.IntegerField("N° FOGLIO CATASTALE DI APPARTENENZA", blank=False, validators=[positive_num_validator])
    n_first_particle = models.IntegerField("N° PRIMA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=False, validators=[positive_num_validator])
    n_subscribers_to_first_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA PRIMA PARTICELLA", max_length=20,
                                                        blank=False)
    n_second_particle = models.IntegerField("N° SECONDA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True,
                                            validators=[positive_num_validator])
    n_subscribers_to_second_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA SECONDA PARTICELLA",
                                                         max_length=20, blank=True, null=True)
    n_third_particle = models.IntegerField("N° TERZA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True,
                                           validators=[positive_num_validator])
    n_subscribers_to_third_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA TERZA PARTICELLA", max_length=20,
                                                        blank=True, null=True)
    n_fourth_particle = models.IntegerField("N° QUARTA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True,
                                            validators=[positive_num_validator])
    n_subscribers_to_fourth_belonging = models.CharField("N° SUBALTERNI APPARTENTI ALLA QUARTA PARTICELLA",
                                                         max_length=20, blank=True, null=True)
    n_fifth_particle = models.IntegerField("N° QUINTA PARTICELLA COSTITUENTE IL CONDOMINIO", blank=True, null=True,
                                           validators=[positive_num_validator])
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


class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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
    beneficiary = models.ManyToManyField(Beneficiary, verbose_name="DETTAGLIO DEI BENEFICIARI")
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
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, null=True,
                                              verbose_name="ISTITUTO DI CREDITO")


class BonusCondo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("DENOMINAZIONE CONDOMINIO", max_length=50, blank=False)
    fiscal_code = models.CharField("CODICE FISCALE", max_length=16, blank=True, validators=[validate_fiscal_code])
    street = models.CharField("CONDOMINIO VIA E NUMERO/I UBICAZIONE", max_length=50, blank=False)
    cap = models.CharField("CAP UBICAZIONE CONDOMINIO - IMMOBILE", max_length=5, validators=[validate_cap])
    common_location = models.CharField("COMUNE UBICAZIONE CONDOMINIO - IMMOBILE", max_length=50, blank=True)
    province = models.CharField("CONDOMINIO - IMMOBILE PROVINCIA UBICAZIONE ", max_length=10, blank=True)
    email = models.EmailField("CONDOMINIO - IMMOBILE INDIRIZZO MAIL DEL", max_length=54, blank=False)
    pec_mail = models.EmailField("CONDOMINIO INDIRIZZO PEC DEL CONDOMINIO", max_length=54, blank=False)
    catastal = models.ForeignKey(CatastalData, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="DATI CATASTALI")
    beneficiary = models.ManyToManyField(Beneficiary, verbose_name="DETTAGLIO DEI BENEFICIARI")
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
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, null=True,
                                              verbose_name="ISTITUTO DI CREDITO")


class SuperBonus(models.Model):
    id = models.AutoField(primary_key=True)
    bonus_villa = models.ForeignKey(BonusVilla, on_delete=models.CASCADE, blank=True, null=True)
    bonus_condo = models.ForeignKey(BonusCondo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Superbonus'


class FileRequired(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to=user_directory_path)  # to add uplaod to option for specific bank or

    def __str__(self):
        return self.name


class StatusFile(models.Model):
    file = models.OneToOneField(FileRequired, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='UPLOADED')

    def __str__(self):
        return self.status


class BankRequirements(models.Model):
    id = models.AutoField(primary_key=True)
    bonus = models.ForeignKey(SuperBonus, on_delete=models.CASCADE)
    admin_id = models.ManyToManyField(FileRequired, related_name='aid')
    admin_hi = models.ManyToManyField(FileRequired, related_name='ahi')
    cond_reg = models.ManyToManyField(FileRequired, related_name='creg')
    cond_tax = models.ManyToManyField(FileRequired, related_name='ctax')
    cat_plan = models.ManyToManyField(FileRequired, related_name='catp')
    thousand_table = models.ManyToManyField(FileRequired, related_name='tt')
    cond_registry = models.ManyToManyField(FileRequired, related_name='cregi')
    notary_act_a = models.ManyToManyField(FileRequired, related_name='not_act')
    app_of_admin = models.ManyToManyField(FileRequired, related_name='app_addmin')
    notary_act_b = models.ManyToManyField(FileRequired, related_name='not_act_b')
    id_card_condo = models.ManyToManyField(FileRequired, related_name='id_condo')
    hic_condo = models.ManyToManyField(FileRequired, related_name='hic')
    leg_title_proc = models.ManyToManyField(FileRequired, related_name='ltp')
    cons_for_exe = models.ManyToManyField(FileRequired, related_name='cfeow')
    estate_unit_cat_visa = models.ManyToManyField(FileRequired, related_name='reucv')
    deed_of_owner_purch = models.ManyToManyField(FileRequired, related_name='doop')
    cert_poss_real_right_enjoy = models.ManyToManyField(FileRequired, related_name='cprre')
    declaration_con_owner = models.ManyToManyField(FileRequired, related_name='dcbo')
    contract_cert_cor_reg = models.ManyToManyField(FileRequired, related_name='cccr')
    pre_contract_reg = models.ManyToManyField(FileRequired, related_name='pcrpp')
    declar_of_cons_owner = models.ManyToManyField(FileRequired, related_name='docbo')
    contract_cert_corr_reg = models.ManyToManyField(FileRequired, related_name='cccreg')
    pre_cont_reg_place_in_pos = models.ManyToManyField(FileRequired, related_name='pcrpip')
    declaration_of_cons_owner = models.ManyToManyField(FileRequired, related_name='docbo_l')
    cert_of_reg_office = models.ManyToManyField(FileRequired, related_name='coro')
    title_of_possession = models.ManyToManyField(FileRequired, related_name='top')
    dec_of_con_by_owner = models.ManyToManyField(FileRequired, related_name='docbto')
    assignment = models.ManyToManyField(FileRequired,related_name='assi')
    t_of_pos = models.ManyToManyField(FileRequired, related_name='top_spouse')
    dec_of_cons_spouse = models.ManyToManyField(FileRequired, related_name='doc_spouse')
    proc_contract = models.ManyToManyField(FileRequired, related_name='pcontract')
    metric_cal = models.ManyToManyField(FileRequired, related_name='mc')
    presumed_deadline_sal = models.ManyToManyField(FileRequired, related_name='pds')
    sub_contract = models.ManyToManyField(FileRequired, related_name='sub_contract')
    visura_aurica = models.ManyToManyField(FileRequired, related_name='vis_auri')
    ape_ante = models.ManyToManyField(FileRequired, related_name='aa')
    liability_insurance_asseverate = models.ManyToManyField(FileRequired, related_name='lib_ins_ass')
    any_binding_doc = models.ManyToManyField(FileRequired, related_name='abdocs')
    dec_of_con_of_exis_sys = models.ManyToManyField(FileRequired, related_name='docoes')
    dec_of_enroll = models.ManyToManyField(FileRequired, related_name='doer')
    leg_status_statement = models.ManyToManyField(FileRequired, related_name='lsos')
    construction_site_sc = models.ManyToManyField(FileRequired, related_name='cssc')
    lat_building_title = models.ManyToManyField(FileRequired, related_name='lbt')
    tech_prot_ad_ver = models.ManyToManyField(FileRequired, related_name='tpfav')
    tech_pre_feas_study = models.ManyToManyField(FileRequired, related_name='tpvs')
    tax_pre_feas_study = models.ManyToManyField(FileRequired, related_name='tpfs')
    towed_inter_comp_cert = models.ManyToManyField(FileRequired, related_name='ticcco')
    cert_enroll_qto = models.ManyToManyField(FileRequired, related_name='ceqto')
    res_of_cond_meeting = models.ManyToManyField(FileRequired, related_name='rocms')
    sowc_practice = models.ManyToManyField(FileRequired, related_name='sowcp')
    sowc_notification = models.ManyToManyField(FileRequired,related_name='sowcnot')
    copy_invoice = models.ManyToManyField(FileRequired, related_name='copy_invoice')
    doc_cert_fairness = models.ManyToManyField(FileRequired, related_name='dcfoi')
    prof_of_pay = models.ManyToManyField(FileRequired, related_name='pop')

    class Meta:
        Managed: True


