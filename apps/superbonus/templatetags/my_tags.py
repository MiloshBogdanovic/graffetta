from django import template
from apps.superbonus.forms import *
register = template.Library()


@register.inclusion_tag('edit-task.html')
def edit_task(file_id, bonus_id):
    file = FileRequired.objects.get(id=file_id)
    status = StatusFile.objects.get(file=file_id)
    return {'file': file, 'status': status, 'id': bonus_id}


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

