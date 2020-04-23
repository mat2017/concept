from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Concept, Phrase, Token

def home(request):
	context = {
		'first_name': 'Megumi',
		'last_name': 'Tsutsui',
		'concepts': Concept.objects.all(),
		'phrase_list': Phrase.objects.all(),
	}
	return render(request, 'home.html', context)# Create your views here.

class TokenList(ListView):
	model = Token

class TokenDetail(DetailView):
	model = Token

class CreateToken(CreateView):
	model = Token
	fields = ('color', 'concept', 'is_primary')
	success_url = reverse_lazy('token-list')

class UpdateToken(UpdateView):
	model = Token
	fields = ('concept',)
	success_url = reverse_lazy('token-list')
