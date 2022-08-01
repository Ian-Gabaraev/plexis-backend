from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.status import HTTP_200_OK

from .serializers import EntrySerializer
from rest_framework.response import Response
from .models import Entry


class WordOfTheDay(RetrieveAPIView):
    serializer_class = EntrySerializer

    def get_object(self):
        return Entry.objects.order_by('?').first()


class AllWords(ListAPIView):
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.all()
