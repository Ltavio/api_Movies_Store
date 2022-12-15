from django.contrib import admin
from django.urls import path
from . import views

# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("movies/", views.MoviesViews.as_view()),
    path("movies/<int:movie_id>/", views.MoviesDetailViews.as_view()),
    path("movies/<int:movie_id>/orders/", views.MovieOrderViews.as_view()),
]
