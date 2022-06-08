"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from book_app import views

#urls of the project / application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view_students,name="view_students"),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:id>", views.edit_book, name="edit_book"),
    path("delete_book/<int:id>", views.delete_book, name="delete_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("view_students/", views.view_students, name="view_students"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),
    path('signup/', views.signup, name='signup'),
]    

