from django.db import models

# Create your models here. 
class Contact(models.Model):
    name = models.CharField(max_length =30)
    email = models.CharField(max_length =65)
    phone = models.CharField(max_length =30)
    desc = models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name
    

