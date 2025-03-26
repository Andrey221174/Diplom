from django import forms
from .models import Book, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pdf_file']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['bio']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['username', 'email', 'bio']  # Добавлено поле

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
        return cleaned_data