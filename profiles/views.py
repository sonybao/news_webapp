from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import TemplateView, FormView
from NEWS_WEBAPP.forms import CustomRegisterForm, CustomEditProfileForm


class LoginSite(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_message = "Logged in successfully"
    success_url = "/"


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


class EditProfile(generic.UpdateView):
    model = User
    form_class = CustomEditProfileForm
    template_name = "edit_profile.html"
    success_url = '/profile/'

    def get_object(self):
        return self.request.user


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
