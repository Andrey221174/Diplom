from django import forms
from .models import Book, CustomUser

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pdf_file']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['bio', 'profile_picture']