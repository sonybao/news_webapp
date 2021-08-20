from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from blogs.models import Post, Comment
from profiles.models import Profile


class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", 'first_name', 'last_name', 'password1', 'password2')
        field_classes = {'username': UsernameField}
        help_texts = {
            'username': None,
            'password2': None,
        }


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


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
    bio = forms.CharField(label='Bio', required=False,
                          widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    avatar = forms.ImageField(label='Profile Photo')
    media_url = forms.CharField(label='Media URL', max_length=300, required=False,
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


class CustomPostForm(forms.ModelForm):
    title = forms.CharField(label='Tiêu đề', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Nhập bình luận: ', required=True,
                           widget=CKEditorUploadingWidget)
    image = forms.ImageField(label='Ảnh thumbnail: ', required=False, widget=forms.ClearableFileInput)

    class Meta:
        model = Post
        fields = ('title','image','body')
