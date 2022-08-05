from django.contrib import admin

from .models import Entry, Example, Tag

admin.site.register(Entry)
admin.site.register(Example)
admin.site.register(Tag)
