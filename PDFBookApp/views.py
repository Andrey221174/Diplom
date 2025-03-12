# from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Book
# # Create your views here.

# def index(request):
#     return render(request, "PDFBookApp/index.html")



# class BookListView(ListView):
#     model = Book
#     template_name = 'library/book_list.html'
#     context_object_name = 'books'

from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

class BookListView(ListView):
    model = Book
    template_name = 'PDFBookApp/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(title__icontains=query)  # Поиск по заголовку
        return queryset

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'PDFBookApp/register.html'
    success_url = reverse_lazy('login')

class UserLogin(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'PDFBookApp/login.html'
    next_page = reverse_lazy('PDFBookApp:book-list')
