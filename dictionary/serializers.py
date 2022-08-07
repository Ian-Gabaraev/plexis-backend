from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Entry, Example, Tag


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('value',)


class ExampleSerializer(ModelSerializer):

    class Meta:
        model = Example
        fields = ("id", "text", "author", "source")


class MinimalEntrySerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = ("word",)


class EntrySerializer(ModelSerializer):
    examples = SerializerMethodField()
    tags = TagSerializer(many=True)
    synonyms = SerializerMethodField()
    antonyms = SerializerMethodField()

    class Meta:
        model = Entry
        fields = ("id", "word", "definition", "examples", "tags", "synonyms", "antonyms")

    def get_synonyms(self, obj: Entry):

        return obj.synonyms.values_list("word", flat=True)

    def get_antonyms(self, obj: Entry):

        return obj.antonyms.values_list("word", flat=True)

    def get_examples(self, obj: Entry): # noqa

        return ExampleSerializer(
            obj.example_set.all(),
            many=True
        ).data
