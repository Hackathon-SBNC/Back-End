from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from core.models import Aluno
from core.serializers import AlunoSerializer


class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["turma__id", "turma__curso__id"]
    search_fields = ["nome", "matricula"]