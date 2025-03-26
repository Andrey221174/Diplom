from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class CustomUser (AbstractUser ):
    # Ваши дополнительные поля
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    marked_books = models.ManyToManyField('Book', related_name='marked_by', blank=True)
    # Указываем уникальные имена для обратных связей
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Измените это имя на уникальное
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Измените это имя на уникальное
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

