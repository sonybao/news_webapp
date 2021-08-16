from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Profile
from django.views import generic
from django.views.generic import TemplateView, FormView, UpdateView
from NEWS_WEBAPP.forms import CustomRegisterForm, CustomEditProfileForm, ProfileForm


class LoginSite(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_message = "Logged in successfully"


class RegisterSite(FormView):
    template_name = 'register.html'
    form_class = CustomRegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email']
        )
        messages.success(self.request, 'Register successful')
        return redirect('login')


class LogoutSite(LogoutView):
    template_name = 'profile.html'


class ProfileSite(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


# class EditProfile(generic.UpdateView):
#     model = User
#     form_class = CustomEditProfileForm
#     template_name = "edit_profile.html"
#     success_url = '/profile/'
#
#     def get_object(self):
#         return self.request.user
#
#
# class BioProfileView(generic.UpdateView):
#     model = Profile
#     fields = ('bio', 'avatar', 'media_url')
#     template_name = 'bio_profile.html'
#     success_url = '/profile/'
#
#     def get_object(self):
#         return self.request.user

@login_required
def update_profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = CustomEditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = CustomEditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class PasswordChange(PasswordChangeView):
    from_class = PasswordChangeView
    template_name = 'pass_change.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        self.request.session.flush()
        logout(self.request)
        messages.success(self.request, 'Changed Password Successfully')
        return super().form_valid(form)
