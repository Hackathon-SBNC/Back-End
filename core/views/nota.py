from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from core.models import Nota
from core.serializers import NotaSerializer


class NotaViewSet(ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["aluno__id", "disciplina__id"]