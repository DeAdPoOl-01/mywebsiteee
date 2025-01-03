from django.db import models

# Create your models here.
from django.db import models



# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=60)
    smtp_email = models.EmailField(max_length=40)
    smtp_password = models.CharField(max_length=150)
    smtp_port = models.CharField(max_length=90)
    youtube = models.URLField(blank=True, null=True)
    Istagramm = models.URLField(blank=True, null=True)
    Facebook = models.URLField(blank=True, null=True)
    icon = models.CharField(blank=True, upload_to='images/')
    aboutus = models.CharField(blank=True, max_length=250)
    contact = models.CharField(blank=True, max_length=250)

    def __str__(self):
        return self.title 
