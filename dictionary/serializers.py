from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Entry, Example, Tag


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('value',)


class ExampleSerializer(ModelSerializer):

    class Meta:
        model = Example
        fields = ("text", "author", "source")


class EntrySerializer(ModelSerializer):
    examples = SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Entry
        fields = ("id", "word", "definition", "examples", "tags")

    def get_examples(self, obj: Entry): # noqa

        return ExampleSerializer(
            obj.example_set.all(),
            many=True
        ).data
