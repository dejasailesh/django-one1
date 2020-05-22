from django.db import models

# Create your models here.
class BaseContent(models.Model):
    intro = models.TextField(max_length=100)
    about = models.TextField(max_length=100)
    mission = models.TextField(max_length=200)
    vision = models.TextField(max_length=100)
    footer = models.TextField(max_length=60)


class Contact(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=100)
    myemail = models.EmailField(max_length=100)
    myphn = models.CharField(max_length=10)
    myadd = models.CharField(max_length=30)

    def __str__(self):
        return self.name
