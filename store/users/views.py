from typing import Any
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User, EmailVerification
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

from products.models import Basket
from common.views import TitleMixin


class UserRegistrationView(SuccessMessageMixin, TitleMixin,CreateView):
        model = User
        form_class = UserRegistrationForm
        template_name = 'users/register.html'
        success_url = reverse_lazy('users:login')
        success_message = 'Вы успешно зарегистрировались!'
        title = 'Registration'
        

class UserProfileView(UpdateView):
        model = User
        form_class = UserProfileForm
        template_name = 'users/profile.html'
        success_url = reverse_lazy('users:profile')
        
        def get_success_url(self) -> str:
                return reverse_lazy('users:profile', args=(self.object.id,))
        
        
        
        
class UserLoginView(TitleMixin, LoginView):
        template_name = 'users/login.html'
        form_class = UserLoginForm
        success_url = reverse_lazy('index')
        title = 'Store - Авторизация'

class EmailVerificationView(TitleMixin, TemplateView):
        title = 'Store - Подтверждение электронной почти'
        template_name = 'users/email_verification.html'
        
        def get(self, request, *args, **kwargs):
                code = kwargs['code']
                user = User.objects.get(email = kwargs['email'])
                email_verifications = EmailVerification.objects.filter(user=user, code=code)
                if email_verifications.exists() and not email_verifications.first().is_expride():
                        user.is_verifield = True
                        user.save()
                        return super(EmailVerificationView,self).get(request, *args, **kwargs)
                else:
                        return HttpResponseRedirect(reverse('index'))
                        
