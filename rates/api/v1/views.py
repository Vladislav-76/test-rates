from api.v1.filters import RateFilter
from api.v1.serialaizers import RateSerializer
from currencies.models import Rate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer


class RateListView(ListAPIView):
    """Отображение списка курсов."""

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RateFilter
    renderer_classes = (JSONRenderer,)
