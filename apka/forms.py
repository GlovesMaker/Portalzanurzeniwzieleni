from django import forms
from .models import Newsletter
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

class NewsletterCreateForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = ['first_name',
                  'email', 
                  'regulamin_1',]
       

    def clean(request):
        
        regulamin_1 = request.cleaned_data.get('regulamin_1')
        

        if regulamin_1 == False:
            # Only do something if both fields are valid so far.

            #raise forms.ValidationError('Musisz zaznaczyc pole regulaminu nr 1 oraz pole nie jestem robotem')
            messages.error(request, 'Zaznaczyc pole regulaminu')

        

        #else:
            #raise forms.validate('Musisz')
            #raise forms.ValidationError('Zostales zarejstrowany prawidlowo')
            #return render(self, 'apka/created.html')


        
