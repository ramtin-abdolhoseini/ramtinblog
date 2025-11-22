from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField()
    subject=models.CharField()
    email=models.EmailField()
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    class Meta:
        ordering=['created_date']
    def __str__(self):
        return f"{self.id}- {self.name}"  
    

class newsletter(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email