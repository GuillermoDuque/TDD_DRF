from django.urls import path

from movies.views.views import MovieList, MovieDetail
from movies.views.dogs_views import DogList

urlpatterns = [
    path("api/movies/", MovieList.as_view()),
    path("api/movies/<int:pk>/", MovieDetail.as_view()),
    path("api/dog/", DogList.as_view()),
]