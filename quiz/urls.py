from django.urls import path
from quiz.views.index import index_view
from quiz.views.categories import category_view
from quiz.views.quiz import quiz_view

urlpatterns = [
    path('', index_view, name='index'),
    path('<slug:cat>/', category_view, name='category'),
    path('<slug:cat>/<slug:quiz>/', quiz_view, name='quiz'),

    
]
