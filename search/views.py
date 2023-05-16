from django.shortcuts import render, redirect
from .models import Dic
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    if request.method == 'POST':
        form_value = request.POST.get('word')
        data = Dic.objects.filter(word_Nihon=form_value)
        return render(request, 'word.html', {'data': data})
    else:
        return render(request, 'index.html')

def insert_data(request):
    if request.method == 'POST':
        word_nihon = request.POST.get('word_nihon')
        word_meaning_eng = request.POST.get('word_meaning_eng')
        word_nihon_similar = request.POST.get('word_nihon_similar')
        word_kanji = request.POST.get('word_kanji')
        
        Dic.objects.create(
            word_Nihon=word_nihon,
            Word_Meaning_Eng=word_meaning_eng,
            word_Nihon_Similar=word_nihon_similar,
            word_Kanji=word_kanji
        )
        
        return render(request, 'success.html')
    
    return render(request, 'insert_data.html')

from django.core.paginator import Paginator

def display_data(request):
    words = Dic.objects.all()
    
    paginator = Paginator(words, 10)  # Show 10 words per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'display_data.html', {'page_obj': page_obj})

def search_data(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query')
        words = Dic.objects.filter(word_Nihon__icontains=search_query)
        
        paginator = Paginator(words, 10)  # Show 10 words per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'display_data.html', {'page_obj': page_obj, 'search_query': search_query})

    return redirect('display_data')