from django import forms
from app.models import RegForm
from datetime import date 

class UserForm(forms.ModelForm):
    DoB = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_DoB(self):
        dob = self.cleaned_data['DoB']
        age = (date.today() - dob).days / 365
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old')
        return dob

    Phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))

    def clean_Phone(self):
        phone = self.cleaned_data['Phone']
        length = len(str(phone))
        if length < 10 and length > 14:
            raise forms.ValidationError('You must minimum 10 digit number ')
        return phone
    
    class Meta:
        model = RegForm
        fields = "__all__"

