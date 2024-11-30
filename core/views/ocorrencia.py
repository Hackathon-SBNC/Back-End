from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from core.models import Ocorrencia
from core.serializers import OcorrenciaSerializer


class OcorrenciaViewSet(ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["aluno__id"]