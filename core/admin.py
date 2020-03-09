from django.contrib import admin

from .models import client,book_store

admin.site.register(client)
admin.site.register(book_store)