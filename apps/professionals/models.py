from django.db import models
from django.db.models import manager
from django.forms import widgets
from django.forms.models import ModelForm
from internationalflavor.vat_number.models import VATNumberField
from django.forms.widgets import EmailInput, TextInput, Select, NumberInput, DateInput, Textarea
from phone_field import PhoneField

from apps.app.views import individual

# Create your models here.
individual_labels = {
    'title': 'TITOLO',
    'name': 'NOME E COGNOME',
    'dob': 'DATA DI NASCITA',
    'birthplace': 'LUOGO DI NASCITA',
    'birthplace_county': 'PROVINCIA DI NASCITA',
    'residence_street': 'VIA E NUMERO RESIDENZA',
    'residence_cap': 'CAP RESIDENZA',
    'residence_city': 'LUOGO DI RESIDENZA',
    'residence_province': 'PROVINCIA DI RESIDENZA',
    'activity_street': 'VIA E NUMERO/I SEDE ATTIVITA',
    'acitivity_cap':'CAP SEDE ATTIVITA',
    'activity_municipality': 'COMUNE SEDE ATTIVITA',
    'activity_province':'PROVINCIA SEDE ATTIVITA',
    'province_head_office': 'PROVINCIA DELLA SEDE CENTRALE ',
    'cap_headquarters': 'CAP SEDE CENTRALE',
    'board_order_registration': "REGISTRAZIONE DELL'ORDINE DI BORDO",
    'province_college': 'COLLEGIO PROVINCIALE',
    'province_college_registration_order': "ORDINE DI ISCRIZIONE ALL'UNIVERSITÀ DELLA PROVINCIA",
    'vat_number': 'PARTITA IVA',
    'fiscal_code': 'CODICE FISCALE',
    'phone_number': 'TELEFONO',
    'security_case_technician': 'TECNICO DEL CASO DI SICUREZZA '
}

legal_labels = {
    'company_name':'DENOMINAZIONE SOCIETA',
    'municipal_reg_office':'COMUNE SEDE LEGALE',
    'province_reg_office':'PROVINCIA SEDE LEGALE',
    'cap_reg_office':'CAP',
    'street_reg_office':'VIA E NUMERO SEDE LEGALE',
    'province_of_registration':'PROVINCIA DI REGISTRAZIONE SEDE LEGALE',
    'company_registration_number':'',
    'rep_name':'COGNOME E NOME LEGALE RAPPRESENTANTE',
    'rep_dob':'DATA DI NASCITA LEGALE RAPPRESENTANTE',
    'rep_dob_municipality':'COMUNE DE RAPPRESENTANTE',
    'rep_dob_province':'PROVINCIA DE RAPPRESENTANTE',
    'rep_residence_zip':'CODICE POSTALE DEL RAPPRESENTANTE',
    'rep_street':'VIA E NUMERO SEDE RAPPRESENTANTE',
    'rep_tax_code':'CODICE FISCALE DEL RAPPRESENTANTE ',
    'rep_phone_number':'TELEFONO DEL RAPPRESENTANTE ',
    'ss_fund':''
}

individual_widgets = {
    'title': TextInput(attrs={
        'class':'form-control',
        'id': 'title'
    }),
    'name': TextInput(attrs={
        'class':'form-control',
        'id':'name'
    }),
    'dob': DateInput(attrs={
        'class':'form-control',
        'id':'dob'
    }),
    'birthplace': TextInput(attrs={
        'class':'form-control',
        'id':'birthplace'
    }),
    'birthplace_county': TextInput(attrs={
        'class':'form-control',
        'id':'birthplace_county'
    }),
    'residence_street': TextInput(attrs={
        'class':'form-control',
        'id':'residence_street'
    }),
    'residence_cap': TextInput(attrs={
        'class':'form-control',
        'id':'residence_cap'
    }),
    'residence_city': TextInput(attrs={
        'class':'form-control',
        'id':'residence_city'
    }),
    'residence_province': TextInput(attrs={
        'class':'form-control',
        'id':'residence_province'
    }),
    'activity_street': TextInput(attrs={
        'class':'form-control',
        'id':'activity_street'
    }),
    'activity_municipality': TextInput(attrs={
        'class':'form-control',
        'id':'activity_municipality'
    }),
    'province_head_office': TextInput(attrs={
        'class':'form-control',
        'id':'province_head_office'
    }),
    'cap_headquarters': NumberInput(attrs={
        'class':'form-control',
        'id':'cap_headquarters'
    }),
    'board_order_registration': TextInput(attrs={
        'class':'form-control',
        'id':'board_order_registration'
    }),
    'province_college': TextInput(attrs={
        'class':'form-control',
        'id':'province_college'
    }),
    'province_college_registration_order': TextInput(attrs={
        'class':'form-control',
        'id':'province_college_registration_order'
    }),
    'vat_number': TextInput(attrs={
        'class':'form-control',
        'id':'vat_number'
    }),
    'fiscal_code': NumberInput(attrs={
        'class':'form-control',
        'id':'fiscal_code'
    }),
    'phone_number': TextInput(attrs={
        'class':'form-control',
        'id':'phone_number'
    }),
    'security_case_technician': TextInput(attrs={
        'class':'form-control',
        'id':'security_case_technician'
    })
}

