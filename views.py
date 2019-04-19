from django.views import generic
from django.template import Context, Template
from .models import Book
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic.base import TemplateView



class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'book_list'


    def dispatch(self, args):
        return super(IndexView, self).dispatch(args)


    def get_queryset(self):
        return Book.objects.all()




class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'
