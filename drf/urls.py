from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.book_list, name='book_list'),
#     path('create/', views.book_create, name='book_create'),
#     path('<int:pk>/', views.book_detail, name='book_detail'),
#     path('<int:pk>/update/', views.book_update, name='book_update'),
#     path('<int:pk>/delete/', views.book_delete, name='book_delete'),
#     path('search/', views.search, name='search'),
# ]


from django.urls import path
from .views import BookListView, \
                    BookCreateView, BookDetailView, \
                    BookUpdateView, BookDeleteView, \
                    BookSearchView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('search/', BookSearchView.as_view(), name='search_results'),

    path('index/', views.index, name='index'),
]


# from django.urls import path
# from .views import BookListCreateView, BookRetrieveUpdateDeleteView

# urlpatterns = [
#     path('books/', BookListCreateView.as_view(), name='book-list'),
#     path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
# ]
