from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
# Create your views here.


@login_required(login_url="/login/")
def app(request):
    context = {'segment': 'bonus-app-view'}
    html_template = loader.get_template('superbonus.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_condo(request, id):
    context = {'segment': 'bonus-app-view'}
    html_template = loader.get_template('add-bonus.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_villa(request, id):
    context = {'segment': 'bonus-app-view'}
    html_template = loader.get_template('add-bonus.html')
    return HttpResponse(html_template.render(context, request))