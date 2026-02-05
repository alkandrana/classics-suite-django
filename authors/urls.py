from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('authors/', views.authors, name='authors'),
    path('authors/details/<str:id>', views.details, name='details'),
]