# Generated by Django 3.2.6 on 2021-12-27 10:10

from django.db import migrations, models
import internationalflavor.vat_number.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parcel', models.CharField(max_length=50, verbose_name='PARTICELLA')),
                ('name', models.CharField(max_length=50, verbose_name='COGNOME NOME/RAGIONE O DENOMINAZIONE SOCIALE')),
                ('title', models.CharField(choices=[('PROPRIETARIO', 'PROPRIETARIO'), ('AFFITTUARIO', 'AFFITTUARIO'), ('NUDO PROPRIETARIO', 'NUDO PROPRIETARIO'), ('USUFRUTTUARIO ', 'USUFRUTTUARIO'), ('ALTRO ', 'ALTRO')], max_length=50, verbose_name='TITOLO DI POSSESSO')),
                ('single_ownership_fee', models.CharField(choices=[('1', '1'), ('1/2', '1/2'), ('1/3', '1/3'), ('1/4', '1/4'), ('1/16', '1/16')], max_length=50, verbose_name="QUOTA PROPRIETA' DEL SINGOLO")),
                ('street', models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name="VIA E NUMERO IN CUI SI TROVA L'IMMOBILE")),
                ('total_thousands', models.DecimalField(blank=True, decimal_places=3, max_digits=12, verbose_name='MILLESIMI COMPLESSIVI')),
                ('benef_of_diss_in_invo', models.CharField(blank=True, max_length=50, verbose_name='BENEFICIARI DELLO SCONTO IN FATTURA')),
                ('thousands_benef_diss', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True, verbose_name='MILLESIMI DI BENEFICIO DELLO SCONTO IN FATTURA SU PARTI COMUNI')),
                ('name_of_company', models.CharField(blank=True, max_length=50, verbose_name="DENOMINAZIONE SOCIETA' BENEFICIARIA")),
                ('municipal_reg_office', models.CharField(blank=True, max_length=20, verbose_name="COMUNE  SEDE LEGALE SOCIETA' BENEFICIARIA")),
                ('province_reg_office', models.CharField(blank=True, max_length=20, verbose_name="PROVINCIA  SEDE LEGALE SOCIETA' BENEFICIARIA")),
                ('post_code_cap', models.CharField(blank=True, max_length=20, verbose_name="CAP SEDE LEGALE SOCIETA' BENEFICIARIA")),
                ('company_street', models.CharField(blank=True, max_length=150, verbose_name="VIA E NUMERO SEDE LEGALE SOCIETA' BENEFICIARIA")),
                ('province_reg_comp_office', models.CharField(blank=True, max_length=20, verbose_name="PROVINCIA ISCRIZIONE REGISTRO IMPRESE SOCIETA' BENEFICIARIA")),
                ('vat_number_company', internationalflavor.vat_number.models.VATNumberField(blank=True, countries=['IT'], verbose_name='IVA-C.F')),
                ('name_of_company_representitave', models.CharField(blank=True, max_length=120, verbose_name="COGNOME E NOME LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('dob_of_rep', models.DateField(verbose_name="DATA NASCITA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('muncipality_of_birth_rep', models.CharField(blank=True, max_length=50, verbose_name="COMUNE NASCITA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('province_of_birth_rep', models.CharField(blank=True, max_length=50, verbose_name="PROVINCIA NASCITA LEGALE RAPPRESENTANTE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('muncipality_of_res_rep', models.CharField(blank=True, max_length=50, verbose_name="COMUNE RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('province_of_residance_rep', models.CharField(blank=True, max_length=50, verbose_name="PROVINCIA RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('cap_of_residance_rep', models.CharField(blank=True, max_length=50, verbose_name="CAP RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('street_res_of_rep', models.CharField(blank=True, max_length=150, verbose_name="VIA E NUMERO RESIDENZA LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('legal_tax_code_rep', models.CharField(blank=True, max_length=50, verbose_name="CODICE FISCALE LEGALE RAPPRESENTATE SOCIETA' BENEFICIARIA o del BENEFICIARIO PERSONA FISICA")),
                ('amount_advance_deposit_by_customer_common', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True, verbose_name='IMPORTO ACCONTO INTERVENTI COMUNI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA')),
                ('amount_advance_deposit_by_customer_subjective', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='IMPORTO ACCONTO INTERVENTI SOGGETTIVI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA')),
                ('total_adv_deposit_customer', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='IMPORTO COMPLESSIVO ACCONTO - CASSA PREVIDENZA INCLUSA E IVA INCLUSA')),
                ('amount_discount_common', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True, verbose_name='IMPORTO SCONTO IN FATTURA INTERVENTI COMUNI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA')),
                ('amount_discount_subjective', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True, verbose_name='IMPORTO SCONTO IN FATTURA INTERVENTI SOGGETTIVI - CASSA PREVIDENZA INCLUSA E IVA INCLUSA')),
                ('total_discount', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True, verbose_name='IMPORTO COMPLESSIVO SCONTO IN FATTURA - CASSA PREVIDENZA INCLUSA E IVA INCLUSA')),
                ('select_form', models.ManyToManyField(to='app.FormFaccata')),
            ],
        ),
    ]
