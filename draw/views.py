from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Sjanse, Tickets
from accounts.models import Deltager
from .forms import BuyTickets
from django.urls import reverse_lazy
from django.utils import timezone
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def GetTicketsView(request):
    form = BuyTickets()
    player_tickets=[]
    my_tickets=[]
    players={}
    if request.method == 'POST':
    	form=BuyTickets(request.POST)
    	if form.is_valid():
    		post = form.save(commit=False)
    		post.owner = request.user
    		post.kjopt_dato=timezone.now()
    		lodd = post.antall_lodd
    		for x in range(lodd):
    			l1=random.randint(1,2000000)
    			t=Tickets(my_tickets=l1, trekknings_dato=timezone.now(), lot=request.user)
    			print (t.my_tickets)
    			t.save()
    		post.save()
    	elif form.is_valid() != True:
    		print ('ooops!')
    form = BuyTickets()
    return render(request, 'draw/draw_form.html', {'form': form})

class AllTickets(ListView):
 	model=Sjanse
 	#context_object_name = 'my_t'

 	def get_queryset(self):
 		queryset = Sjanse.objects.filter(kjopt_dato=timezone.now())
 		return queryset

class MyTickets(LoginRequiredMixin, ListView):
	model = Sjanse
	template_name='draw/my_tickets.html'

	def get_queryset(self):
		queryset = Sjanse.objects.filter(owner_id=self.request.user)
		return queryset

	def get_context_data(self,**kwargs):
 		context = super().get_context_data(**kwargs)
 		context['my_t']=Tickets.objects.filter(trekknings_dato=timezone.now(), lot_id=self.request.user)
 		context['tz']= timezone.now()
 		return context

class CollectTickets(TemplateView):
	template_name = 'draw/collect_tickets.html'
	#tickets_a={}
	context={}
	winning_ticket=0

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		queryset = Tickets.objects.filter(trekknings_dato=timezone.now())
		tickets_a=[]
		for t in queryset:
			tickets_a.append(t.my_tickets)
		context['lodd']=tickets_a
		return context

@login_required
def draw_winner(request):
    winning_ticket=0
    tickets_a=[]
    context={}

    if request.method=='POST':
        queryset = Tickets.objects.filter(trekknings_dato=timezone.now(), valid=True)
        for t in queryset:
            tickets_a.append(t.my_tickets)
        context['lodd']=tickets_a
        winning_ticket=random.choice(tickets_a)
        tic = Tickets.objects.get(my_tickets=winning_ticket)
        context['winning_person'] = tic.lot
        context['winner']= winning_ticket
        tic.valid=False
        tic.save()
    else:
        print ('oh no')
    return render(request,'draw/winner.html', context)


