
from django import forms

class ResumeForm(forms.Form):
    resume_text = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":60}), label="Paste your Resume")
