from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(upload_to='bolimlar')

    def __str__(self):
        return self.nom

class Product(models.Model):
    nom = models.CharField(max_length=30)
    batafsil = models.TextField()
    narx = models.IntegerField()
    rasm = models.FileField(upload_to='mahsulotlar')
    chegirma = models.PositiveSmallIntegerField()
    vazn = models.PositiveIntegerField()
    brend = models.CharField(max_length=30)
    mamlakat = models.CharField(max_length=30)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f'{self.nom} ({self.brend})'

