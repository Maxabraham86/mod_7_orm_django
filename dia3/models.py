from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion= models.TextField(default='', unique = True)
    eliminada = models.BooleanField(default=False)
    # atributo fantasma
    #subtareas=[SubTarea 1, SubTarea 2, ...]
    
class SubTarea(models.Model):
    descripcion= models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea= models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE)
    
    # st5= SubTarea.objects.get(5) # pregunto por la subtarea 5
    # st5.tarea.descripcion # veo a que tarea pertenece la subtarea 5
    
    # #si queremos iterar y ver que subtarea pertence a una tarea
    # t2 = Tarea.objects.get(2)
    # for sub_tarea in t2.subtareas:
    #     print (f'Una de las subtaras de t2 es {sub_tarea.descripcion}')