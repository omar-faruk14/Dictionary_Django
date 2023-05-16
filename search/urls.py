from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('word', views.word, name='word'),
    path('insert/', views.insert_data, name='insert_data'),
    path('display_data/', views.display_data, name='display_data'),
    path('my_view', views.my_view, name='my_view'),
]
