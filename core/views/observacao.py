from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from core.models import Observacao
from core.serializers import ObservacaoSerializer


class ObservacaoViewSet(ModelViewSet):
    queryset = Observacao.objects.all()
    serializer_class = ObservacaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["aluno__id"]