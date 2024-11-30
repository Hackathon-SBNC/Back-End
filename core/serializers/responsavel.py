from rest_framework.serializers import ModelSerializer

from core.models import Responsavel


class ResponsavelSerializer(ModelSerializer):
    class Meta:
        model = Responsavel
        fields = "__all__"
        depth = 1