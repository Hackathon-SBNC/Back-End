from rest_framework.viewsets import ModelViewSet

from core.models import Responsavel
from core.serializers import ResponsavelSerializer


class ResponsavelViewSet(ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer