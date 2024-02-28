from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import UserRegistrationView, UserLoginView, UserProfileView, EmailVerificationView
from django.contrib.auth.views import LogoutView

app_name='users'

urlpatterns = [
        path('registration/', UserRegistrationView.as_view(), name = 'register'),
        path('login/', UserLoginView.as_view(), name = 'login'),
        path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name = 'profile'),
        path('logout/',LogoutView.as_view(), name='logout'),
        path('verify/<str:email>/<uuid:code>',EmailVerificationView.as_view(), name='email_verification'),
]