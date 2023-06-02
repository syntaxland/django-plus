


# Using Django Func-Based Views

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def index(request):
    return render(request, 'books/index.html')

# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books': books})

# # def book_create(request):
# #     form = BookForm(request.POST or None)
# #     if form.is_valid():
# #         form.save()
# #         return redirect('book_list')
# #     return render(request, 'books/book_form.html', {'form': form})

# def book_create(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'books/book_form.html', {'form': form})

# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/book_detail.html', {'book': book})

# def book_update(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     form = BookForm(request.POST or None, instance=book)
#     if form.is_valid():
#         form.save()
#         return redirect('book_list')
#     return render(request, 'books/book_form.html', {'form': form})

# def book_delete(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request, 'books/book_confirm_delete.html', {'book': book})

# def search(request):
#     if request.method == 'POST':
#         query = request.POST.get('q')
#         if query:
#             results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
#             return render(request, 'books/search_results.html', {'results': results})
#         else:
#             results = []
#     return render(request, 'books/book_list.html')



# Using django.views.generic (Class-Based Views)

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm, BookSearchForm

from django.shortcuts import render
from django.db.models import Q

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    # context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

class BookSearchView(FormView):
    template_name = 'books/search_results.html'
    form_class = BookSearchForm

    def form_valid(self, form):
            query = form.cleaned_data['query']
            if query:
                results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
                return self.render_to_response(self.get_context_data(form=form, results=results))
            else:
                results = []
            return self.render_to_response(self.get_context_data(form=form, results=results))









# Using rest_framework, generics & serializer class

# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
