from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('authors/', views.authors, name='authors'),
    path('authors/details/<str:id>', views.details, name='details'),
    path('authors/add/', views.add_author, name='add_author'),
    path('authors/edit/<int:author_id>', views.edit_author, name='edit_author'),
    path('authors/delete/<int:author_id>', views.delete_author, name='delete_author'),
    path('opera/', views.opera, name='opera'),
    path('opera/add/', views.add_work, name='add_work'),
    path('opera/add/<int:author_id>', views.add_work, name='add_work'),
    path('opera/edit/<int:work_id>', views.edit_work, name='edit_work'),
    path('opera/delete/<int:work_id>', views.delete_work, name='delete_work'),
]