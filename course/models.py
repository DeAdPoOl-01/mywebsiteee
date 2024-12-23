from django.db import models

# Create your models here.
from django.db import models



# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(null = False, upload_to='images/')
    slug = models.SlugField(null = False, unique=True)

    def __str__(self):
        return self.title

from django.db import models



# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(null = False, upload_to='images/')
    slug = models.SlugField(null = False, unique=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=100)
    subject_tutor = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, upload_to='images/')
    price = models.CharField(max_length=150)
    detail = models.CharField(max_length=300)
    slug = models.SlugField(null=False, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

