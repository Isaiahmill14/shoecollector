from django.db import models
from django.urls import reverse
from datetime import date

# Tuple
RARITIES = (
    ('N', 'New'),
    ('P', 'Previously Owned'),
    ('M', 'Multiple Owners'),
)

# Create your models here.

class Cleaning_Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cleaning_products_detail', kwargs={'pk': self.id})

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    release_year = models.IntegerField()
    price = models.IntegerField()
    # Add M:M relationship
    cleaning_products = models.ManyToManyField(Cleaning_Product)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})
    
    def history_assigned(self):
        return self.history_set.filter(date=date.today()).count() >= 1
    
class History(models.Model):
    date = models.DateField('log date')
    rarity = models.CharField(
        max_length=30, 
        choices=RARITIES, 
        default=RARITIES[0][0]
    )
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rarity_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']