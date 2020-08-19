# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class Topic(models.Model):

    
    text = models.CharField(max_length=200, verbose_name='Tytuł artykułu')
    key_words = models.TextField(verbose_name='Słowa kluczowe', default='Tu możesz dodać słowa kluczowe, a nawet całe artykuły')
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
    width = models.CharField(max_length=200, verbose_name='Szerokość zdjęcia', default='400')
    height = models.CharField(max_length=200, verbose_name='Wysokość zdjęcie', default='300')
    foto = models.CharField(max_length=200, verbose_name='Zdjęcie', default='link do zdjęcia')


    class Meta:
        verbose_name_plural = 'Artykuły'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.text[:50]+'...'


class Newsletter(models.Model):
    first_name 		= models.CharField(max_length=50, verbose_name='Twoje imię')
    email 		= models.EmailField(blank=False, verbose_name='Twój e-mail')
    regulamin_1 	= models.BooleanField(default=False, verbose_name='Chcę zapisać się do newslettera, a co za tym idzie wyrażam zgodę na otrzymanie na mój adres e-mail informacji o działalności Zanurzeni w zieleni.')
    date_added          = models.DateTimeField(auto_now_add=True)

   
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.email
