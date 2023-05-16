from django.shortcuts import render
from .models import Dic

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
def book_list(request):
    Dic = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

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