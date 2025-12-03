from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            'user_name', 
            'user_email', 
            'user_phone',
            'incident_type', 
            'description', 
            'location',
            'evidence_file'
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
