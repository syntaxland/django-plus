from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    sender_email = forms.EmailField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
