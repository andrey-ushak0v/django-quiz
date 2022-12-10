from django.shortcuts import render
from quiz.models.categories import Category

def index_view(request):
    categories = Category.objects.all()
    context = {
        'title': 'Главная страница',
        'categories': categories,
    }
    return render(request, 'quiz/index.html', context=context)
    