from django.db import models
from complaints.models import Client,Category
# Create your models here.

class Vendor(models.Model):
    
    name = models.CharField(max_length=100)
    comtact_no = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} - {self.category.name}"
