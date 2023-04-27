from django.contrib import admin
from .models import Category, TodoList
# Register your models here.

admin.site.register(Category)
admin.site.register(TodoList)