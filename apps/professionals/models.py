from django.db import models
from django.forms.fields import ChoiceField, MultipleChoiceField
from django.forms.forms import Form
from django.forms.models import ModelForm, ModelMultipleChoiceField
from internationalflavor.vat_number.models import VATNumberField
from django.forms.widgets import CheckboxSelectMultiple, EmailInput, TextInput, Select, NumberInput, DateInput, Textarea
from phone_field import PhoneField

SSCT = [
    ('4%', '4%'),
    ('4%', '5%')
]

PROFESSION_CHOICES = [
    ('DATI PROGETTISTA', 'DATI PROGETTISTA'),
    ('DATI COORDINATORE SICUREZZA IN FASE DI PROGETTAZIONE', 'DATI COORDINATORE SICUREZZA IN FASE DI PROGETTAZIONE'),
    ('DATI COORDINATORE SICUREZZA IN FASE DI ESECUZIONE', 'DATI COORDINATORE SICUREZZA IN FASE DI ESECUZIONE'),
    ('DATI DIRETTORE LAVORI', 'DATI DIRETTORE LAVORI'),
    ('DATI TERMOTECNICO', 'DATI TERMOTECNICO'),
    ('DATI ESPERTO ENERGETICO', 'DATI ESPERTO ENERGETICO'),
    ('DATI RESPONSABILE DEI LAVORI', 'DATI RESPONSABILE DEI LAVORI')
]

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
    'activity_cap': 'CAP SEDE ATTIVITA',
    'activity_municipality': 'COMUNE SEDE ATTIVITA',
    'activity_province': 'PROVINCIA SEDE ATTIVITA',
    'board_order_registration': "COLLEGIO/ORDINE - ISCRIZIONE",
    'province_college': 'PROVINCIA COLLEGIO',
    'number_of_reg_order_college': "No ISCRIZIONE",
    'vat_number': 'PARTITA IVA',
    'fiscal_code': 'CODICE FISCALE',
    'phone_number': 'TELEFONO',
    'security_case_technician': 'CASSA DI PREVIDENZA TECNICO',

}

legal_labels = {
    'company_name': 'DENOMINAZIONE SOCIETA',
    'municipal_reg_office': 'COMUNE SEDE LEGALE',
    'province_reg_office': 'PROVINCIA SEDE LEGALE',
    'cap_reg_office': 'CAP SEDE LEGALE',
    'street_reg_office': 'VIA E NUMERO SEDE LEGALE',
    'province_of_inscription_enterprises_register': 'PROVINCIA/E DI ISCRIZIONE REGISTRO IMPRESE',
    'number_of_inscription_enterprises_register': 'No ISCRIZIONE REGISTRO IMPRESE - C.F. - P.IVA',
    'rep_name': 'COGNOME E NOME LEGALE RAPPRESENTANTE',
    'rep_dob': 'DATA DI NASCITA LEGALE RAPPRESENTANTE',
    'rep_dob_municipality': 'COMUNE DI NASCITA LEGALE RAPPRESENTANTE',
    'rep_dob_province': 'PROVINCIA DI NASCITA LEGALE RAPPRESENTANTE',
    'rep_residence_municipality': 'CAP RESIDENZA LEGALE RAPPRESENTANTE',
    'rep_residence_province': "PROVINCIA RESIDENZA LEGALE RAPPRESENTANTE",
    'rep_residence_zip': 'CODICE POSTALE DEL LEGALE RAPPRESENTANTE',
    'rep_street': 'VIA E NUMERO RESIDENZA SEDE RAPPRESENTANTE',
    'rep_fiscal_code': 'CODICE FISCALE DEL RAPPRESENTANTE ',
    'rep_phone_number': 'TELEFONO DEL RAPPRESENTANTE ',
    'ss_fund': "EVENTUALE CASSA DI PREVIDENZA DA APPLICARE ALLA SOCIETA'/STUDIO PROFESSIONALE"
}

