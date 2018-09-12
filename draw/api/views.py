from rest_framework.generics import ListAPIView
from draw.models import Tickets
from .serializers import TicketSerializer
from django.utils import timezone


class TicketsAPIView(ListAPIView):
    queryset = Tickets.objects.filter(trekknings_dato=timezone.now())
    serializer_class = TicketSerializer

