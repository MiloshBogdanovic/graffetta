from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.models import AdministrationIndividual, AdministrationLegal, CatastalData, CondominiumData


@csrf_exempt
def save_admin_individual(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    try:       
        admin_individual=AdministrationIndividual.objects.get(id=id)
        if type=="title":
            admin_individual.title=value

        if type == "name":
            admin_individual.name = value

        if type == "fiscal_code":
            admin_individual.fiscal_code = value

        if type == "vat_number":
            admin_individual.vat_number = value

        if type == "dob":
            admin_individual.dob = value

        if type == "birthplace":
            admin_individual.birthplace = value

        if type == "birthplace_county":
            admin_individual.birthplace_county = value

        if type == "activity_street":
            admin_individual.activity_street = value

        if type == "activity_location_cap":
            admin_individual.activity_location_cap = value
        
        if type == "activity_municipality":
            admin_individual.activity_municipality = value
        
        if type == "activity_province":
            admin_individual.activity_province = value
        
        if type == "residence_street":
            admin_individual.residence_street = value
        
        if type == "residence_cap":
            admin_individual.residence_cap = value
        
        if type == "residence_city":
            admin_individual.residence_city = value
        
        if type == "residence_province":
            admin_individual.residence_province = value
        
        admin_individual.save()
        return JsonResponse({"success":"Updated"})
    except:
        return JsonResponse({"success": False})

@csrf_exempt
def save_admin_legal(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    try:       
        admin_legal = AdministrationLegal.objects.get(id=id)
        if type=="company_name":
            admin_legal.company_name=value

        if type == "province":
            admin_legal.province = value

        if type == "vat_number":
            admin_legal.vat_number = value

        if type == "street":
            admin_legal.street = value

        if type == "cap":
            admin_legal.cap = value

        if type == "municipal_reg_office":
            admin_legal.municipal_reg_office = value

        if type == "province_reg_office":
            admin_legal.province_reg_office = value

        if type == "legal_title_rep":
            admin_legal.legal_title_rep = value

        if type == "leg_rep_name":
            admin_legal.leg_rep_name = value
        
        if type == "leg_rep_tax_code":
            admin_legal.leg_rep_tax_code = value
        
        if type == "leg_rep_dob":
            admin_legal.leg_rep_dob = value
        
        if type == "municipal_of_birth_of_leg":
            admin_legal.municipal_of_birth_of_leg = value
        
        if type == "province_of_birth_of_leg":
            admin_legal.province_of_birth_of_leg = value
        
        if type == "legal_street":
            admin_legal.legal_street = value
        
        if type == "cap_legal":
            admin_legal.cap_legal = value
        
        if type == "municipal_of_leg_residence":
            admin_legal.municipal_of_leg_residence = value
        
        if type == "province_of_leg_residence":
            admin_legal.province_of_leg_residence = value
        
        admin_legal.save()
        return JsonResponse({"success":"Updated"})
    except:
        return JsonResponse({"success": False})

@csrf_exempt
def save_condominium(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    try:       
        condo = CondominiumData.objects.get(id=id)
        if type=="name":
            condo.name=value
        
        if type=="fiscal_code":
            condo.fiscal_code=value
        
        if type=="street":
            condo.street=value
        
        if type=="cap":
            condo.cap=value
        
        if type=="municipality":
            condo.municipality=value
        
        if type=="province":
            condo.province=value
        
        if type=="email":
            condo.email = value
        
        if type=="pec_mail":
            condo.pec_mail=value
        
        condo.save()
        return JsonResponse({"success":"Updated"})
    except:
        return JsonResponse({"success": False})

@csrf_exempt
def save_catastal(request):
    id=request.POST.get('id', '')
    type=request.POST.get('type', '')
    value=request.POST.get('value', '')
    try:
        cat = CatastalData.objects.get(id=id)
        if type == "n_catastal_cheet":
            cat.n_catastal_cheet = value

        if type == "n_first_particle":
            cat.n_first_particle = value
        
        if type == "n_subscribers_to_first_belonging":
            cat.n_subscribers_to_first_belonging = value
        
        if type == "n_second_particle":
            cat.n_second_particle = value
        
        if type == "n_subscribers_to_second_belonging":
            cat.n_subscribers_to_second_belonging = value
        
        if type == "n_third_particle":
            cat.n_third_particle = value
        
        if type == "n_subscribers_to_third_belonging":
            cat.n_subscribers_to_third_belonging = value
        
        if type == "n_fourth_particle":
            cat.n_fourth_particle = value
        
        if type == "n_subscribers_to_fourth_belonging":
            cat.n_subscribers_to_fourth_belonging = value
        
        if type == "description_of_intervention":
            cat.description_of_intervention = value
        
        if type == "data_of_condominium_assembly":
            cat.data_of_condominium_assembly = value
        
        cat.save()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})