import django_tables2 as tables
from apps.app.models import CondominiumData



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