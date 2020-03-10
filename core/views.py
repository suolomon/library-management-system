from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (TemplateView,
	                              ListView,
	                              DetailView,
	                              UpdateView,
	                              )

from django.views.generic.edit import CreateView

from .models import Client, Book_store


class InStore(LoginRequiredMixin, ListView):
	model = Book_store

	template_name = 'book_store.html'

	login_url = 'login'


class BookList(LoginRequiredMixin,CreateView, ListView):
	queryset = Client.objects.order_by('book_title')

	template_name = 'booklist.html'

	fields = '__all__'

	login_url = 'login'


class LendBook(CreateView):
	model = Client

	template_name = 'lendbook.html'

	fields='__all__'

	success_url = reverse_lazy('lendbook')


class BooksTaken(ListView):
	queryset = Client.objects.filter(status = 'taken').order_by('book_title')

	template_name = 'bookstaken.html'
	

class Returner(DetailView,UpdateView):
	model = Client

	template_name = 'return.html'

	fields=('status',)

	success_url = reverse_lazy('booklist')


class BookDetails(DetailView):
	model = Book_store

	template_name = 'bookdetails.html'