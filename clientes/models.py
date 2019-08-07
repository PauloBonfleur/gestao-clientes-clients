from django.db import models


class Documento(models.Model):
    new_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.new_doc


class Person(models.Model):
    Nome = models.CharField(max_length=30)
    Sobrenome = models.CharField(max_length=30)
    Idade = models.IntegerField()
    Salário = models.DecimalField(max_digits=7, decimal_places=2)
    Descrição = models.TextField()
    Foto = models.ImageField(upload_to='clients_photos', null=True, blank=True) # O null e o blank=True é para tornar o campo opcional.
    Documento = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome + ' ' + self.Sobrenome


class Produto(models.Model):
    descrição = models.CharField(max_length=100)
    preço = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.descrição


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    desconto = models.DecimalField(max_digits=7, decimal_places=2)
    impostos = models.DecimalField(max_digits=7, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.numero

