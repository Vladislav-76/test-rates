from django_filters import FilterSet, rest_framework

from currencies.models import Rate


class RateFilter(FilterSet):
    """Фильтр для курсов."""

    charcode = rest_framework.CharFilter(field_name='currency__charcode')

    class Meta:
        model = Rate
        fields = ('charcode', 'date')
