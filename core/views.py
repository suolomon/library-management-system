from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (TemplateView,
	                              ListView,
	                              DetailView,
	                              UpdateView,
	                              DeleteView)
from django.views.generic.edit import CreateView
from .models import client, book_store


class In_store(LoginRequiredMixin, ListView):
	model= book_store
	template_name= 'book_store.html'

class booklist(LoginRequiredMixin,CreateView, ListView):
	model=book_store
	booker=book_store.objects.all()
	queryset=client.objects.order_by('book_title')
	template_name= 'booklist.html'
	fields='__all__'
	success_url = reverse_lazy('booklist')
	login_url='login'

class lendbook(CreateView):
	model= client
	template_name= 'lendbook.html'
	fields='__all__'
	success_url = reverse_lazy('lendbook')

class bookstaken(ListView):
	queryset=client.objects.filter(status='taken').order_by('book_title')
	template_name= 'bookstaken.html'
	

class returner(DetailView,UpdateView):
	model= client
	template_name= 'return.html'
	fields=('status',)
	success_url = reverse_lazy('booklist')

class bookdetails(DetailView):
	model= book_store
	template_name= 'bookdetails.html'
	
