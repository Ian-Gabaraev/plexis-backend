# Generated by Django 4.0.6 on 2022-08-05 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0008_remove_entrylearningprogress_personal_dictionaries_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrylearningprogress',
            name='failed_attempts',
        ),
        migrations.RemoveField(
            model_name='entrylearningprogress',
            name='last_exposed',
        ),
        migrations.RemoveField(
            model_name='entrylearningprogress',
            name='successful_attempts',
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('successful', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.entrylearningprogress')),
            ],
        ),
    ]
