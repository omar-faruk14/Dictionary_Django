from django.db import models

class Dic(models.Model):
        word_ID = models.AutoField(primary_key=True)
        word_Nihon = models.CharField(max_length=250)
        word_Kanji = models.CharField(max_length=250,null = True)
        word_Nihon_Similar = models.CharField(max_length=250,null = True)
        Word_Meaning_Eng = models.CharField(max_length=250)
     



   

