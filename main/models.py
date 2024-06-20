from django.db import models, migrations

# Create your models here.
class Estudiante(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField ( max_length =50)
    apellido= models.CharField ( max_length =50)
    email= models.EmailField ( max_length =50)
    
    
    
class Curso(models.Model):
    cod= models.CharField(max_length=3, primary_key=True)
    nombre= models.CharField ( max_length =255)
    activo= models.BooleanField ( default =False)
    
    
class Adltest(models.Model):
    campo1=  models.CharField(max_length=100)
    valor1= models.IntegerField()