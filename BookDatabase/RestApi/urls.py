from django.urls import path
from .views import *

urlpatterns = [
    path('books',view_get_post_book),
    path('books/<int:ID>',view_getByID_updateByID_deleteByID),
    path('books/delete/<int:ID>', api_delete_data),
    path('books/update/<int:ID>', api_update_data),
    path('books/page/<int:PAGENO>', api_book_pagination),
    
]

