from currencies.models import Rate
from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    """Сериализатор курса."""

    charcode = serializers.StringRelatedField(source='currency')
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        fields = ('charcode', 'date', 'rate')

    def get_rate(self, rate):
        return round(rate.value / rate.nominal, 4)
