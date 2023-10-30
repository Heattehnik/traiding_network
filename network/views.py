from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from .permissions import IsActiveEmployee


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]

    def get_queryset(self):
        country = self.request.query_params.get('country')
        if country:
            return NetworkNode.objects.filter(country=country)
        return NetworkNode.objects.all()

