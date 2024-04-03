from django.db import models
from django.urls import reverse

# Create your models here.

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    release_year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})