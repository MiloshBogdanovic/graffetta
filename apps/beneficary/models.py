from django.db import models
from django.forms import ModelForm
from apps.app.models import FormFaccata
from internationalflavor.vat_number import VATNumberField
from django.forms.widgets import DateInput

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
    ('1/16', '1/16'),
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
    post_code_cap = models.CharField("CAP SEDE LEGALE SOCIETA' BENEFICIARIA", max_length=20, blank=True)
    company_street = models.CharField("VIA E NUMERO SEDE LEGALE SOCIETA' BENEFICIARIA", max_length=150, blank=True)
    province_reg_comp_office = models.CharField("PROVINCIA ISCRIZIONE REGISTRO IMPRESE SOCIETA' BENEFICIARIA", max_length=20,
                                           blank=True)
    vat_number_company = VATNumberField(countries=['IT'], blank=True, verbose_name="IVA-C.F")#"N° ISCRIZIONE REGISTRO IMPRESE-PARTITA IVA-C.F.SOCIETA BENEFICIARIA"
    name_of_company_representitave = models.CharField("COGNOME E NOME LEGALE RAPPRESENTATE SOCIETA' "
                                                      "BENEFICIARIA o del BENEFICIARIO PERSONA FISICA", max_length=120,
                                                      blank=True)
    dob_of_rep = models.DateField("DATA NASCITA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                  auto_now=False, auto_now_add=False)
    muncipality_of_birth_rep = models.CharField("COMUNE NASCITA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                                max_length=50, blank=True)
    province_of_birth_rep = models.CharField("PROVINCIA NASCITA LEGALE RAPPRESENTANTE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                             max_length=50, blank=True)
    muncipality_of_res_rep = models.CharField("COMUNE RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                max_length=50, blank=True)
    province_of_residance_rep = models.CharField("PROVINCIA RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                                 max_length=50, blank=True)
    cap_of_residance_rep = models.CharField("CAP RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                            max_length=50, blank=True)
    street_res_of_rep = models.CharField("VIA E NUMERO RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                         max_length=150, blank=True)
    legal_tax_code_rep= models.CharField("CODICE FISCALE LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA",
                                         max_length=50, blank=True)
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
    select_form = models.ManyToManyField(FormFaccata)

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

