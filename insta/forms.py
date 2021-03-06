from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import *

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1']



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
        exclude = ['user', 'date_posted']
        fields = ['comment']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','bio']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']