# Generated by Django 4.0.6 on 2022-08-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0011_entry_antonyms_entry_synonyms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
