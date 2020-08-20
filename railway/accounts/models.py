from django.db import models


class registration(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    mid_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False, primary_key=True)
    secques = models.CharField(max_length=200, null=False)
    secans = models.CharField(max_length=200, null=False)
    prflanguage = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=200, null=False)
    dofbir = models.CharField(max_length=200, null=False)
    occupation = models.CharField(max_length=200, null=False)
    maritalstatus = models.CharField(max_length=200, null=False)
    countryname = models.CharField(max_length=200, null=False)
    prflanguage = models.CharField(max_length=200, null=False)
    mobileno = models.IntegerField(max_length=200, null=False)
    nationality = models.CharField(max_length=200, null=False)
    doorno = models.CharField(max_length=200, null=False)
    street = models.CharField(max_length=200, null=False)
    Area = models.CharField(max_length=200, null=False)
    pincode = models.IntegerField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    town = models.CharField(max_length=200, null=False)
    postoffice = models.CharField(max_length=200, null=False)
    ResitoOffAddr = models.CharField(max_length=200, null=False)
    phoneno = models.IntegerField(max_length=200, null=False)






