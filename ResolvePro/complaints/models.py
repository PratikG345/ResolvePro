from django.db import models
from clients.models import Client


# Create your models here.
class Resident(models.Model):
    flat_no = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.flat_no} - {self.client.name}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}({self.client.name})"

class Job(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('ASSIGNED', 'Assigned'),
        ('RESOLVED', 'Resolved'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to="complaintphotos/")
    assigned_vendor = models.ForeignKey('vendors.Vendor', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.client.name} - {self.resident.flat_no} - {self.status}"
