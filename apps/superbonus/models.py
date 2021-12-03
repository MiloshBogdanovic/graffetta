from django.db import models
from apps.beneficary.models import Beneficiary, BeneficiaryForm
from apps.professionals.models import Prof_table
from decimal import Decimal
# Create your models here.

YN = [
    ('NO', 'NO'),
    ('SI', 'SI')
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


class InterventionCost(models.Model):
    id = models.AutoField(primary_key=True)
    total_amt_of_work = models.DecimalField("IMPORTO COMPLESSIVO DEI LAVORI DA ESEGUIRE", decimal_places=2, max_digits=12, default=0, null=True)
    total_amt_safety_charges = models.DecimalField("IMPORTO COMPLESSIVO ONERI SICUREZZA ", decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_designer = models.DecimalField("SPESE TECNICHE PROGETTISTA ", decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_coordinator_safety_des = models.DecimalField("SPESE TECNICHE COORDINATORE SICUREZZA PROGETTAZIONE", decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_coordinator_safety_exe = models.DecimalField("SPESE TECNICHE COORDINATORE SICUREZZA ESECUZIONE", decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_director_of_work = models.DecimalField("SPESE TECNICHE DIRETTORE LAVORI", decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_thermotechnical = models.DecimalField("SPESE TECNICHE TERMOTECNICO", decimal_places=2, max_digits=12, default=0, null=True)
    tech_exp_energy_expert = models.DecimalField("SPESE TECNICHE ESPERTO ENERGETICO", decimal_places=2, max_digits=12, default=0, null=True)
    poss_respo_work = models.DecimalField("EVENTUALE RESPONSABILE DEI LAVORI", decimal_places=2, max_digits=12, default=0, null=True)
    app_for_conformity_visa = models.DecimalField("APPOSIZIONE VISTO DI CONFORMTA'", decimal_places=2, max_digits=12, default=0, null=True)
    total_tech_exp = models.DecimalField("TOTALE TECNICHE", decimal_places=2, max_digits=12, default=0, null=True)
    total_of_the_order = models.DecimalField("TOTALE DELLA COMMESSA", decimal_places=2, max_digits=12, default=0, null=True)

    class Meta:
        abstract = True


class OverallInterCostsNOVat(InterventionCost):
    vat_for_total_work = models.DecimalField("IMPORTO COMPLESSIVO IVA DA APPLICARE", decimal_places=2, max_digits=10, default=Decimal('0.22'), blank=False,
                                             choices=VTA_CHOICE)
    ss_cash_for_designer = models.DecimalField("CASSA PREVIDENZA PROGETTISTA", decimal_places=2, max_digits=10, default=Decimal('0.04'), blank=False,
                                               choices=CASSA_CHOICE)
    ss_cash_for_coordinator_safety_des = models.DecimalField("CASSA PREVIDENZA COORDINATORE SICUREZZA PROGETTAZIONE", decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                             blank=False, choices=CASSA_CHOICE)
    ss_cash_for_coordinator_safety_exe = models.DecimalField("CASSA PREVIDENZA COORDINATORE SICUREZZA ESECUZIONE", decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                             blank=False, choices=CASSA_CHOICE)
    ss_cash_for_director_of_work = models.DecimalField("CASSA PREVIDENZA DIRETTORE LAVORI", decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                       blank=False, choices=CASSA_CHOICE)
    ss_cash_for_thermotechnical = models.DecimalField("CASSA PREVIDENZA TECNICHE TERMOTECNICO", decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                      blank=False, choices=CASSA_CHOICE)
    ss_cash_for_energy_expert = models.DecimalField("CASSA PREVIDENZA ESPERTO ENERGETICO", decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                    blank=False, choices=CASSA_CHOICE)
    ss_cash_for_respo_work = models.DecimalField("CASSA PREVIDENZA RESPONSABILE DEI LAVORI", decimal_places=2, max_digits=10, default=Decimal('0.04'),
                                                 blank=False, choices=CASSA_CHOICE)
    ss_app_for_conformity_visa = models.DecimalField("CASSA PREVIDENZA ", decimal_places=2, max_digits=10, default=Decimal('0.0'),
                                                 blank=False, choices=CASSA_CHOICE)


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
    #Driving inteventions
    art119_c1_a = models.CharField(max_length=2, choices=YN)
    art119_c1_b = models.CharField(max_length=2, choices=YN)
    art119c_4 = models.CharField(max_length=2, choices=YN)
    #Towed inteventions
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


class OverallInterventions(models.Model):
    id = models.AutoField(primary_key=True)


class BonusVilla(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("DENOMINAZIONE DELL'IMMOBILE", max_length=50, blank=False)
    street = models.CharField("VIA E NUMERO/I UBICAZIONE  DELL'IMMOBILE", max_length=50, blank=False)
    cap = models.IntegerField("CAP UBICAZIONE DELL'IMMOBILE", blank=False)
    municipality = models.CharField("COMUNE UBICAZIONE DELL'IMMOBILE", max_length=50, blank=False)
    province = models.CharField("PROVINCIA UBICAZIONE DELL'IMMOBILE", max_length=10, blank=False)
    email = models.EmailField("INDIRIZZO MAIL DELL'IMMOBILE - DEL CLIENTE", max_length=254, blank=False)
    pec_mail = models.EmailField("INDIRIZZO PEC DELL'IMMOBILE - DEL CLIENTE", max_length=254, blank=False)
    catastal = models.ForeignKey(CatastalData, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="DATI CATASTALI")
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name="INTERVENTI")
    professionals = models.ForeignKey(Prof_table, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="PROFESSIONALI")
    interventions = models.ForeignKey(Interventions, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="INTERVENTI")
    overall_interventions = models.ForeignKey(OverallInterventions, on_delete=models.SET_NULL, blank=True, null=True,
                                              verbose_name="COMPLESSIVA DELL'INTERVENTO")


class BonusCondo(models.Model):
    id = models.AutoField(primary_key=True)


class SuperBonus(models.Model):
    id = models.AutoField(primary_key=True)
    bonus_villa = models.ForeignKey(BonusVilla, on_delete=models.CASCADE, blank=True, null=True)
    bonus_condo = models.ForeignKey(BonusCondo, on_delete=models.CASCADE, blank=True, null=True)