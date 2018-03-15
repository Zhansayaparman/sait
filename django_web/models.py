from django.db import models

# Create your models here.
from django.urls import reverse

class Kinoteatr(models.Model):
    kino_name = models.CharField(max_length=200, help_text=" ")
    kino_address = models.CharField(max_length=200, help_text=" ")
    kino_janr = models.CharField(max_length=200, help_text=" ")
    phone_number = models.IntField(null=True, blank=True)

    class Meta:
        ordering = ["kino_name", "kino_address"]


    def get_absolute_url(self):
        return reverse('kino-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.kino_name, self.kino_address)


class Client(models.Model):
    name = models.CharField(max_length=200, help_text=" ")
    kinotet= models.CharField(max_length=200, help_text=" ")


    class Meta:
        ordering = ["name","kinotet"]

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.name,self.kinotet)

