from django.urls import path
from . import views
from BookDatabase.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('search/',views.search, name = 'search' ),
    path('search/searchdata/', views.searchdata, name='searchdata' ),
    path('signup/', views.signup_part),
    path('login/', views.login_part),
    path('deny/', views.danger),
    path('logout/',views.logout)
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)