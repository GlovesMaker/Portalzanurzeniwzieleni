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
                        messages.success(request, 'Zostałeś zapisany! Do zobaczenia. Oczekuj na wiadomość e-mail w przeciągu 24h!')
                        #return HttpResponse("ok");
                    else:
                        
                        messages.error(request, 'Nie zostałeś zapisany! Zaznacz pole "Nie jestem robotem"!')
                        #return HttpResponse("Invalid reCAPTCHA. Please try again.");
                   
       
        #context = {'form': form }
      
        
        
	return render(request, 'apka/base.html', {'form': form})
	
		

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

def search(request):


	if request.method=='POST':
		srch = request.POST['srh']
		if srch:
		
			match = Topic.objects.filter(Q(text__icontains=srch)|
                                                     Q(key_words__icontains=srch))
		
			if match:
				return render(request, 'apka/search.html', {'sr':match})	
			else:
				messages.error(request, 'Przykro nam, ale nie znaleziono żadnego z Twoich haseł. Spróbuj ponownie używając różnych słów kluczowych.')
		

	
	return render(request, 'apka/search.html')	
	

def contact(request):
        
        return render(request,'apka/contact.html')
	

def cooperation(request):

         return render(request,'apka/cooperation.html')

def worth_recommending(request):

        return render(request,'apka/worth_recommending.html')       
