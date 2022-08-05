# Generated by Django 4.0.6 on 2022-08-05 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_personaldictionary_entry_personal_dictionaries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='personal_dictionaries',
        ),
        migrations.CreateModel(
            name='EntryLearningProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_exposed', models.DateTimeField(blank=True, null=True)),
                ('failed_attempts', models.IntegerField(default=0)),
                ('successful_attempts', models.IntegerField(default=0)),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.entry')),
                ('personal_dictionaries', models.ManyToManyField(blank=True, to='dictionary.personaldictionary')),
            ],
        ),
    ]
