from django.db import models

class DDD(models.Model):
    ddd = models.CharField(max_length=10)
    def __str__(self):
        return self.ddd

class SiglaEstado(models.Model):
    sigla = models.CharField(max_length=4)
    
    def __str__(self):
        return self.sigla

class Regiao(models.Model):
    A = models.CharField(max_length=200)
    B = models.CharField(max_length=200)
    C = models.CharField(max_length=200)
    
    def __str__(self):
        return self.A