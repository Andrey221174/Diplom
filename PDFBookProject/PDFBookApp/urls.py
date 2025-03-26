from django.urls import path
from . import views
from .views import BookListView, UserRegisterView, UserLogin
from django.contrib.auth import views as auth_views
from .views import upload_book
from .views import profile_view, edit_profile_view, custom_login_view

app_name = 'PDFBookApp'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('login/', custom_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('upload/', upload_book, name='upload-book'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
]



