from django.urls import path
from . import views
from .views import BookListView, UserRegisterView, UserLogin
from django.contrib.auth import views as auth_views


app_name = 'PDFBookApp'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]



