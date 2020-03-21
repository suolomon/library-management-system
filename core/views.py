from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Client, BookStore


class InStore(LoginRequiredMixin, ListView):
    model = BookStore
    template_name = 'book_Store.html'


class BookList(LoginRequiredMixin, CreateView, ListView):
    model = BookStore
    queryset = Client.objects.order_by('book_title')
    template_name = 'booklist.html'
    fields = '__all__'
    success_url = reverse_lazy('booklist')
    login_url = 'login'

    def get_context_data(self,**kwargs):
        context = super(BookList,self).get_context_data(**kwargs)
        context['total_books'] = self.model.objects.all().count()
        return context


class LendBook(CreateView):
    model = Client
    template_name = 'lendbook.html'
    fields = '__all__'
    success_url = reverse_lazy('lendbook')


class BooksTaken(ListView):
    queryset = Client.objects.filter(status='taken').order_by('book_title')
    template_name = 'bookstaken.html'


class Returner(DetailView, UpdateView):
    model = Client
    template_name = 'return.html'
    fields = ('status',)
    success_url = reverse_lazy('booklist')


class BookDetails(DetailView):
    model = BookStore
    template_name = 'bookdetails.html'
