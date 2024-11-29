from yaml import serialize
from rest_framework.viewsets import ModelViewSet

from core.models import Observacao
from core.serializers import ObservacaoSerializer


class ObservacaoViewSet(ModelViewSet):
    queryset = Observacao.objects.all()
    serializer_class = ObservacaoSerializer