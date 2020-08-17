# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class Topic(models.Model):

    
    text = models.CharField(max_length=200, verbose_name='Tytuł artykułu')
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tematy'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.text  
 

class Entry(models.Model):    
# Create your models here.
    topic = models.ForeignKey(Topic, verbose_name='Tytuł artykułu')
    text = models.TextField(verbose_name='Tekst artykułu')
	
    date_added = models.DateTimeField(auto_now_add=True)
    width = models.CharField(max_length=200, verbose_name='Szerokość zdjęcia', default='100%')
    height = models.CharField(max_length=200, verbose_name='Wysokość zdjęcie', default='20%')
    foto = models.CharField(max_length=200, verbose_name='Zdjęcie', default='link do zdjęcia')


    class Meta:
        verbose_name_plural = 'Artykuły'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.text[:50]+'...'


