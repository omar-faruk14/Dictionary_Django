# Generated by Django 4.2 on 2023-04-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0004_dic_word_kanji"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dic",
            name="word_Kanji",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
