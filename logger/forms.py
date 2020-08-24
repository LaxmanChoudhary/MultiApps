from django import forms
from .models import *


class CreateForm(forms.ModelForm):
    #__init__ ref- https://stackoverflow.com/a/52760176
    def __init__(self, *args, **kwargs):
        users = kwargs.pop('user')
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['boards'].queryset = Board.objects.filter(creator=users)
    #datepicker ref- https://stackoverflow.com/a/3368268/8614751
    #forms/widgets ref-https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#styling-widget-instances
    class Meta:
        model = Topic
        fields = ['date', 'name', 'description', 'boards']

    date = forms.DateField(widget=forms.DateInput(attrs=
    	{'id':'datepicker'})
    )
    name = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)

    #forms.ModelChoiceField ref- https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#field-types
    #objects.filter() ref- https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-all-objects
    boards = forms.ModelChoiceField(queryset=None, widget=forms.Select)