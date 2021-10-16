from django import forms
from .models import Language, Entry, EntryName


class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = [
            'name',
            'language',
        ]

    def __init__(self, *args, **kwargs):
        super(EntryCreationForm, self).__init__(*args, **kwargs)
        self.fields['language'].queryset = Language.objects.none()

        if 'language' in self.data:
            self.fields['language'].queryset = Language.objects.all()


class EntryMultipleCreationForm(forms.ModelForm):

    class Meta:
        model = EntryName
        fields = [
            'name',
            'language',
        ]
