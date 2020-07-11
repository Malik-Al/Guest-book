from django.contrib import admin
from webapp.models import Book

#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'text', 'status']
#     list_filter = ['name', 'status']
#     fields = ['name', 'email', 'text', 'status', 'created_at', 'updated_at']
#     readonly_fields = ['created_at', 'updated_at']
#



admin.site.register(Book)
# admin.site.register(BookAdmin)


