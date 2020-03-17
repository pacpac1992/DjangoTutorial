from django.db import models

# Create your models here.
class Clientes(models.Model):
	nombre = models.CharField(max_length=50)
	email  = models.EmailField()
	tfno   = models.CharField(max_length=50)
	direccion   = models.CharField(max_length=200)

	def __str__(self):
		return 'Nombre: %s, Email: %s, Telefono: %s, Direccion: %s' % (self.name,self.email,self.tfno,self.direccion)
	

class Articulos(models.Model):
	nombre  = models.CharField(max_length=50)
	seccion = models.CharField(max_length=50)
	precio  = models.IntegerField()

class Pedidos(models.Model):
	numero  = models.CharField(max_length=50)
	fecha   = models.DateField()
	entregado = models.BooleanField()