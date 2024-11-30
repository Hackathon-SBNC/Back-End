from rest_framework.viewsets import ModelViewSet

from core.models import Professor
from core.serializers import ProfessorSerializer


class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer