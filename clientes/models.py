from django.db import models


class Person(models.Model):
    Nome = models.CharField(max_length=30)
    Sobrenome = models.CharField(max_length=30)
    Idade = models.IntegerField()
    Salário = models.DecimalField(max_digits=7, decimal_places=2)
    Descrição = models.TextField()
    Foto = models.ImageField(upload_to='clients_photos', null=True, blank=True) # O null e o blank=True é para tornar o campo opcional.

    def __str__(self):
        return self.Nome + ' ' + self.Sobrenome


