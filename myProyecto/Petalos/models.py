from django.db import models

# Create your models here.
class Floreria(models.Model):
    name=models.CharField(max_length=100,primary_key=True,null=False)
    valor=models.IntegerField(null=True)
    descripcion=models.TextField(null=True)
    estado=models.CharField(max_length=10,null=True)
    stock=models.IntegerField(null=True)
    fotografia=models.ImageField(upload_to="flores",null=True)
    
    def __str__(self):
        return self.name
    
class Ticket(models.Model):
    usuario=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    total=models.IntegerField()
    fecha=models.DateField()

    def __str__(self):
        return str(self.usuario)+' '+str(self.nombre)