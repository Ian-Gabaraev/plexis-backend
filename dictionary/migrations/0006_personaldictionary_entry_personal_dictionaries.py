# Generated by Django 4.0.6 on 2022-08-05 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictionary', '0005_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='personal_dictionaries',
            field=models.ManyToManyField(blank=True, to='dictionary.personaldictionary'),
        ),
    ]