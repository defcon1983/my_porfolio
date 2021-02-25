from django.db import models

# Create your models here.


class Welcome(models.Model):
    encabezado = models.CharField(max_length = 150)
    biografia = models.CharField(max_length = 3000)
    contenido = models.CharField(max_length = 10000)
    
    
class Project(models.Model):
    titulo = models.CharField(max_length = 150)
    descripcion = models.CharField(max_length = 150)
    contenido = models.CharField(max_length = 10000)
    img = models.ImageField(upload_to='project', height_field=None, width_field=None, max_length=100)

class Error404(models.Model):
    error404 = models.ImageField(upload_to='error404', height_field=None, width_field=None, max_length=100)
    
class Skill(models.Model):
    titulo = models.CharField(max_length = 150)
    descripcion = models.CharField(max_length = 150)
    contenido = models.CharField(max_length = 10000)
    img = models.ImageField(upload_to='skill', height_field=None, width_field=None, max_length=100)
    elegir_icon = {
        ('icon solid major fa-code', 'icon solid major fa-code'),
        ('icon solid major fa-lock', 'icon solid major fa-lock'),
        ('icon solid major fa-cog', 'icon solid major fa-cog'),
        ('icon solid major fa-desktop', 'icon solid major fa-desktop'),
        ('icon solid major fa-link', 'icon solid major fa-link'),
        ('icon major fa-gem', 'icon major fa-gem')
    }
    icon = models.CharField(max_length = 150, choices=elegir_icon)
    
class Contact(models.Model):
    nombre = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    mensaje = models.CharField(max_length = 150)

class Social_network(models.Model):
    facebook = models.CharField(max_length = 150)
    youtube = models.CharField(max_length = 150)
    git = models.CharField(max_length = 150)
    Linkedin = models.CharField(max_length = 150)
    
class My_data(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()

