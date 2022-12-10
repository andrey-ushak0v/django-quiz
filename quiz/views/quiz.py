from django.http import HttpResponse
#from django.shortcuts import render

def quiz_view(request, cat, quiz):
    return HttpResponse (f'страница {quiz} из {cat}')