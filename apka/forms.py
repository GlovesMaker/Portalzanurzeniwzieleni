from django import forms
from .models import Newsletter
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ValidationError

class NewsletterCreateForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = ['first_name',
                  'email', 
                  'regulamin_1',]
       

    def clean(self):
        
        regulamin_1 = self.cleaned_data.get('regulamin_1')
        

        if regulamin_1 == False:
            #return HttpResponse('Zaznaczyc pole regulaminu');
            # Only do something if both fields are valid so far.
          
            raise forms.ValidationError("Zaznaczyc pole regulaminu")
        

        

        #else:
            #raise forms.validate('Musisz')
            #raise forms.ValidationError('Zostales zarejstrowany prawidlowo')
            #return render(self, 'apka/base.html')


        
