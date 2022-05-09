from django.contrib.auth.models import User
from django.db import models
from asosiy.models import Product

class Mijoz(models.Model):
    ism = models.CharField(max_length=40)
    tel = models.CharField(max_length=13)
    manzil = models.CharField(max_length=40)
    zipcode = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.ism

class Comment(models.Model):
    matn = models.TextField()
    baho = models.PositiveSmallIntegerField(default=5)
    sana = models.DateTimeField(auto_now_add=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null = True)
    mahsulot = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.matn