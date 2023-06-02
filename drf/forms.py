from .models import Book
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'desc', 'pub_date']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control'}),
        #     'desc': forms.Textarea(attrs={'class': 'form-control'}),
        # }

    
class BookSearchForm(forms.Form):
    # query = forms.CharField(required=False)
    query = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter text here',
            'class': 'border rounded-md py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            })
    )
