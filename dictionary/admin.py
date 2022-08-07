from django.contrib import admin

from .models import Entry, EntryLearningProgress, Example, Tag

for model in [Example, Tag, EntryLearningProgress]:
    admin.site.register(model)


class ExampleInline(admin.StackedInline):
    model = Example


class EntryLearningProgressInline(admin.StackedInline):
    model = EntryLearningProgress


class TagInline(admin.StackedInline):
    model = Tag


class EntryAdmin(admin.ModelAdmin):
    inlines = [
        ExampleInline,
        EntryLearningProgressInline,
    ]


admin.site.register(Entry, EntryAdmin)
