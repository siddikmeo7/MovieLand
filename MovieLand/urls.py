from django.urls import path 
from .views import *

urlpatterns = [
    path("",MoviesView.as_view(),name="Base-Page"),
    path("registeruser",RegistrateUser.as_view(),name="Register-User"),
    path("detailuser/<int:pk>",DetailUser.as_view(),name="Detail-User"),
    path("seregisteredusers",RegisteredUserListView.as_view(),name="See-Registered-Users"),
    path("detailmovie/<int:pk>",DetailMovieView.as_view(),name="Detail-Movie"),
    path("createmovie",CreateMovie.as_view(),name="Create-Movie"),
    path("editmovie/<int:pk>",EditMovie.as_view(),name="Edit-Movie"),
    path("deletemovie/<int:pk>",DeleteMovie.as_view(),name="Delete-Movie"),
    path("watchtrailer/<int:pk>",WatchTrailer.as_view(),name="Watch-Movie-Trailer"),
    path("orderticketmovie",OrderMovieTicket.as_view(),name="Order-Movie-Ticket"),
    path("addtrailer",AddTrailer.as_view(),name="Add-Trailer"),
    path("conforderticket/<int:pk>",ConfOrderTicket.as_view(),name="Conf-Order-Ticket"),
    path("theaterdetail<int:pk>",TheaterDetailView.as_view(),name="Theater-Detail"),
    path("addbio",CreateBio.as_view(),name="Add-Bio"),
    path("moviesbyjanre/<int:pk>",MoviebyJanre.as_view(),name="Movies-By-Janre"),
]
