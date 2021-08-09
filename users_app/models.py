from django.db import models

class Users(models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    edad = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'{self.nombre} {self.apellido}'
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
