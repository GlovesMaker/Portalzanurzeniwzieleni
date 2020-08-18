# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from .models import Topic 
from .models import Entry
from django.contrib import messages

import urllib
import urllib2
import json


from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .forms import NewsletterCreateForm

def home(request):

        form = NewsletterCreateForm()
        
        if request.method == 'POST':
                form = NewsletterCreateForm(request.POST)   
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Zostałeś zapisany do newsletter!')
					
                """
                    recaptcha_response = request.POST.get('g-recaptcha-response')
                    url = 'https://www.google.com/recaptcha/api/siteverify'
                    values = {
                        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                        'response': recaptcha_response
                    }
                    data = urllib.urlencode(values)
                    req = urllib2.Request(url, data)
                    response = urllib2.urlopen(req)
                    result = json.load(response)
                    ''' End reCAPTCHA validation '''

                if result['success']:
                        form.save()
                        messages.success(request, 'Zostałeś zapisany do newsletter!')
                        #return HttpResponse("ok");
                else:
                        
                        messages.error(request, 'Nie zostałeś zapisany! Zaznacz pole "Nie jestem robotem"!')
                        #return HttpResponse("Invalid reCAPTCHA. Please try again.");"""
                   
       
        #context = {'form': form }
        #name = {'name': name}
        
        
	return render(request, 'apka/base.html', {'form': form})
	
		

def topics(request):

        topics = Topic.objects.order_by('date_added')
		form = NewsletterCreateForm()
        context = {'topics': topics, 'form': form}
		
	

		
        return render(request, 'apka/topics.html', context)


def topic(request, topic_id):
    """Display a single topic and all its entries"""
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    width=topic.entry_set.order_by('-date_added')
    height=topic.entry_set.order_by('-date_added')
    foto=topic.entry_set.order_by('-date_added')
	form = NewsletterCreateForm()
	
    x={'topic':topic,'entries':entries,'width':width,'height':height,'foto':foto, 'form': form}
    return render(request, 'apka/topic.html', x)		

def search(request):
	form = NewsletterCreateForm()

	if request.method=='POST':
		srch = request.POST['srh']
		if srch:
		
			match = Topic.objects.filter(Q(text__icontains=srch)) 
			#match_1 = Entry.objects.filter(Q(text__icontains=srch)|
										   #Q(text__icontains=srch))
			if match:
				return render(request, 'apka/search.html', {'sr':match})	
			else:
				messages.error(request, 'Szukaj dalej')
		

	
	return render(request, 'apka/search.html', {'form': form})	
	
	
