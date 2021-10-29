from django.core import serializers
from django.http import JsonResponse
from django.urls.conf import path
from django.views.decorators.csrf import csrf_exempt

from app.models import AdministrationIndividual, AdministrationLegal, CatastalData, CondominiumData


@csrf_exempt
def save_table_data(request):
    try:
        id=request.POST.get('id','')
        type=request.POST.get('type', '')
        value=request.POST.get('value', '')
        table=request.POST.get('table', '') 
        write_to = None
        
        if(table == 'condo'):
            write_to = CondominiumData.objects.get(id=id)
        elif(table == 'individual'):
            write_to = AdministrationIndividual.objects.get(id=id)
        elif(table == 'legal'):
            write_to = AdministrationLegal.objects.get(id=id)
        elif(table == 'cat'):
            write_to = CatastalData.objects.get(id=id)
        
        
        write_to[type]=value
        write_to.save()
        return JsonResponse({"success":"Info updated."})

    except Exception as e:
        print('Error saving table data:')
        print(e)
        return JsonResponse({'success':False})