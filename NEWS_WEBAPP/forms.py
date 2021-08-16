from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User

from blogs.models import Post, Comment
from profiles.models import Profile


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}
        help_texts = {
            'username': None,
            'password2': None,
        }


class CustomEditProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    avatar = forms.ImageField(label='Profile Photo')
    media_url = forms.CharField(label='Media URL', max_length=300,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('bio', 'media_url', 'avatar')


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Write comment',
                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))

    class Meta:
        model = Comment
        fields = ('name', 'body')
