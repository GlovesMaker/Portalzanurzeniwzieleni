from django import forms
from .models import Newsletter
from django import forms
from django.http import HttpResponse
from django.shortcuts import render


class NewsletterCreateForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = ['first_name',
                  'email', 
                  'regulamin_1',]
       

    def clean(self):
        
        regulamin_1 = self.cleaned_data.get('regulamin_1')
        

        if regulamin_1 == False:
            # Only do something if both fields are valid so far.

            raise forms.ValidationError('Musisz zaznaczyc pole regulaminu nr 1 oraz pole nie jestem robotem')


        

        #else:
            #raise forms.validate('Musisz')
            #raise forms.ValidationError('Zostales zarejstrowany prawidlowo')
            #return render(self, 'apka/created.html')


        
