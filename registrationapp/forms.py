
from typing import Any
from django import forms
from registrationapp.models import registration

class rgform(forms.ModelForm):
    class Meta:
        model=registration
        fields=['username','last_name','first_name','mob','password','email']

    def clean_username(self):
        user=self.cleaned_data['username']
        if not(user[0].isupper()) or not(len(user)>=6):
            raise ValueError('USERNAME SHOULD BE 6 CHARS AND FIRSY UPPERCASE')  
        return user

    def clean_mob(self):
        mob=self.cleaned_data['mob']
        if not(len(str(mob))==10):
            raise ValueError('mob should be 10 digits')
        return mob  


    def clean(self):
        user=self.cleaned_data['username']
        if not(user[0].isupper()) or not(len(user) >=6):
            raise ValueError('USERNAME SHOULD BE 6 CHARS AND FIRST UPPERCASE')

        mob=self.cleaned_data['mob']
        if str(mob)[0] not in ['6','7','8','9'] or len(str(mob))!=10:
            raise ValueError('MOB SHOULD BE 10 DIGITS AND STARTS WITH 6,7,8,9')
        
            

    
    