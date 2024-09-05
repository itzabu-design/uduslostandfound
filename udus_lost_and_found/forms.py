from django import forms
from .models import LostReport, FoundReport

class LostReportForm(forms.ModelForm):
    class Meta:
        model = LostReport
        fields = ['item_name', 'description', 'date_lost']

class FoundReportForm(forms.ModelForm):
    class Meta:
        model = FoundReport
        fields = ['item_name', 'description', 'date_found', 'finder_name']
