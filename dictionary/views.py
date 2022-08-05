from django.conf import settings
from django.core.cache import cache
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveAPIView)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Entry
from .paginators import LargeResultsSetPagination
from .serializers import EntrySerializer


class WordOfTheDay(GenericAPIView):

    def get(self, request, *args, **kwargs):
        wod = cache.get(settings.WOD_CACHE_KEY)

        return Response(
            data=wod, status=HTTP_200_OK
        )


class AllWords(ListAPIView):
    serializer_class = EntrySerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Entry.objects.all()
