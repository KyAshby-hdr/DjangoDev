from django.shortcuts import render
from django.http import HttpResponse

def mapExplorer(request):
    return render(request, 'MapDataExplorer/home.html')

def about(request):
    return render(request, 'MapDataExplorer/about.html')