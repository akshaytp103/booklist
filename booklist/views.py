from django.shortcuts import render
from .models import Book



# def book_list(request):
#     query = request.GET.get('q')
#     if query:
#         books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
#     else:
#         books = Book.objects.all()
#     return render(request, 'book_list.html', {'books': books, 'query': query})


from django.shortcuts import render
from django.db.models import Q
from .models import Book

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    context = {'books': books}
    return render(request,'home.html', context)

