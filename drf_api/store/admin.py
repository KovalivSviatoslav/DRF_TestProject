from django.contrib import admin

# Register your models here.
from store.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'author')
    list_display = ('name', 'price', 'author')
