from django import forms


class ImagesToPDF(forms.Form):
    images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))
