"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, book_create_view, book_delete_view, book_update_view, filter_book_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('book/create/', book_create_view, name='book_create'),
    path('book/<int:pk>/delete/', book_delete_view, name='book_delete'),
    path('book/<int:pk>/edit/', book_update_view, name='book_update'),
    path('book/filter/', filter_book_name, name='filter_name')

]
