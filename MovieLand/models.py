from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


class Trailer(models.Model):
    trailer_video = models.FileField(upload_to='static/trailer_file')
    created_at = models.DateTimeField(auto_now=True)

class Bio(models.Model):
    description = models.TextField()
    publication_date = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    janre = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='static/movie_imgs')
    trailer = models.ForeignKey("MovieLand.Trailer",on_delete=models.CASCADE)
    bio = models.ForeignKey("MovieLand.Bio",on_delete=models.CASCADE)
    theater = models.ForeignKey("MovieLand.Theater",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Order(models.Model):
    payment_type = models.CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    movie_id = models.ForeignKey("MovieLand.Movie",on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_ticket = models.IntegerField()
    order_date = models.DateTimeField(auto_now=True)

class Theater(models.Model):
    name = models.CharField(max_length=50)
    desciption = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)



