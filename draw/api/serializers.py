from rest_framework.serializers import ModelSerializer

from draw.models import Tickets


class TicketSerializer(ModelSerializer):
    class Meta():
        model=Tickets
        fields = ['my_tickets','lot_id','valid']


