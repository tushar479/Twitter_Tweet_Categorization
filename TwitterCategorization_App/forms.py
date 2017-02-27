from django import forms

class NameForm(forms.Form):
    twitterusername = forms.CharField(label='twitter username', max_length=100)