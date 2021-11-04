from django.db import models
from django.db.models import manager
from internationalflavor.vat_number.models import VATNumberField

# Create your models here.


class DataDesignerIndividual(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=120)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    birthplace = models.CharField(max_length=30)
    birthplace_county = models.CharField(max_length=30)
    residence_street = models.CharField(max_length=50)
    residence_cap = models.IntegerField(blank=False)
    residence_city = models.CharField(max_length=50)
    residence_province = models.CharField(max_length=50)
    activity_street = models.CharField(max_length=50)
    activity_municipality = models.CharField(max_length=50)
    province_head_office = models.CharField(max_length=50)
    cap_headquarters = models.CharField(max_length=50)
    board_order_registration = models.CharField(max_length=50)
    province_college = models.CharField(max_length=40)
    province_college_registration_order = models.IntegerField(blank=False)
    vat_number = VATNumberField(countries=['IT', 'NL'])
    fiscal_code = models.CharField(max_length=16)
    phone_number = models.IntegerField(max_length=16)
    security_case_technician = models.IntegerField(blank=False)

    class Meta:
        managed = True

class DataDesignerLegal(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    municipal_reg_office = models.CharField(max_length=20)
    province_reg_office = models.CharField(max_length=20)
    cap_reg_office = models.CharField(max_length=20)
    street_reg_office = models.CharField(max_length=100)
    province_of_registration = models.CharField(max_length=20)
    company_registration_number = VATNumberField(countries=['IT', 'NL'])
    leg_rep_name = models.CharField(max_length=100)
    leg_dob = models.DateField(auto_now=False, auto_now_add=False)
    leg_dob_municipality = models.CharField(max_length=50)
    leg_dob_province = models.CharField(max_length=50)
    rep_residence_zip = models.CharField(max_length=30)
    rep_street = models.CharField(max_length=100)
    rep_tax_code = models.CharField(max_length=20)
    rep_phone_number = models.IntegerField(blank=False)
    ss_fund = models.IntegerField(blank=False)

    class Meta:
        managed = True

class DataSecurityCoordinatorIndividual(DataDesignerIndividual):
    class Meta:
        managed = True

class DataSecurityCoordinatorLegal(DataDesignerLegal):
    class Meta:
        managed = True

class DataSecurityCoordinatorExecutionIndividual(DataDesignerIndividual):
    class Meta: 
        managed = True

class DataSecurityCoordinatorExecutionLegal(DataDesignerLegal):
    class Meta: 
        managed = True

class DataDirectorWorksIndividual(DataDesignerIndividual):
    class Meta: 
        managed = True

class DataDirectorWorksLegal(DataDesignerLegal):
    class Meta: 
        managed = True

class DataThermoTechnicalIndividual(DataDesignerIndividual):
    class Meta: 
        managed = True

class DataThermoTechnicalLegal(DataDesignerLegal):
    class Meta: 
        managed = True

class DataEnergyExpertIndividual(DataDesignerIndividual):
    class Meta:
        managed = True

class DataEnergyExpertLegal(DataDesignerLegal):
    class Meta:
        managed = True

class DataResponsibleForWorksIndividual(DataDesignerIndividual):
    class Meta:
        managed = True

class DataResponsibleForWorksLegal(DataDesignerLegal):
    class Meta:
        managed = True
