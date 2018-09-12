from django.db import models
from accounts.models import Deltager
from django.core.validators import validate_comma_separated_integer_list

#from django.utils.timezone import timezone


# Create your models here.
class Sjanse(models.Model):

	antall_lodd = models.IntegerField()
	kjopt_dato = models.DateField(auto_now=False, auto_now_add=False)
	owner= models.ForeignKey('auth.User', on_delete=models.CASCADE)
	tall=models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')


class Tickets(models.Model):
    my_tickets = models.IntegerField()
    trekknings_dato=models.DateField(auto_now=False, auto_now_add=False)
    valid=models.BooleanField(default=True)
    lot=models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.my_tickets)
