from django.db import models


# Create your models here.


class MyModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    user = models.OneToOneField(MyModel, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
