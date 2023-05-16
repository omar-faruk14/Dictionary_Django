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
def add_word(request):
    if request.method == 'GET':
        word_nihon = request.GET.get('word_nihon')
        word_meaning = request.GET.get('word_meaning')
        word_nihon_similar = request.GET.get('word_nihon_similar')
        word_kanji = request.GET.get('word_kanji')

        if word_nihon and word_meaning and word_nihon_similar and word_kanji:
            Dic.objects.create(
                word_Nihon=word_nihon,
                Word_Meaning_Eng=word_meaning,
                word_Nihon_Similar=word_nihon_similar,
                word_Kanji=word_kanji
            )
            # Redirect to a success page or display a success message

    return render(request, 'add_word.html')