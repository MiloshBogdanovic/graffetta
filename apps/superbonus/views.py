from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from .models import *
from django.contrib import messages
# Create your views here.


@login_required(login_url="/login/")
def app(request):
    context = {'segment': 'bonus-app-view', 'table': SuperBonus.objects.all()}
    html_template = loader.get_template('superbonus.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_condo(request):
    context = {'segment': 'bonus-app-view'}
    html_template = loader.get_template('add-condo.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_villa(request):
    context = {'segment': 'bonus-add-villa', 'form': BonusVillaForm()}
    if request.method == 'POST':
        form = BonusVillaForm(request.POST)
        if form.is_valid():
            super_bonus = SuperBonus(bonus_villa=form.save())
            super_bonus.save()
            messages.success(request, 'Successfully')
            return render(request, 'add-villa.html', context)
        else:
            messages.error(request, 'Error')
            return render(request, 'add-villa.html', context)
    html_template = loader.get_template('add-villa.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def interventions(request):
    context = {'segment': 'bonus-app-view', 'form': InterventionsForm()}
    html_template = loader.get_template('interventions.html')
    # if request.method == 'POST':
    #     form = InterventionsForm(request.POST)
    #     if form.is_valid():
    #         super_bonus = SuperBonus(bonus_villa=form.save())
    #         super_bonus.save()
    #         messages.success(request, 'Successfully')
    #         return render(request, 'add-villa.html', context)
    #     else:
    #         messages.error(request, 'Error')
    #         return render(request, 'add-villa.html', context)
    return HttpResponse(html_template.render(context, request))



#