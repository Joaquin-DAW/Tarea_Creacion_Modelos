from django.conf import settings
from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.CharField(max_length=250, unique=True)
    contrasenia = models.CharField(max_length=250, null=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()

    usuarios_asignados = models.ManyToManyField(Usuario, related_name='proyectos_asignados')
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    
class Tarea(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    ]
    
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    completada = models.BooleanField()
    fecha_creacion = models.DateField()
    hora_vencimiento = models.DateTimeField()
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')
    etiquetas_asociadas = models.ManyToManyField(Etiqueta)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    
class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField()
    
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)