individual_widgets = {
    'title': TextInput(attrs={
        'class': 'form-control',
        'id': 'title'
    }),
    'name': TextInput(attrs={
        'class': 'form-control',
        'id': 'name'
    }),
    'dob': DateInput(attrs={
        'class': 'form-control',
        'id': 'dob',
        'type': 'date'
    }),
    'birthplace': TextInput(attrs={
        'class': 'form-control',
        'id': 'birthplace'
    }),
    'birthplace_county': TextInput(attrs={
        'class': 'form-control',
        'id': 'birthplace_county'
    }),
    'residence_street': TextInput(attrs={
        'class': 'form-control',
        'id': 'residence_street'
    }),
    'residence_cap': TextInput(attrs={
        'class': 'form-control',
        'id': 'residence_cap'
    }),
    'residence_city': TextInput(attrs={
        'class': 'form-control',
        'id': 'residence_city'
    }),
    'residence_province': TextInput(attrs={
        'class': 'form-control',
        'id': 'residence_province'
    }),
    'activity_street': TextInput(attrs={
        'class': 'form-control',
        'id': 'activity_street'
    }),
    'activity_cap': TextInput(attrs={
        'class': 'form-control',
        'id': 'activity_cap'
    }),
    'activity_province': TextInput(attrs={
        'class': 'form-control',
        'id': 'activity_province'
    }),
    'activity_municipality': TextInput(attrs={
        'class': 'form-control',
        'id': 'activity_municipality'
    }),
    'province_head_office': TextInput(attrs={
        'class': 'form-control',
        'id': 'province_head_office'
    }),
    'cap_headquarters': NumberInput(attrs={
        'class': 'form-control',
        'id': 'cap_headquarters'
    }),
    'board_order_registration': TextInput(attrs={
        'class': 'form-control',
        'id': 'board_order_registration'
    }),
    'province_college': TextInput(attrs={
        'class': 'form-control',
        'id': 'province_college'
    }),
    'number_description': TextInput(attrs={
        'class': 'form-control',
        'id': 'number_description'
    }),
    'vat_number': TextInput(attrs={
        'class': 'form-control',
        'id': 'vat_number'
    }),
    'fiscal_code': TextInput(attrs={
        'class': 'form-control',
        'id': 'fiscal_code'
    }),
    'phone_number': TextInput(attrs={
        'class': 'form-control',
        'id': 'phone_number'
    }),
    'security_case_technician': Select(attrs={
        'class': 'form-control',
        'id': 'security_case_technician'
    })
}

legal_widgets = {
    'company_name': TextInput(attrs={
        'class': 'form-control',
        'id': 'company_name'
    }),
    'municipal_reg_office': TextInput(attrs={
        'class': 'form-control',
        'id': 'municipal_reg_office'
    }),
    'province_reg_office': TextInput(attrs={
        'class': 'form-control',
        'id': 'province_reg_office'
    }),
    'cap_reg_office': NumberInput(attrs={
        'class': 'form-control',
        'id': 'cap_reg_office'
    }),
    'street_reg_office': TextInput(attrs={
        'class': 'form-control',
        'id': 'street_reg_office'
    }),
    'province_of_registration': TextInput(attrs={
        'class': 'form-control',
        'id': 'province_of_registration'
    }),
    'company_registration_number': TextInput(attrs={
        'class': 'form-control',
        'id': 'company_registration_number'
    }),
    'rep_name': TextInput(attrs={
        'class': 'form-control',
        'id': 'leg_rep_name'
    }),
    'rep_dob': TextInput(attrs={
        'class': 'form-control',
        'id': 'leg_dob',
        'type': 'date'
    }),
    'rep_dob_municipality': TextInput(attrs={
        'class': 'form-control',
        'id': 'leg_dob_municipality'
    }),
    'rep_dob_province': TextInput(attrs={
        'class': 'form-control',
        'id': 'leg_dob_province'
    }),

    'rep_residence_zip': TextInput(attrs={
        'class': 'form-control',
        'id': 'leg_rep_name'
    }),
    'rep_street': TextInput(attrs={
        'class': 'form-control',
        'id': 'rep_street'
    }),
    'rep_fiscal_code': TextInput(attrs={
        'class': 'form-control',
        'id': 'rep_fiscal_code'
    }),
    'rep_tax_code': TextInput(attrs={
        'class': 'form-control',
        'id': 'rep_tax_code'
    }),
    'rep_phone_number': TextInput(attrs={
        'class': 'form-control',
        'id': 'rep_phone_number'
    }),
    'ss_fund': TextInput(attrs={
        'class': 'form-control',
        'id': 'ss_fund'
    })
}


