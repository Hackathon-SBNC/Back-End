from rest_framework.serializers import ModelSerializer

from core.models import Aluno


class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"
        depth = 2