legal_widgets = {
    'company_name': TextInput(attrs={
        'class':'form-control',
        'id': 'company_name'
    }),
    'municipal_reg_office':TextInput(attrs={
        'class':'form-control',
        'id':'municipal_reg_office'
    }),
    'province_reg_office': TextInput(attrs={
        'class':'form-control',
        'id': 'province_reg_office'
    }),
    'cap_reg_office': NumberInput(attrs={
        'class':'form-control',
        'id': 'cap_reg_office'
    }),
    'street_reg_office': TextInput(attrs={
        'class':'form-control',
        'id': 'street_reg_office'
    }),
    'province_of_registration': TextInput(attrs={
        'class':'form-control',
        'id': 'province_of_registration'
    }),
    'company_registration_number': TextInput(attrs={
        'class':'form-control',
        'id': 'company_registration_number'
    }),
    'rep_name': TextInput(attrs={
        'class':'form-control',
        'id': 'leg_rep_name'
    }),
    'rep_dob': TextInput(attrs={
        'class':'form-control',
        'id': 'leg_dob'
    }),
    'rep_dob_municipality': TextInput(attrs={
        'class':'form-control',
        'id': 'leg_dob_municipality'
    }),
    'rep_dob_province': TextInput(attrs={
        'class':'form-control',
        'id': 'leg_dob_province'
    }),
    'rep_name': TextInput(attrs={
        'class':'form-control',
        'id': 'leg_rep_name'
    }),
    'rep_residence_zip': TextInput(attrs={
        'class':'form-control',
        'id': 'leg_rep_name'
    }),
    'rep_street': TextInput(attrs={
        'class':'form-control',
        'id': 'rep_street'
    }),
    'rep_residence_zip': TextInput(attrs={
        'class':'form-control',
        'id': 'leg_rep_zip'
    }),
    'rep_tax_code': TextInput(attrs={
        'class':'form-control',
        'id': 'rep_tax_code'
    }),
    'rep_phone_number': TextInput(attrs={
        'class':'form-control',
        'id': 'rep_phone_number'
    }),
    'ss_fund': TextInput(attrs={
        'class':'form-control',
        'id': 'ss_fund'
    })
}

"""Check type for phone number"""
"""Check type for registration"""
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
    activity_cap = models.IntegerField(blank=False)
    activity_municipality = models.CharField(max_length=50)
    activity_province = models.CharField(max_length=50)
    province_head_office = models.CharField(max_length=50)
    cap_headquarters = models.CharField(max_length=50)
    board_order_registration = models.CharField(max_length=50)
    province_college = models.CharField(max_length=40)
    province_college_registration_order = models.IntegerField(blank=False)
    vat_number = VATNumberField(countries=['IT', 'NL'])
    fiscal_code = models.IntegerField(blank=False)
    phone_number = PhoneField(blank=False)
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
    rep_name = models.CharField(max_length=100)
    rep_dob = models.DateField(auto_now=False, auto_now_add=False)
    rep_dob_municipality = models.CharField(max_length=50)
    rep_dob_province = models.CharField(max_length=50)
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

#Forms
class DataDesignerIndividualForm(ModelForm):
    class Meta:
        model = DataDesignerIndividual
        exclude = ['id']
        labels = individual_labels
        widgets = individual_widgets

class DataDesignerLegalForm(ModelForm):
    class Meta:
        model = DataDesignerLegal
        exclude = ['id']
        labels = legal_labels
        widgets = legal_widgets

class DataSecurityCoordinatorIndividualForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorIndividual
        exclude = ['id']
        labels =  individual_labels
        widgets = legal_widgets

class DataSecurityCoordinatorLegalForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorLegal
        exclude = ['id']
        labels = legal_labels
        widgets = legal_widgets

class DataSecurityCoordinatorExecutionIndividualForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorExecutionIndividual
        exclude = ['id']
        labels =  individual_labels
        widgets = legal_widgets

class DataSecurityCoordinatorExecutionLegalForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorExecutionLegal
        exclude = ['id']
        labels =  legal_labels
        widgets = legal_widgets

class DataDirectorWorksIndividualForm(ModelForm):
    class Meta:
        model = DataDirectorWorksIndividual
        exclude = ['id']
        labels =  individual_labels
        widgets = legal_widgets

class DataDirectorWorksLegalForm(ModelForm):
    class Meta:
        model = DataDirectorWorksLegal
        exclude = ['id']
        labels =  legal_labels
        widgets = legal_widgets

class DataThermoTechnicalIndividualForm(ModelForm):
    class Meta:
        model = DataThermoTechnicalIndividual
        exclude = ['id']
        labels =  individual_labels
        widgets = legal_widgets

class DataThermoTechnicalLegalForm(ModelForm):
    class Meta:
        model = DataThermoTechnicalLegal
        exclude = ['id']
        labels =  legal_labels
        widgets = legal_widgets

class DataEnergyExpertIndividualForm(ModelForm):
    class Meta:
        model = DataEnergyExpertIndividual
        exclude = ['id']
        labels =  individual_labels
        widgets = legal_widgets

class DataEnergyExpertLegalForm(ModelForm):
    class Meta:
        model = DataEnergyExpertLegal
        exclude = ['id']
        labels =  legal_labels
        widgets = legal_widgets
        
class DataResponsibleForWorksIndividualForm(ModelForm):
    class Meta:
        model = DataResponsibleForWorksIndividual
        exclude = ['id']
        labels =  individual_labels
        widgets = legal_widgets

class DataResponsibleForWorksLegalForm(ModelForm):
    class Meta:
        model = DataResponsibleForWorksLegal
        exclude = ['id']
        labels =  legal_labels
        widgets = legal_widgets