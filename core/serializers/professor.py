from rest_framework.serializers import ModelSerializer

from core.models import Professor


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"
        depth = 1