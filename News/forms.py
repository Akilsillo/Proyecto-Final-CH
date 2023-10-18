from django import forms

class NewsForm(forms.Form):
    title = forms.CharField(max_length=30)
    date = forms.CharField(max_length=30)
    preview = forms.CharField(max_length=250)
    full_view = forms.CharField(max_length=2000)
    image = forms.ImageField()
    