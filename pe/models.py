from django.db import models

# Create your models here.
class BaseContent(models.Model):
    intro = models.TextField(max_length=300)
    about = models.TextField(max_length=350)
    mission = models.TextField(max_length=250)
    vision = models.TextField(max_length=300)
    footer = models.TextField(max_length=60)


class Contact(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=100)
    myemail = models.EmailField(max_length=100)
    myphn = models.CharField(max_length=10)
    myadd = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.TextField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServiceField(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    field = models.TextField(max_length=50,)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field


class Career(models.Model):
    name = models.TextField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CareerField(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    field = models.TextField(max_length=60,)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field

    def get_absolute_url():
        return reverse("career_detail", args=[str(self.id)])


class PortFolio(models.Model):
    name = models.TextField(max_length=50)
    logo = models.ImageField(upload_to="image/products_pics", blank=False)

    def __str__(self):
        return self.name

