from django.urls import path 
from .views import *

urlpatterns = [
    path("",MoviesView.as_view(),name="Movies-List"),
    path("createmovie>",CreateMovie.as_view(),name="Create-Movie"),
    path("editmovie/<int:pk>",EditMovie.as_view(),name="Edit-Movie"),
    path("detailmovie/<int:pk>",DetailMovieView.as_view(),name="Detail-Movie"),
    path("deletemovie/<int:pk>",DeleteMovie.as_view(),name="Detail-Movie"),
    

]
