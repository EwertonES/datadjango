from django.db import models


class AUser(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.IntegerField()
    b_date = models.DateField()
    email = models.EmailField()
    nickname = models.CharField(max_length=100, blank=True)
    observation = models.CharField(max_length=280, blank=True)