from django.views import generic
from django.urls import reverse_lazy
from .models import *

class RegistrateUser(generic.CreateView):
    model = User
    fields = ["first_name","last_name","username","phone_number","email","password"]
    template_name = "user_form.html"
    success_url = reverse_lazy("Base-Page")

class RegisteredUserListView(generic.ListView):
    model = User
    fields = ["first_name","last_name","username","phone_number","email","password"]
    template_name = "users_view.html"

class DetailUser(generic.DetailView):
    model = User
    template_name = "detail_user.html"

class MoviesView(generic.ListView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "base.html"

class AddTrailer(generic.CreateView):
    model = Trailer
    fields = ["name","trailer_video"]
    template_name = "create_movie_trailerform.html"
    success_url = reverse_lazy("Base-Page")
    
class WatchTrailer(generic.DetailView):
    model = Trailer
    template_name = "watch_trailer.html"
    context_object_name = 'trailer'
    

class OrderMovieTicket(generic.CreateView):
    model = Order
    fields = ["payment_type", "user", "movie", "amount_ticket"]
    template_name = "Order_ticket_movie.html"
    success_url = reverse_lazy("Base-Page")
  

class ConfOrderTicket(generic.TemplateView):
    template_name = "conf_order.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.request.session.get('order') 
        return context

class CreateMovie(generic.CreateView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "MovieForm.html"
    success_url = reverse_lazy("Base-Page")

class DetailMovieView(generic.DetailView):
    model = Movie
    template_name = "detail_movie.html"
  

class EditMovie(generic.UpdateView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "MovieForm.html"
    success_url = reverse_lazy("Base-Page")

class DeleteMovie(generic.DeleteView):
    model = Movie
    fields = ["name","description","janre","photo","trailer","bio","theater"]
    template_name = "ConfDeleteMovie.html"
    success_url = reverse_lazy("Base-Page")

class TheaterDetailView(generic.ListView):
    model = Theater
    template_name = "theater_detail.html"
    context_object_name = "theater"

class OrdersListView(generic.ListView):
    model = Order
    template_name = "orders_list.html"
    fields = ["payment_type","user","movie","amount_price"]
    
    
    

class CreateBio(generic.CreateView):
    model = Bio
    fields = ["name","description","publication_date"]
    template_name = "bio_form.html"
    success_url = reverse_lazy("Base-Page")

class MoviebyJanre(generic.ListView):
    model = Movie
    template_name = "movies_by_janre.html"
    def get_queryset(self):
        return Movie.objects.filter(janre_id = self.kwargs['pk'])
    
