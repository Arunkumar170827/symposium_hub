from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student_name', 'college_name', 'email', 'event_type']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-input'}),
            'college_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'event_type': forms.Select(attrs={'class': 'form-select'}),
        }