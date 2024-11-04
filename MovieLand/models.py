from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50,null=True)
    registered_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

class Trailer(models.Model):
    name = models.CharField(max_length=50,null=True)
    trailer_video = models.FileField(upload_to='static/trailer_file')
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Trailer {self.name}"

class Bio(models.Model):
    name = models.CharField(max_length=50,null=True)
    description = models.TextField()
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f"Name:{self.name} Description:{self.description} Public:{self.publication_date}"

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
    def __str__ (self):
        return f"{self.name}"


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('Online', 'Online'),
        ('Cash', 'Cash')
    ]
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey("MovieLand.Movie", on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_ticket = models.IntegerField()
    order_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.user}"

class Theater(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name



