from django import template
from apps.superbonus.forms import *

register = template.Library()


@register.simple_tag
def get_verbose_name(object):
    return object._meta.verbose_name


@register.inclusion_tag('edit-task.html')
def edit_task(file_id, bonus_id, modal_target):
    file = FileRequired.objects.get(id=file_id)
    status = StatusFile.objects.get(file=file_id)
    return {'file': file, 'status': status, 'id': bonus_id, 'modal_target': modal_target}


@register.inclusion_tag('file-table.html')
def file_table( bonus_id, modal_target):
    bank_req = BankRequirements.objects.get(bonus=bonus_id)
    files = getattr(bank_req, modal_target).all()
    print(type(files))
    files = list(files)
    statuses = list()
    res = {}
    for file in files:
        statuses.append(StatusFile.objects.get(file=file.id))

    for f in files:
        for s in statuses:
            res[f] = s
            statuses.remove(s)
            break
    print(res)
    return {'files': res, 'statuses': statuses, 'id': bonus_id, 'modal_target': modal_target}


@register.inclusion_tag('status-task.html')
def get_status(file_id):
    print(file_id)
    if file_id:
        try:
            status = StatusFile.objects.get(file=file_id)
            return {'status': status.status}
        except StatusFile.DoesNotExist:
            return {'status': None}
    else:
        return {'status': None}


@register.inclusion_tag('status-task.html')
def get_status_all(field, bank_req_id):
    bank_req = BankRequirements.objects.get(id=bank_req_id)
    if bank_req:
        files_status = getattr(bank_req, field).all()
        statuses = set()
        if files_status:
            for file in files_status:
                statuses.add(StatusFile.objects.get(file=file.id).status)
        else:
            return {'status': None}

        if all(s == 'UPLOADED' for s in statuses):
            statuses.clear()
            return {'status': 'UPLOADED'}
        elif all(s == 'VERIFIED' for s in statuses):
            statuses.clear()
            return {'status': 'VERIFIED'}
        elif all(s == 'AUTHORISED' for s in statuses):
            statuses.clear()
            return {'status': 'AUTHORISED'}
        else:
            return {'status': 'UNFINISHED'}


@register.inclusion_tag('add-file-modal.html')
def file_modal(modal_id):
    file = FileRequiredForm()
    status = StatusFileForm()
    return {'modal_id': modal_id, 'file_form': file, 'status_form': status}


