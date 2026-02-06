from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('authors/', views.authors, name='authors'),
    path('authors/details/<str:id>', views.details, name='details'),
    path('authors/add/', views.add_author, name='add_author'),
    path('authors/edit/<int:author_id>', views.edit_author, name='edit_author'),
    path('authors/delete/<int:author_id>', views.delete_author, name='delete_author'),
]