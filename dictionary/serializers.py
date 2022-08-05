from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Entry, Example, Tag


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('value',)


class ExampleSerializer(ModelSerializer):

    class Meta:
        model = Example
        fields = "__all__"


class EntrySerializer(ModelSerializer):
    examples = SerializerMethodField()
    tags = SerializerMethodField()

    class Meta:
        model = Entry
        fields = ("id", "word", "definition", "examples", "tags")

    def get_examples(self, obj: Entry): # noqa

        return ExampleSerializer(
            obj.example_set.all(),
            many=True
        ).data

    def get_tags(self, obj: Entry): # noqa

        return TagSerializer(
            obj.tag_set.all(),
            many=True
        ).data
