from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import OverallInventory


class TableListView(ListView):
    model = OverallInventory
    template_name = 'table.html'