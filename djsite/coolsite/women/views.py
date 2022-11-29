from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Страница women')

def categories(request, catid):
    return HttpResponse(f'<h1>статьи по категориям</h1><p>{catid}</p>')