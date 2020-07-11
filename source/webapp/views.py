from django.shortcuts import render, redirect

from webapp.models import Book


def index_view(request, *args, **kwargs):
    books = Book.objects.all()
    return render(request, 'index.html', context={
        'books': books

    })


# def book_create_view(request, *args, **kwargs):
#     if request.method == "GET":
#         form = ProductForm()
#         return render(request, 'create.html', context={'form': form})
#     elif request.method =='POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             book = Book.objects.create(
#                 name=form.cleaned_data['name'],
#                 description=form.cleaned_data['description'],
#                 category=form.cleaned_data['category'],
#                 amount=form.cleaned_data['amount'],
#                 price=form.cleaned_data['price']
#
#             )
#             return redirect('product_detail', pk=book.pk)
#         else:
#             return render(request, 'create.html', context={'form': form})
#
