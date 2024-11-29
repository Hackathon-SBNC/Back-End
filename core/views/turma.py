from rest_framework.viewsets import ModelViewSet

from core.models import Turma
from core.serializers import TurmaSerializer


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer