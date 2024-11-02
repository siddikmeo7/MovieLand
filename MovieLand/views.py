from django.views import generic
from django.urls import reverse_lazy
from .models import *

class MoviesView(generic.ListView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "base.html"

class CreateMovie(generic.CreateView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "MovieForm.html"
    success_url = reverse_lazy("Movies-List")

class DetailMovieView(generic.DeleteView):
    model = Movie
    template_name = "DetailMovie.html"
  

class EditMovie(generic.UpdateView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "MovieForm.html"
    success_url = reverse_lazy("Movies-List")

class DeleteMovie(generic.DeleteView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "ConfDeleteMovie.html"
    success_url = reverse_lazy("Movies-List")
