# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Topic 
from .models import Entry


def home(request):

    
	return render(request, 'apka/base.html')



def topics(request):

        topics = Topic.objects.order_by('date_added')
        context = {'topics': topics}
        return render(request, 'apka/topics.html', context)


def topic(request, topic_id):
    """Display a single topic and all its entries"""
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    width=topic.entry_set.order_by('-date_added')
    height=topic.entry_set.order_by('-date_added')
    foto=topic.entry_set.order_by('-date_added')
    
    x={'topic':topic,'entries':entries,'width':width,'height':height,'foto':foto}
    return render(request, 'apka/topic.html', x)		
