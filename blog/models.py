from django.db import models

from blog import validators


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre del grupo'
    )
    icon = models.ImageField(
        upload_to='icons/',
        verbose_name='Ícono',
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Grupos'
        ordering = ['name']
        
        
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre de la categoría'
    )
    icon = models.ImageField(
        upload_to='icons/',
        verbose_name='Ícono',
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        

class Link(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        verbose_name='Link o Red social'
    )
    icon = models.ImageField(
        upload_to='icons/',
        verbose_name='Ícono',
    )
    url = models.URLField(
        verbose_name='URL'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
    
        
class Duration(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField(
        verbose_name='Duración (en minutos)'
    )
    
    def __str__(self):
        return f"{self.value} min"
    
    class Meta:
        verbose_name = 'Duración'
        verbose_name_plural = 'Duraciones'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=100,
        verbose_name='Título del post'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Grupo'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Categoría'
    )
    duration = models.ForeignKey(
        Duration,
        on_delete=models.CASCADE,
        verbose_name='Duración (en minutos)'
    )
    text = models.TextField(
        verbose_name='Texto del post',
        null=True,
        blank=True,
    )
    links = models.ManyToManyField(
        Link,
        verbose_name='Links relacionados y redes sociales',
        blank=True,
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Imagen',
        null=True,
        blank=True,
    )
    audio_link = models.URLField(
        verbose_name='Audio',
        null=True,
        blank=True,
    )
    video_link = models.URLField(
        verbose_name='Video',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
        editable=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización',
        editable=True,
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'