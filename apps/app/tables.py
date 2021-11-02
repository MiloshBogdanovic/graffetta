import django_tables2 as tables
from apps.app.models import AdministrationIndividual, AdministrationLegal, CatastalData, CondominiumData



class CondominiumTable(tables.Table):
    name = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.name,
                'data-type':'name'
        }
    }, verbose_name='nome')

    fiscal_code = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.fiscal_code,
                'data-type':'fiscal_code'
        }
    }, verbose_name='codice fiscale')

    street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.street,
                'data-type':'street'
        }
    }, verbose_name='Via')

    cap = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.cap,
                'data-type':'cap'
        }
    })

    municipality = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.municipality,
                'data-type':'municipality'
        }
    }, verbose_name='comune')

    province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province,
                'data-type':'province'
        }
    }, verbose_name='provincia')

    email = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.email,
                'data-type':'email'
        }
    }, verbose_name='e-mail')

    pec_mail = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.pec_mail,
                'data-type':'pec_mail'
        }
    }, verbose_name='pec e-mail')

    select_administrator = tables.Column(verbose_name='tipo di amministratore')
    
    class Meta:
        model = CondominiumData
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-table":'condo'
        }
        attrs = {
            'class':'table table-hover m-b-0'
        }

class CatastalTable(tables.Table):
    n_catastal_cheet = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_catastal_cheet,
                'data-type':'n_catastal_cheet'
        }
    })
    n_first_particle = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_first_particle,
                'data-type':'n_first_particle'
        }
    })
    n_subscribers_to_first_belonging = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_subscribers_to_first_belonging,
                'data-type':'n_subscribers_to_first_belonging'
        }
    })
    n_second_particle = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_second_particle,
                'data-type':'n_second_particle'
        }
    })
    n_subscribers_to_second_belonging = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_subscribers_to_second_belonging,
                'data-type':'n_subscribers_to_second_belonging'
        }
    })
    n_third_particle = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_third_particle,
                'data-type':'n_third_particle'
        }
    })
    n_subscribers_to_third_belonging = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_subscribers_to_third_belonging,
                'data-type':'n_subscribers_to_third_belonging'
        }
    })
    n_fourth_particle = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_fourth_particle,
                'data-type':'n_fourth_particle'
        }
    })

    n_subscribers_to_fourth_belonging = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.n_subscribers_to_fourth_belonging,
                'data-type':'n_subscribers_to_fourth_belonging'
        }
    })
    
    description_of_intervention = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.description_of_intervention,
                'data-type':'description_of_intervention'
        }
    })
    data_of_condominium_assembly = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.data_of_condominium_assembly,
                'data-type':'data_of_condominium_assembly'
        }
    })
    class Meta:
        model = CatastalData
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-table":'cat'
        }
        attrs = {
            'class': 'table table-hover m-b-0'
        }

class AdministrationLegalTable(tables.Table):
    company_name = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.company_name,
                'data-type':'company_name'
        }
    }, verbose_name='Nome commerciale')
    province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province,
                'data-type':'province'
        }
    }, verbose_name='Provincia')
    vat_number = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.vat_number,
                'data-type':'vat_number'
        }
    }, verbose_name='Partita IVA')
    street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.street,
                'data-type':'street'
        }
    }, verbose_name='strada')
    cap = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.cap,
                'data-type':'cap'
        }
    })
    municipal_reg_office = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.municipal_reg_office,
                'data-type':'municipal_reg_office'
        }
    }, verbose_name='sede legale comunale')
    province_reg_office = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province_reg_office,
                'data-type':'province_reg_office'
        }
    }, verbose_name='sede legale della provincia')
    legal_title_rep = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.legal_title_rep,
                'data-type':'legal_title_rep'
        }
    }, verbose_name='titolo rappresentativo ')
    leg_rep_name = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.leg_rep_name,
                'data-type':'leg_rep_name'
        }
    }, verbose_name='nome del rappresentante ')
    leg_rep_tax_code = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.leg_rep_tax_code,
                'data-type':'leg_rep_tax_code'
        }
    }, verbose_name='codice fiscale rappresentativo ')
    leg_rep_dob = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.leg_rep_dob,
                'data-type':'leg_rep_dob'
        }
    }, verbose_name='data di nascita rappresentativa ')
    municipal_of_birth_of_leg = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.municipal_of_birth_of_leg,
                'data-type':'municipal_of_birth_of_leg'
        }
    }, verbose_name='data di nascita rappresentativa comune ')
    province_of_birth_of_leg = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province_of_birth_of_leg,
                'data-type':'province_of_birth_of_leg'
        }
    })
    legal_street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.legal_street,
                'data-type':'legal_street'
        }
    }, verbose_name='strada legale')

    cap_legal = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.cap_legal,
                'data-type':'cap_legal'
        }
    }, verbose_name='cap legale')

    municipal_of_leg_residence = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.municipal_of_leg_residence,
                'data-type':'municipal_of_leg_residence'
        }
    }, verbose_name='comune di residenza legale')

    province_of_leg_residence = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province_of_leg_residence,
                'data-type':'province_of_leg_residence'
        }
    }, verbose_name='provincia di residenza legale ')

    class Meta:
        model = AdministrationLegal
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-table":'legal'
        }
        attrs = {
            'class': 'table table-hover m-b-0'
        }

class AdministrationIndividualTable(tables.Table):
    title = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.title,
                'data-type':'title'
        }
    }, verbose_name='titolo')
    name = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.name,
                'data-type':'name'
        }
    }, verbose_name='nome e cognome')
    fiscal_code = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.fiscal_code,
                'data-type':'fiscal_code'
        }
    }, verbose_name='codice fiscale')
    vat_number = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.vat_number,
                'data-type':'vat_number'
        }
    }, verbose_name='Partita IVA')
    dob = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.dob,
                'data-type':'dob'
        }
    }, verbose_name='data di nascita')
    birthplace = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.birthplace,
                'data-type':'birthplace'
        }
    }, verbose_name='luogo di nascita')
    birthplace_county = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.birthplace_county,
                'data-type':'birthplace_county'
        }
    }, verbose_name='contea natale')
    activity_street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_street,
                'data-type':'activity_street'
        }
    }, verbose_name='via delle attività')
    activity_location_cap = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_location_cap,
                'data-type':'activity_location_cap'
        }
    }, verbose_name='via delle attività')
    activity_municipality = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_municipality,
                'data-type':'activity_municipality'
        }
    }, verbose_name='comune di attività')
    activity_province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_province,
                'data-type':'activity_province'
        }
    }, verbose_name='provincia di attività')
    residence_street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.residence_street,
                'data-type':'residence_street'
        }
    }, verbose_name='via della residenza')
    residence_city = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.residence_city,
                'data-type':'residence_city'
        }
    }, verbose_name='città di residenza')
    residence_province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.residence_province,
                'data-type':'residence_province'
        }
    }, verbose_name='provincia di residenza')

    class Meta: 
        model = AdministrationIndividual
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-table":'individual'
        }
        attrs = {
            'class': 'table table-hover m-b-0'
        }