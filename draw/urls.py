from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import GetTicketsView, AllTickets, MyTickets, CollectTickets, draw_winner


urlpatterns = [
	#path('', TicketsView.as_view(), name='tickets'),
	path('', GetTicketsView, name='tickets'),
	path('all_tickets/', AllTickets.as_view(), name='all_tickets'),
	path('my_tickets/', MyTickets.as_view(), name='my_tickets'),
	path('collect_tickets/', CollectTickets.as_view(), name='collect_tickets'),
    path('winner/', draw_winner,name='draw_winner'),
]
