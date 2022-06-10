from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
        
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'date_posted']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }  
class CommentForm(forms.Form):
    class Meta:
        model = Comments
        fields = ['comment']
