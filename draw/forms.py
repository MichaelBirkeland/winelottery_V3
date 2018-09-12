from django.forms import ModelForm
from .models import Sjanse


class BuyTickets(ModelForm):
	class Meta:
	    model = Sjanse
	    fields = ['antall_lodd',]
