from django.db import models
from django.forms import ModelForm
from internationalflavor.vat_number import VATNumberField
from django.forms.widgets import DateInput
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from apps.superbonus.csv_reader import get_cap_list
from django import forms


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



TITLE = [
    ('PROPRIETARIO', 'PROPRIETARIO'),
    ('AFFITTUARIO', 'AFFITTUARIO'),
    ('NUDO PROPRIETARIO', 'NUDO PROPRIETARIO'),
    ('USUFRUTTUARIO ', 'USUFRUTTUARIO'),
    ('ALTRO ', 'ALTRO'),
]
OWNERSHIP = [
    ('1', '1'),
    ('1/2', '1/2'),
    ('1/3', '1/3'),
    ('1/4', '1/4'),
    ('1/5', '1/5'),
    ('1/6', '1/6'),
    ('1/7', '1/7'),
    ('1/8', '1/8'),
]


class Beneficiary(models.Model):
    id = models.AutoField(primary_key=True)
    parcel = models.CharField("PARTICELLA", max_length=50, blank=False)
    name = models.CharField("COGNOME NOME/RAGIONE O DENOMINAZIONE SOCIALE", max_length=50, blank=False)
    title = models.CharField("TITOLO DI POSSESSO", max_length=50, choices=TITLE, blank=False)
    single_ownership_fee = models.CharField("QUOTA PROPRIETA' DEL SINGOLO", choices=OWNERSHIP, max_length=50,
                                            blank=False)
    street = models.CharField("VIA E NUMERO IN CUI SI TROVA L'IMMOBILE", max_length=150, blank=True, null=True,
                              default=0)
    total_thousands = models.DecimalField("MILLESIMI COMPLESSIVI", decimal_places=3, max_digits=12, blank=True)
    benef_of_diss_in_invo = models.CharField("BENEFICIARI DELLO SCONTO IN FATTURA", max_length=50, blank=True)
    thousands_benef_diss = models.DecimalField("MILLESIMI DI BENEFICIO DELLO SCONTO IN FATTURA SU PARTI COMUNI",
                                            decimal_places=3, max_digits=12, null=True, blank=True, default=0)
    name_of_company = models.CharField("DENOMINAZIONE SOCIETA' BENEFICIARIA", max_length=50, blank=True)
    municipal_reg_office = models.CharField("COMUNE  SEDE LEGALE SOCIETA' BENEFICIARIA", max_length=20, blank=True)
    province_reg_office = models.CharField("PROVINCIA  SEDE LEGALE SOCIETA' BENEFICIARIA", max_length=20, blank=True)
    post_code_cap = models.CharField("CAP SEDE LEGALE SOCIETA' BENEFICIARIA", max_length=5, validators=[validate_cap])
    company_street = models.CharField("VIA E NUMERO SEDE LEGALE SOCIETA' BENEFICIARIA", max_length=150, blank=True)
    province_reg_comp_office = models.CharField("PROVINCIA ISCRIZIONE REGISTRO IMPRESE SOCIETA' BENEFICIARIA", max_length=20,
                                           blank=True)
    vat_number_company = VATNumberField(countries=['IT'], blank=True, verbose_name="IVA-C.F")#"N° ISCRIZIONE REGISTRO IMPRESE-PARTITA IVA-C.F.SOCIETA BENEFICIARIA"
    name_of_company_representitave = models.CharField("COGNOME E NOME LEGALE RAPPRESENTATE SOCIETA' "
                                                      "BENEFICIARIA o del BENEFICIARIO PERSONA FISICA", max_length=120,
                                                      blank=True)
    dob_of_rep = models.DateField("DATA NASCITA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                  auto_now=False, auto_now_add=False, default=date.today)
    muncipality_of_birth_rep = models.CharField("COMUNE NASCITA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                                max_length=50, blank=True)
    province_of_birth_rep = models.CharField("PROVINCIA NASCITA LEGALE RAPPRESENTANTE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                             max_length=50, blank=True)
    muncipality_of_res_rep = models.CharField("COMUNE RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                max_length=50, blank=True)
    province_of_residance_rep = models.CharField("PROVINCIA RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                                 max_length=50, blank=True)
    cap_of_residance_rep = models.CharField("CAP RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                            max_length=5, validators=[validate_cap])
    street_res_of_rep = models.CharField("VIA E NUMERO RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                         max_length=150, blank=True)
    legal_tax_code_rep= models.CharField("CODICE FISCALE LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                         max_length=16, blank=True, validators=[validate_fiscal_code])
    amount_advance_deposit_by_customer_common = models.DecimalField("IMPORTO ACCONTO INTERVENTI COMUNI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA",
                                                                    decimal_places=3, max_digits=12, null=True, blank=True, default=0)
    amount_advance_deposit_by_customer_subjective = models.DecimalField("IMPORTO ACCONTO INTERVENTI SOGGETTIVI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA",
                                     decimal_places=2, max_digits=12, null=True, blank=True, default=0)
    total_adv_deposit_customer = models.DecimalField("IMPORTO COMPLESSIVO ACCONTO - CASSA PREVIDENZA INCLUSA E IVA INCLUSA",
                                     decimal_places=2, max_digits=12, null=True, blank=True, default=0)
    amount_discount_common = models.DecimalField("IMPORTO SCONTO IN FATTURA INTERVENTI COMUNI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA",
                                                                        decimal_places=3, max_digits=12, null=True, blank=True, default=0)
    amount_discount_subjective = models.DecimalField("IMPORTO SCONTO IN FATTURA INTERVENTI SOGGETTIVI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA",
                                                                        decimal_places=3, max_digits=12, null=True, blank=True, default=0)
    total_discount = models.DecimalField("IMPORTO COMPLESSIVO SCONTO IN FATTURA - CASSA PREVIDENZA INCLUSA E IVA INCLUSA",
                                                   decimal_places=3, max_digits=12, null=True, blank=True, default=0)
    select_form = models.ManyToManyField('app.FormFaccata')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.total_adv_deposit_customer = self. amount_advance_deposit_by_customer_common + \
                                          self.amount_advance_deposit_by_customer_subjective
        self.total_discount = self.amount_discount_subjective + self.amount_discount_common
        super().save(*args, **kwargs)






class BeneficiaryForm(ModelForm):
    class Meta:
        model = Beneficiary
        exclude = ['id', 'select_form']
        labels = {
            'vat_number_company': 'N° ISCRIZIONE REGISTRO IMPRESE-PARTITA IVA-C.F.SOCIETA BENEFICIARIA',
            'select_form': 'SELEZIONA LA FORMA DI CONDOMINIO RELATIVA AL BENEFICIARIO'
            }
        widgets ={
            'dob_of_rep': DateInput(attrs={
                'class': 'form-control',
                'id': 'dob_of_rep',
                'type': 'date'
            }),
        }
        error_messages = {
            'vat_number_company': {
                'invalid': ("Il numero di partita IVA dovrebbe iniziare con IT seguito da undici cifre"),
            },

        }

    def clean_dob_of_rep(self):
        d = self.cleaned_data['dob_of_rep']
        if d > date.date.today():
            raise forms.ValidationError("La data futura non è valida")
        return d
