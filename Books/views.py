# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from .models import Book
from django.http import JsonResponse
from .forms import BookForm
from django.template.loader import render_to_string
from rest_framework import viewsets
from  .serializers import BookSerializer


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'book_list': books})


def save_book_form(request,form, templete_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            data['form_is_valid']=True
            books=Book.objects.all()
            data['html_book_list']=render_to_string('books/includes/partial_book_list.html',
                                                    {
                                                        'book_list': books
                                                    })
        else:
            data['form_is_valid']=False

    context={
        'form':form,
    }
    data['html_form']=render_to_string(templete_name,
                               context=context,
                               request=request
                               )
    return JsonResponse(data)


def book_create(request):
    if request.method=='POST':
        form=BookForm(request.POST)
    else:
        form=BookForm()
    return save_book_form(request,form,'books/includes/partial_book_create.html')


def book_update(request,pk):
    book=get_object_or_404(Book,pk=pk)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
    else:
        form=BookForm(instance=book)
    return save_book_form(request,form,'books/includes/partial_book_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
            'book_list': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/includes/partial_book_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


def dataTable(request):
    return render(request,'books/book-datatable.html')