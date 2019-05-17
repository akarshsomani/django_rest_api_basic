from .models import Ticks
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticks
        fields = ('ticker', 'order_type', 'quantity', 'currency', 'exchange')

