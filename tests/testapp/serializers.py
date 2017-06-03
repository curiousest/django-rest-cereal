
from rest_framework import serializers

from .models import A, B, C
from .mixins import ReduceFieldsMixin


class ASerializer(ReduceFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = A
        fields = ('b', 'title')


class BSerializer(ReduceFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = B
        fields = ('c', 'title')


class CSerializer(ReduceFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = C
        fields = ('a', 'title')

