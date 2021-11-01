import django_tables2 as tables
from apps.app.models import AdministrationIndividual, AdministrationLegal, CatastalData, CondominiumData



class CondominiumTable(tables.Table):
    name = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.name,
                'data-type':'name',
                'data-table':'condo'
        }
    })

    fiscal_code = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.fiscal_code,
                'data-type':'fiscal_code',
                'data-table':'condo'
        }
    })

    street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.street,
                'data-type':'street'
        }
    })

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
    })

    province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province,
                'data-type':'province'
        }
    })

    email = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.email,
                'data-type':'email'
        }
    })

    pec_mail = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.pec_mail,
                'data-type':'pec_mail'
        }
    })
    
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
    })
    province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province,
                'data-type':'province'
        }
    })
    vat_number = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.vat_number,
                'data-type':'vat_number'
        }
    })
    street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.street,
                'data-type':'street'
        }
    })
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
    })
    province_reg_office = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province_reg_office,
                'data-type':'province_reg_office'
        }
    })
    legal_title_rep = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.legal_title_rep,
                'data-type':'legal_title_rep'
        }
    })
    leg_rep_name = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.leg_rep_name,
                'data-type':'leg_rep_name'
        }
    })
    leg_rep_tax_code = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.leg_rep_tax_code,
                'data-type':'leg_rep_tax_code'
        }
    })
    leg_rep_dob = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.leg_rep_dob,
                'data-type':'leg_rep_dob'
        }
    })
    municipal_of_birth_of_leg = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.municipal_of_birth_of_leg,
                'data-type':'municipal_of_birth_of_leg'
        }
    })
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
    })

    cap_legal = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.cap_legal,
                'data-type':'cap_legal'
        }
    })

    municipal_of_leg_residence = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.municipal_of_leg_residence,
                'data-type':'municipal_of_leg_residence'
        }
    })

    province_of_leg_residence = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.province_of_leg_residence,
                'data-type':'province_of_leg_residence'
        }
    })

    class Meta:
        model = AdministrationLegal
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-table":'catastal'
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
    })
    name = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.name,
                'data-type':'name'
        }
    })
    fiscal_code = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.fiscal_code,
                'data-type':'fiscal_code'
        }
    })
    vat_number = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.vat_number,
                'data-type':'vat_number'
        }
    })
    dob = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.dob,
                'data-type':'dob'
        }
    })
    birthplace = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.birthplace,
                'data-type':'birthplace'
        }
    })
    birthplace_county = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.birthplace_county,
                'data-type':'birthplace_county'
        }
    })
    activity_street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_street,
                'data-type':'activity_street'
        }
    })
    activity_location_cap = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_location_cap,
                'data-type':'activity_location_cap'
        }
    })
    activity_municipality = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_municipality,
                'data-type':'activity_municipality'
        }
    })
    activity_province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.activity_province,
                'data-type':'activity_province'
        }
    })
    residence_street = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.residence_street,
                'data-type':'residence_street'
        }
    })
    residence_city = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.residence_city,
                'data-type':'residence_city'
        }
    })
    residence_province = tables.Column(attrs={
        'td': {
                'class': 'editable',
                'data-id': lambda record: record.residence_province,
                'data-type':'residence_province'
        }
    })

    class Meta: 
        model = AdministrationIndividual
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-table":'catastal'
        }
        attrs = {
            'class': 'table table-hover m-b-0'
        }