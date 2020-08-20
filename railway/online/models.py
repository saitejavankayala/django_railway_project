from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse



class station(models.Model):
    station_id = models.CharField(max_length=200)
    station_name = models.CharField(max_length=200)


class train(models.Model):
    train_name = models.CharField(max_length=200, blank=False, null=False)
    train_id = models.CharField(max_length=200, blank=False, null=False, primary_key=True)
    startpoint = models.CharField(max_length=200, blank=False, null=False)
    endpoint = models.CharField(max_length=200, blank=False, null=False)
    stops = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    days = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    seats= ArrayField(models.IntegerField(), blank=True, default=list)
    seattype= ArrayField(models.CharField(max_length=120), blank=True, default=list)



    def get_absolute_url(self):
        return reverse('train_edit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.train_id
