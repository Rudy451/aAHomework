from django import forms

class UserForm(forms.Form):
  user_name = forms.CharField(label='Your name', max_length=80)
  password = forms.CharField(label="Your password", max_length=80)