class Individual(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=120)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    birthplace = models.CharField(max_length=30)
    birthplace_county = models.CharField(max_length=30)
    residence_city = models.CharField(max_length=50)
    residence_province = models.CharField(max_length=50)
    residence_cap = models.IntegerField(blank=False)
    activity_street = models.CharField(max_length=50)
    activity_municipality = models.CharField(max_length=50)
    activity_province = models.CharField(max_length=50)
    activity_cap = models.IntegerField(blank=False)
    residence_street = models.CharField(max_length=50)
    board_order_registration = models.CharField(max_length=50)
    province_college = models.CharField(max_length=40)
    number_of_reg_order_college = models.IntegerField(blank=False)
    vat_number = VATNumberField(countries=['IT'])
    fiscal_code = models.CharField(max_length=40)
    phone_number = PhoneField(blank=False)
    security_case_technician = models.CharField(max_length=5, choices=SSCT)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class DataDesignerIndividual(Individual):
    class Meta:
        managed = True


class Legal(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    municipal_reg_office = models.CharField(max_length=20)
    province_reg_office = models.CharField(max_length=20)
    cap_reg_office = models.CharField(max_length=20)
    street_reg_office = models.CharField(max_length=100)
    province_of_inscription_enterprises_register = models.CharField(max_length=20)
    number_of_inscription_enterprises_register = models.CharField(max_length=50)
    rep_name = models.CharField(max_length=100)
    rep_dob = models.DateField(auto_now=False, auto_now_add=False)
    rep_dob_municipality = models.CharField(max_length=50)
    rep_dob_province = models.CharField(max_length=50)
    rep_residence_municipality = models.CharField(max_length=100)
    rep_residence_province = models.CharField(max_length=100)
    rep_residence_zip = models.CharField(max_length=30)
    rep_street = models.CharField(max_length=100)
    rep_fiscal_code = models.CharField(max_length=50)
    rep_phone_number = models.IntegerField(blank=False)
    ss_fund = models.IntegerField(blank=False)

    def __str__(self):
        return self.company_name

    class Meta:
        abstract = True


class DataDesignerLegal(Legal):
    class Meta:
        managed = True


class DataSecurityCoordinatorIndividual(Individual):
    class Meta:
        managed = True


class DataSecurityCoordinatorLegal(Legal):
    class Meta:
        managed = True


class DataSecurityCoordinatorExecutionIndividual(Individual):
    class Meta:
        managed = True


class DataSecurityCoordinatorExecutionLegal(Legal):
    class Meta:
        managed = True


class DataDirectorWorksIndividual(Individual):
    class Meta:
        managed = True


class DataDirectorWorksLegal(Legal):
    class Meta:
        managed = True


class DataThermoTechnicalIndividual(Individual):
    class Meta:
        managed = True


class DataThermoTechnicalLegal(Legal):
    class Meta:
        managed = True


class DataEnergyExpertIndividual(Individual):
    class Meta:
        managed = True


class DataEnergyExpertLegal(Legal):
    class Meta:
        managed = True


class DataResponsibleForWorksIndividual(Individual):
    class Meta:
        managed = True


class DataResponsibleForWorksLegal(Legal):
    class Meta:
        managed = True


class Prof_table(models.Model):
    id = models.AutoField(primary_key=True)
    designer_individual = models.ForeignKey(DataDesignerIndividual, on_delete=models.CASCADE,
                                            related_name='disgner_individual',
                                            blank=True, null=True)
    designer_legal = models.ForeignKey(DataDesignerLegal, on_delete=models.CASCADE, related_name='disgner_legal',
                                       blank=True, null=True)
    security_exe_individual = models.ForeignKey(DataSecurityCoordinatorExecutionIndividual, on_delete=models.CASCADE,
                                                related_name='sec_exe_individual', blank=True, null=True)
    security_exe_legal = models.ForeignKey(DataSecurityCoordinatorExecutionLegal, on_delete=models.CASCADE,
                                           related_name='sec_exe_legal', blank=True, null=True)
    security_plan_individual = models.ForeignKey(DataSecurityCoordinatorIndividual, on_delete=models.CASCADE,
                                                 related_name='secutiy_individual', blank=True, null=True)
    security_plan_legal = models.ForeignKey(DataSecurityCoordinatorLegal, on_delete=models.CASCADE,
                                            related_name='security_individual', blank=True, null=True)
    director_works_individual = models.ForeignKey(DataDirectorWorksIndividual, on_delete=models.CASCADE,
                                                  related_name='direktor_individual', blank=True, null=True)
    director_works_legal = models.ForeignKey(DataDirectorWorksLegal, on_delete=models.CASCADE,
                                             related_name='direktor_legal', blank=True, null=True)
    thermotechnical_individual = models.ForeignKey(DataThermoTechnicalIndividual, on_delete=models.CASCADE,
                                                   related_name='+', blank=True, null=True)
    thermotechnical_legal = models.ForeignKey(DataThermoTechnicalLegal, on_delete=models.CASCADE,
                                              related_name='+', blank=True, null=True)
    energy_expert_individual = models.ForeignKey(DataEnergyExpertIndividual, on_delete=models.CASCADE,
                                                 related_name='dividual', blank=True, null=True)
    energy_expert_legal = models.ForeignKey(DataEnergyExpertLegal, on_delete=models.CASCADE,
                                            related_name='energy_legal', blank=True, null=True)
    resp_work_individual = models.ForeignKey(DataResponsibleForWorksIndividual, on_delete=models.CASCADE,
                                             related_name='resposible_for_work_ind', blank=True, null=True)
    resp_work_legal = models.ForeignKey(DataResponsibleForWorksLegal, on_delete=models.CASCADE,
                                        related_name='resposible_for_work_leg', blank=True, null=True)

    class Meta:
        verbose_name = ("Proifessionals Table List")


# Forms
class DataDesignerIndividualForm(ModelForm):
    class Meta:
        model = DataDesignerIndividual
        exclude = ['id', 'form_id']
        labels = individual_labels
        widgets = individual_widgets


class DataDesignerLegalForm(ModelForm):
    class Meta:
        model = DataDesignerLegal
        exclude = ['id', 'form_id']
        labels = legal_labels
        widgets = legal_widgets


class DataSecurityCoordinatorIndividualForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorIndividual
        exclude = ['id', 'form_id']
        labels = individual_labels
        widgets = individual_widgets


class DataSecurityCoordinatorLegalForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorLegal
        exclude = ['id', 'form_id']
        labels = legal_labels
        widgets = legal_widgets


class DataSecurityCoordinatorExecutionIndividualForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorExecutionIndividual
        exclude = ['id', 'form_id']
        labels = individual_labels
        widgets = individual_widgets


class DataSecurityCoordinatorExecutionLegalForm(ModelForm):
    class Meta:
        model = DataSecurityCoordinatorExecutionLegal
        exclude = ['id', 'form_id']
        labels = legal_labels
        widgets = legal_widgets


class DataDirectorWorksIndividualForm(ModelForm):
    class Meta:
        model = DataDirectorWorksIndividual
        exclude = ['id', 'form_id']
        labels = individual_labels
        widgets = individual_widgets


class DataDirectorWorksLegalForm(ModelForm):
    class Meta:
        model = DataDirectorWorksLegal
        exclude = ['id', 'form_id']
        labels = legal_labels
        widgets = legal_widgets


class DataThermoTechnicalIndividualForm(ModelForm):
    class Meta:
        model = DataThermoTechnicalIndividual
        exclude = ['id', 'form_id']
        labels = individual_labels
        widgets = individual_widgets


class DataThermoTechnicalLegalForm(ModelForm):
    class Meta:
        model = DataThermoTechnicalLegal
        exclude = ['id', 'form_id']
        labels = legal_labels
        widgets = legal_widgets


class DataEnergyExpertIndividualForm(ModelForm):
    class Meta:
        model = DataEnergyExpertIndividual
        exclude = ['id', 'form_id']
        labels = individual_labels
        widgets = individual_widgets


class DataEnergyExpertLegalForm(ModelForm):
    class Meta:
        model = DataEnergyExpertLegal
        exclude = ['id', 'form_id']
        labels = legal_labels
        widgets = legal_widgets


class DataResponsibleForWorksIndividualForm(ModelForm):
    class Meta:
        model = DataResponsibleForWorksIndividual
        exclude = ['id', 'form_id']
        labels = individual_labels
        widgets = individual_widgets


class DataResponsibleForWorksLegalForm(ModelForm):
    class Meta:
        model = DataResponsibleForWorksLegal
        exclude = ['id', 'form_id']
        labels = legal_labels
        widgets = legal_widgets


class ProfessionChoiceForm(Form):
    professions = ChoiceField(
        choices=PROFESSION_CHOICES
    )
    type = ChoiceField(
        choices=[('PERSONA FISICA', 'PERSONA FISICA'), ('PERSONA GIURIDICA', 'PERSONA GIURIDICA')]
    )


class ProfTableForm(ModelForm):
    class Meta:
        model = Prof_table
        fields = '__all__'
        labels = {
            'id': 'ID',
            'designer_individual': 'PROGETTISTA PERSONA FISICA',
            'designer_legal': 'PROGETTISTA PERSONA GIURIDICA',
            'security_plan_individual': 'COORDINATORE SICUREZZA IN FASE DI PROGETTAZIONE PERSONA FISICA',
            'security_plan_legal': 'COORDINATORE SICUREZZA IN FASE DI PROGETTAZIONE PERSONA GIURIDICA',
            'security_exe_individual': ' COORDINATORE SICUREZZA IN FASE DI ESECUZIONE PERSONA FISICA',
            'security_exe_legal': 'COORDINATORE SICUREZZA IN FASE DI ESECUZIONE PERSONA GIURIDICA',
            'director_works_individual': 'DIRETTORE LAVORI PERSONA FISICA',
            'director_works_legal': ' DIRETTORE LAVORI PERSONA GIURIDICA',
            'thermotechnical_individual': 'TERMOTECNICO PERSONA FISICA',
            'thermotechnical_legal': 'TERMOTECNICO PERSONA GIURIDICA',
            'energy_expert_individual': 'ESPERTO ENERGETICO PERSONA FISICA',
            'energy_expert_legal': 'ESPERTO ENERGETICO PERSONA GIURIDICA ',
            'resp_work_individual': 'RESPONSABILE DEI LAVORI PERSONA FISICA',
            'resp_work_legal': 'RESPONSABILE DEI LAVORI PERSONA GIURIDICA ',
        }


class ProfTableLegalForm(ModelForm):
    class Meta:
        model = Prof_table
        exclude = ['id', 'designer_individual', 'security_plan_individual', 'security_exe_individual',
                   'director_works_individual', 'thermotechnical_individual', 'energy_expert_individual',
                   'resp_work_individual']
        labels = {
            'designer_legal': 'PROGETTISTA PERSONA GIURIDICA',
            'security_plan_legal': 'COORDINATORE SICUREZZA IN FASE DI PROGETTAZIONE PERSONA GIURIDICA',
            'security_exe_legal': 'COORDINATORE SICUREZZA IN FASE DI ESECUZIONE PERSONA GIURIDICA',
            'director_works_legal': ' DIRETTORE LAVORI PERSONA GIURIDICA',
            'thermotechnical_legal': 'TERMOTECNICO PERSONA GIURIDICA',
            'energy_expert_legal': 'ESPERTO ENERGETICO PERSONA GIURIDICA ',
            'resp_work_legal': 'RESPONSABILE DEI LAVORI PERSONA GIURIDICA ',
        }


class ProfTableIndividualForm(ModelForm):
    class Meta:
        model = Prof_table
        exclude = ['id', 'designer_legal', 'security_plan_legal', 'security_exe_legal', 'director_works_legal',
                   'thermotechnical_legal', 'energy_expert_legal', 'resp_work_legal']
        labels = {
            'designer_individual': 'PROGETTISTA PERSONA FISICA',
            'security_plan_individual': 'COORDINATORE SICUREZZA IN FASE DI PROGETTAZIONE PERSONA FISICA',
            'security_exe_individual': ' COORDINATORE SICUREZZA IN FASE DI ESECUZIONE PERSONA FISICA',
            'director_works_individual': 'DIRETTORE LAVORI PERSONA FISICA',
            'thermotechnical_individual': 'TERMOTECNICO PERSONA FISICA',
            'energy_expert_individual': 'ESPERTO ENERGETICO PERSONA FISICA',
            'resp_work_individual': 'RESPONSABILE DEI LAVORI PERSONA FISICA',
        }


profession_individual = {
    'data-designer': DataDesignerIndividualForm,
    'data-security-coordinator-design': DataSecurityCoordinatorIndividualForm,
    'data-security-coordinator-execution': DataSecurityCoordinatorExecutionIndividualForm,
    'director-works': DataDesignerIndividualForm,
    'thermotechnical': DataThermoTechnicalIndividualForm,
    'data-energy-expert': DataEnergyExpertIndividualForm,
    'data-responsible': DataResponsibleForWorksIndividualForm,
}

profession_legal = {
    'data-designer': DataDesignerLegalForm,
    'data-security-coordinator-design': DataSecurityCoordinatorLegalForm,
    'data-security-coordinator-execution': DataSecurityCoordinatorExecutionLegalForm,
    'director-works': DataDesignerLegalForm,
    'thermotechnical': DataThermoTechnicalLegalForm,
    'data-energy-expert': DataEnergyExpertLegalForm,
    'data-responsible': DataResponsibleForWorksLegalForm,
}


def get_form_class_individual(prof):
    return profession_individual.get(prof)


def get_form_class_legal(prof):
    return profession_legal.get(prof)