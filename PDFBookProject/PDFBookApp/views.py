from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import BookUploadForm, ProfileForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    success_url = reverse_lazy('PDFBookApp:login')

class UserLogin(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'PDFBookApp/login.html'
    next_page = reverse_lazy('PDFBookApp:book-list')

@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохраните книгу в базе данных
            return redirect('PDFBookApp:book-list')  # Перенаправление на список книг
    else:
        form = BookUploadForm()
    return render(request, 'PDFBookApp/upload_book.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'PDFBookApp/profile.html', {'user': user})

@login_required
def edit_profile_view(request):
    user = request.user  # Получаем текущего пользователя
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('profile')  # Перенаправляем на страницу профиля
    else:
        form = ProfileForm(instance=user)  # Заполняем форму текущими данными
    return render(request, 'PDFBookApp/edit_profile.html', {'form': form})

@login_required
def user_profile_view(request):
    user = request.user
    marked_books = user.marked_books.all()  # Получаем все помеченные книги пользователя
    return render(request, 'PDFBookApp/profile.html', {'marked_books': marked_books})