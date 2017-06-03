from rest_framework import viewsets

from .models import A, B, C
from .serializers import ASerializer, BSerializer, CSerializer


class AViewSet(viewsets.ModelViewSet):
    queryset = A.objects.all()
    serializer_class = ASerializer


class BViewSet(viewsets.ModelViewSet):
    queryset = B.objects.all()
    serializer_class = BSerializer


class CViewSet(viewsets.ModelViewSet):
    queryset = C.objects.all()
    serializer_class = CSerializer

