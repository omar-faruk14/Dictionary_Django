from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('word', views.word, name='word'),
    path('books/', views.book_list, name='book_list'),
    path('insert/', views.insert_data, name='insert_data'),
]
