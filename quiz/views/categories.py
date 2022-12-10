from django.http import HttpResponse
#from django.shortcuts import render

def category_view(request, cat):
    return HttpResponse (f'страница {cat}')