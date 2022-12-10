from django.urls import path
from quiz.views.index import index_view
from quiz.views.categories import category_view
from quiz.views.quiz import quiz_view

urlpatterns = [
    path('', index_view, name='index'),
    path('<slug:category_slug>/', category_view, name='category'),
    path('<slug:category_slug>/<slug:quiz_slug>/', quiz_view, name='quiz'),
]
